"""
Channel Model - نموذج موحد للقنوات (الاشتراك الإجباري وإعدادات النشر)
"""
from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text
from app.database import Base

class Channel(Base):
    """نموذج موحد لقنوات الاشتراك الإجباري وإعدادات النشر"""
    __tablename__ = "channels"  # اسم جديد لمنع التعارض مع الجدول القديم

    id = Column(Integer, primary_key=True, index=True)
    channel_id = Column(String(100), unique=True, nullable=False, index=True)
    channel_name = Column(String(255), nullable=True)
    channel_link = Column(String(500), nullable=True)
    
    # للاشتراك الإجباري
    is_required = Column(Boolean, default=True)
    
    # لإعدادات النشر التلقائي
    auto_post = Column(Boolean, default=False)
    post_template = Column(Text, nullable=True)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<Channel {self.channel_id}>"
