import uuid
from enum import Enum
from datetime import datetime

from sqlalchemy import Column, String, TIMESTAMP, INTEGER, ForeignKey, FLOAT
from sqlalchemy.dialects.postgresql import UUID, ENUM
from pytz import UTC

from .users import Users
from .base import DeclarativeBase


class EventType(str, Enum):
    SCOUT: str = 'SCOUT'
    TEENAGER: str = 'TEENAGER'
    JUNIOR: str = 'JUNIOR'
    FAMILY: str = 'FAMILY'


class Events(DeclarativeBase):
    __tablename__ = "events"

    id = Column(UUID, unique=True, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    city = Column(String, nullable=True) # TODO: make it enum
    start_date = Column(TIMESTAMP(timezone=True), nullable=False)
    end_date = Column(TIMESTAMP(timezone=True), nullable=False)
    total_places = Column(INTEGER, nullable=True)
    url_link = Column(String, nullable=True) # social network link
    event_type = Column(ENUM(EventType), nullable=True)
    union_full = Column(String, nullable=True)
    union_short = Column(String, nullable=True)
    min_age = Column(INTEGER, nullable=True)
    address = Column(String, nullable=False)
    latitude = Column(FLOAT, nullable=True) # TODO: make it point
    longitude = Column(FLOAT, nullable=True)
    logo_id = Column(String, nullable=True)
    creator_id = Column(UUID, ForeignKey(Users.id, ondelete="CASCADE"), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, default = lambda x: datetime.now(UTC))
    # TODO: add full-text search

