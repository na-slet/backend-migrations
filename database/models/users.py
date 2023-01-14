import uuid
from datetime import datetime

from enum import Enum

from sqlalchemy import Column, String, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID, ENUM
from pytz import UTC

from .base import DeclarativeBase

class Roles(str, Enum):
    REGULAR: str = "REGULAR"
    CREATOR: str = "CREATOR"
    ADMIN: str = "ADMIN"


class Genders(str, Enum):
    MALE: str = "male"
    FEMALE: str = "female"


class Users(DeclarativeBase):
    __tablename__ = "users"

    id = Column(UUID, unique=True, primary_key=True, default=lambda: str(uuid.uuid4()))
    role = Column(ENUM(Roles), nullable=False, default=Roles.REGULAR)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    gender = Column(ENUM(Genders), nullable=True)
    phone = Column(String, primary_key=True)
    email = Column(String, primary_key=True)
    avatar_id = Column(String, nullable=True)
    tg_link = Column(String, nullable=True)
    birth_date = Column(TIMESTAMP(timezone=True), nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, default = lambda x: datetime.now(UTC))
