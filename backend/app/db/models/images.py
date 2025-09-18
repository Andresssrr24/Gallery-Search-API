from app.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, DateTime, Float, ForeignKey, Integer
from typing import Optional
from datetime import datetime

class Image(Base):
    __tablename__ = "images"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    url: Mapped[str] = mapped_column(String, nullable=False)
    description_embedding: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    description: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    size: Mapped[float] = mapped_column(Float, nullable=False)  # In MB
    #tags: Mapped[Optional[str]] = mapped_column(String, nullable=True) #? Proposed by me
    created_at: Mapped[DateTime] = mapped_column(DateTime, nullable=False, default=datetime.now)
