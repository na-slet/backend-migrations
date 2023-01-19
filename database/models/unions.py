import uuid
from enum import Enum
from datetime import datetime

from sqlalchemy import Column, String, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from pytz import UTC

from .base import DeclarativeBase


class Unions(DeclarativeBase):
    __tablename__ = "unions"

    id = Column(UUID, unique=True, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, unique=True, nullable=False)
    short_name = Column(String, unique=True, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, default = lambda x: datetime.now(UTC))

