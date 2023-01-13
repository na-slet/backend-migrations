import uuid
from datetime import datetime
from enum import Enum

from sqlalchemy import Boolean, Column, String, TIMESTAMP, Enum, INTEGER, ForeignKey, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID, TSVECTOR


from .users import Users
from .events import Events
from ..migrator.base import DeclarativeBase



class Subscribed(DeclarativeBase):
    __tablename__ = "subscribed"

    id = Column(UUID, unique=True, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(UUID, ForeignKey(Users.id, ondelete="CASCADE"), nullable=False)
    event_id = Column(UUID, ForeignKey(Events.id, ondelete="CASCADE"), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, default = lambda x: datetime.now(UTC))

    __table_args__ = (UniqueConstraint("user_id", "event_id"),)
