import uuid
from enum import Enum
from datetime import datetime

from sqlalchemy import Column, String, TIMESTAMP, INTEGER, ForeignKey, FLOAT, NUMERIC
from sqlalchemy.dialects.postgresql import UUID, ENUM
from pytz import UTC

from .users import Users
from .base import DeclarativeBase
from .unions import Unions


class EventType(str, Enum):
    SCOUT = 'SCOUT'
    TEENAGER = 'TEENAGER'
    JUNIOR = 'JUNIOR'
    FAMILY = 'FAMILY'


class CategoryType(str, Enum):
    EVENT = 'EVENT'
    CAMP = 'CAMP'


class ColorVariant(str, Enum):
    RED = "RED"
    ORANGE = "ORANGE"
    YELLOW = "YELLOW"
    GREEN = "GREEN"
    GRAY = "GRAY"


class LogoVariant(str, Enum):
    SCOUT = "SCOUT"
    CAMP = "CAMP"
    FOREST = "FOREST"
    TRIPLE_DANCING = "TRIPLE_DANCING"
    PAIR_STANDING = "PAIR_STANDING"
    TRIPLE_STANDING = "TRIPLE_STANDING"
    TRIPLE_SITTING = "TRIPLE_SITTING"


class Events(DeclarativeBase):
    __tablename__ = "events"

    id = Column(UUID, unique=True, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    short_description = Column(String, nullable=True)
    price = Column(NUMERIC, nullable=True)
    logo_variant = Column(ENUM(LogoVariant), nullable=False)
    city = Column(String, nullable=True) # TODO: make it enum
    reg_end_date = Column(TIMESTAMP(timezone=True), nullable=False)
    start_date = Column(TIMESTAMP(timezone=True), nullable=False)
    end_date = Column(TIMESTAMP(timezone=True), nullable=False)
    total_places = Column(INTEGER, nullable=True)
    url_link = Column(String, nullable=True) # social network link
    category_type = Column(ENUM(CategoryType), nullable=False)
    event_type = Column(ENUM(EventType), nullable=False)
    union_id = Column(UUID, ForeignKey(Unions.id, ondelete="SET NULL"), nullable=True)
    min_age = Column(INTEGER, nullable=True)
    max_age = Column(INTEGER, nullable=True)
    address = Column(String, nullable=False)
    latitude = Column(FLOAT, nullable=True) # TODO: make it point
    longitude = Column(FLOAT, nullable=True)
    creator_id = Column(UUID, ForeignKey(Users.id, ondelete="CASCADE"), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, default = lambda x: datetime.now(UTC))
    # TODO: add full-text search

