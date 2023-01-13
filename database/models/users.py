import uuid

from enum import Enum

from sqlalchemy import Boolean, Column, String, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID, TSVECTOR, ENUM

from ..migrator.base import DeclarativeBase

class Roles(Enum):
    REGULAR: str = "REGULAR"
    CREATOR: str = "CREATOR"

class Gender(Enum):
    MALE: str = "male"
    FEMALE: str = "female"

class Users(DeclarativeBase):
    __tablename__ = "users"

    id = Column(UUID, unique=True, primary_key=True, default=lambda: str(uuid.uuid4()))
    role = Column(ENUM(Roles), nullable=False, default=Roles.REGULAR)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    gender = Column(ENUM(Gender), nullable=True)
    phone = Column(String, primary_key=True)
    email = Column(String, primary_key=True)
    hashed_password = Column(String, nullable=False)
    avatar_id = Column(String, nullable=True)
    vk_link = Column(String, nullable=True)
    tg_link = Column(String, nullable=True)
    birth_date = Column(TIMESTAMP(timezone=True), nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, default = lambda x: datetime.now(UTC))
