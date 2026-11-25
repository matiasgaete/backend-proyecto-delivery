from sqlalchemy import Integer, String, Text, TIMESTAMP, func
from sqlalchemy.orm import DeclarativeBase, mapped_column


class Base(DeclarativeBase):
    pass


class UserSession(Base):
    __tablename__ = "user_sessions"

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id = mapped_column(Integer, nullable=False)
    device_id = mapped_column(String(255), nullable=False)
    refresh_token = mapped_column(Text, nullable=False)
    expires_at = mapped_column(TIMESTAMP(timezone=True), nullable=False)
    created_at = mapped_column(TIMESTAMP(timezone=True), server_default=func.now())