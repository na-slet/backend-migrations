import uuid
from datetime import datetime

from enum import Enum

from sqlalchemy import Column, String, TIMESTAMP, ForeignKey, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID, ENUM
from pytz import UTC

from .base import DeclarativeBase
from .users import Users


class CredentialTypes(str, Enum):
    BASIC: str = 'BASIC'
    VK: str = 'VK'
    GOOGLE: str = 'GOOGLE'


class Credentials(DeclarativeBase):
    __tablename__ = "credentials"

    id = Column(UUID, unique=True, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(UUID, ForeignKey(Users.id, ondelete="CASCADE"), nullable=False)
    credential_type = Column(ENUM(CredentialTypes), nullable=False, default=CredentialTypes.BASIC)
    value = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, default = lambda x: datetime.now(UTC))

    __table_args__ = (
        UniqueConstraint(user_id, credential_type),
    )