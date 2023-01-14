import uuid
from datetime import datetime

from sqlalchemy import Column, String, TIMESTAMP, INTEGER, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from pytz import UTC

from .users import Users
from .base import DeclarativeBase


class Events(DeclarativeBase):
    __tablename__ = "events"

    id = Column(UUID, unique=True, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    city = Column(String, nullable=True) # TODO: make it enum
    start_date = Column(TIMESTAMP(timezone=True), nullable=False)
    end_date = Column(TIMESTAMP(timezone=True), nullable=False)
    total_places = Column(INTEGER, nullable=False)
    url_link = Column(String, nullable=True) # social network link
    address = Column(String, nullable=False)
    logo_id = Column(String, nullable=True)
    creator_id = Column(UUID, ForeignKey(Users.id, ondelete="CASCADE"), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, default = lambda x: datetime.now(UTC))
    # TODO: add full-text search

