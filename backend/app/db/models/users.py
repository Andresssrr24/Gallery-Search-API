from app.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Boolean, Datetime, Integer, Float
from typing import Optional
from datetime import datetime

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[Datetime] = mapped_column(Datetime, nullable=False, default=datetime.now)
    total_storage_limit: Mapped[float] = mapped_column(Float, default=0.5)  # In GB
    used_storage: Mapped[float] = mapped_column(Float, default=0.0)  # In GB
    image_size_limit: Mapped[int] = mapped_column(Integer, default=5)  # In MB
    #daily_upload_limit: Mapped[int] = mapped_column(Integer, default=20) #? Proposed by me
    subscription_tier: Mapped[str] = mapped_column(String(50), default="free")
    profile_picture_url: Mapped[Optional[str]] = mapped_column(String, nullable=True)