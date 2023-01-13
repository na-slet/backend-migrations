import uuid
from datetime import datetime
from enum import Enum

from sqlalchemy import Boolean, Column, String, TIMESTAMP, Enum, INTEGER, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, TSVECTOR


from .users import Users
from .channels import Channels
from ..migrator.base import DeclarativeBase



class Events(DeclarativeBase):
    __tablename__ = "events"

    id = Column(UUID, unique=True, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    city = Column(String, nullable=True) # TODO: make it enum
    start_date = Column(TIMESTAMP(timezone=True), nullable=False)
    end_date = Column(TIMESTAMP(timezone=True), nullable=False)
    total_places = Column(INTEGER, nullable=False)
    available_places = Column(INTEGER, nullable=False)
    rating = Column(INTEGER, default=0)
    link = Column(String, nullable=True) # social network link
    address = Column(String, nullable=False)
    logo_id = Column(String, nullable=True)
    creator_id = Column(UUID, ForeignKey(Users.id, ondelete="CASCADE"), nullable=False)
    channel_id = Column(UUID, ForeignKey(Channels.id, ondelete="CASCADE"), nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, default = lambda x: datetime.now(UTC))
    # TODO: add full-text search

