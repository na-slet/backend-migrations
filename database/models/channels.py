import uuid

from enum import Enum

from sqlalchemy import Boolean, Column, String, TIMESTAMP, Enum, INTEGER, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, TSVECTOR


from database.models.users import Users
from database.alembic.base import DeclarativeBase



class Channels(DeclarativeBase):
    __tablename__ = "channels"

    id = Column(UUID, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    subscribed = Column(INTEGER, default=0)
    creator_id = Column(UUID, ForeignKey(Users.id, ondelete="CASCADE"), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False)

