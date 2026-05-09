"""
Channel Service - خدمة القنوات (الاشتراك الإجباري وإعدادات النشر)
"""
from typing import List, Tuple, Optional
from aiogram import Bot
from sqlalchemy.orm import Session
from app.models.channel_setting import Channel


class ChannelService:
    """خدمة إدارة القنوات المتكاملة"""

    def __init__(self, db: Session):
        self.db = db

    # ==========================================
    # إدارة القنوات الأساسية
    # ==========================================

    def add_channel(
        self,
        channel_id: str,
        channel_name: Optional[str] = None,
        channel_link: Optional[str] = None,
        is_required: bool = True
    ) -> Channel:
        """إضافة قناة جديدة (أو تحديثها إذا وجدت)"""
        existing = self.get_channel(channel_id)
        if existing:
            # تحديث البيانات الموجودة
            if channel_name is not None:
                existing.channel_name = channel_name
            if channel_link is not None:
                existing.channel_link = channel_link
            if is_required is not None:
                existing.is_required = is_required
            self.db.commit()
            self.db.refresh(existing)
            return existing

        channel = Channel(
            channel_id=channel_id,
            channel_name=channel_name,
            channel_link=channel_link,
            is_required=is_required
        )
        self.db.add(channel)
        self.db.commit()
        self.db.refresh(channel)
        return channel

    def remove_channel(self, channel_id: str) -> bool:
        """حذف قناة"""
        channel = self.get_channel(channel_id)
        if not channel:
            return False
        self.db.delete(channel)
        self.db.commit()
        return True

    def get_channel(self, channel_id: str) -> Optional[Channel]:
        """الحصول على قناة بالمعرف (ID أو @username)"""
        return self.db.query(Channel).filter(Channel.channel_id == channel_id).first()

    def get_all_channels(self, required_only: bool = False) -> List[Channel]:
        """الحصول على جميع القنوات (أو فقط المطلوبة للإجبار)"""
        query = self.db.query(Channel)
        if required_only:
            query = query.filter(Channel.is_required == True)
        return query.all()

    def update_channel(
        self,
        channel_id: str,
        channel_name: Optional[str] = None,
        channel_link: Optional[str] = None,
        is_required: Optional[bool] = None
    ) -> Optional[Channel]:
        """تحديث بيانات قناة"""
        channel = self.get_channel(channel_id)
        if not channel:
            return None
        if channel_name is not None:
            channel.channel_name = channel_name
        if channel_link is not None:
            channel.channel_link = channel_link
        if is_required is not None:
            channel.is_required = is_required
        self.db.commit()
        self.db.refresh(channel)
        return channel

    # ==========================================
    # التحقق من الاشتراك
    # ==========================================

    async def check_subscription(self, bot: Bot, user_id: int, channel_id: str) -> bool:
        """فحص اشتراك مستخدم واحد في قناة واحدة"""
        try:
            member = await bot.get_chat_member(chat_id=channel_id, user_id=user_id)
            return member.status in ['member', 'administrator', 'creator']
        except Exception:
            return False

    async def check_all_subscriptions(self, bot: Bot, user_id: int) -> Tuple[bool, List[Channel]]:
        """التحقق من اشتراك المستخدم في جميع القنوات المطلوبة (is_required=True)"""
        channels = self.get_all_channels(required_only=True)
        if not channels:
            return True, []

        not_subscribed = []
        for ch in channels:
            try:
                member = await bot.get_chat_member(chat_id=ch.channel_id, user_id=user_id)
                if member.status in ['left', 'kicked']:
                    not_subscribed.append(ch)
            except Exception:
                # في حالة خطأ (قناة غير موجودة أو البوت ليس مشرفاً) نعتبره غير مشترك
                not_subscribed.append(ch)
        return len(not_subscribed) == 0, not_subscribed

    # ==========================================
    # إعدادات النشر التلقائي
    # ==========================================

    def setup_auto_post(
        self,
        channel_id: str,
        auto_post: bool = False,
        post_template: Optional[str] = None
    ) -> Optional[Channel]:
        """تفعيل/تعطيل النشر التلقائي وتعيين القالب"""
        channel = self.get_channel(channel_id)
        if not channel:
            return None
        channel.auto_post = auto_post
        if post_template is not None:
            channel.post_template = post_template
        self.db.commit()
        self.db.refresh(channel)
        return channel

    def get_setting(self, channel_id: str) -> Optional[Channel]:
        """الحصول على إعدادات قناة (نفس get_channel)"""
        return self.get_channel(channel_id)

    def get_all_settings(self) -> List[Channel]:
        """الحصول على جميع القنوات (مع إعداداتها)"""
        return self.get_all_channels()

    def toggle_auto_post(self, channel_id: str) -> Optional[Channel]:
        """تبديل حالة النشر التلقائي لقناة"""
        channel = self.get_channel(channel_id)
        if not channel:
            return None
        channel.auto_post = not channel.auto_post
        self.db.commit()
        self.db.refresh(channel)
        return channel
