"""
Channel Settings Models - نموذج إعدادات القنوات
"""
from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from app.database import Base


class ChannelSetting(Base):
    __tablename__ = "channel_settings"
    id = Column(Integer, primary_key=True)
    channel_id = Column(String, unique=True, nullable=False)
    channel_link = Column(String, nullable=False)
    channel_name = Column(String, nullable=True)
    is_required = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<ForceJoinChannel {self.channel_id}>"


class ChannelSetting(Base):
    """نموذج إعدادات النشر"""
    __tablename__ = "channel_settings"

    id = Column(Integer, primary_key=True, index=True)
    channel_id = Column(String(100), nullable=False, unique=True)
    channel_name = Column(String(255), nullable=True)
    auto_post = Column(Boolean, default=False)
    post_template = Column(String(5000), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<ChannelSetting {self.channel_id}>"
