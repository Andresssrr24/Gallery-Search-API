from app.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Float, Integer
from typing import Optional

class Subscription(Base):
    __tablename__ = "subscription_plans"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    price: Mapped[float] = mapped_column(Float, nullable=False)  # In USD
    storage_limit: Mapped[float] = mapped_column(Float, nullable=False)  # In GB
    image_size_limit: Mapped[float] = mapped_column(Float, nullable=False)  # In MB
    max_face_searches_per_day: Mapped[int] = mapped_column(Integer, nullable=False)
    features: Mapped[Optional[str]] = mapped_column(String, nullable=True) # In JSON format
    #daily_upload_limit: Mapped[int] = mapped_column(Integer, nullable=False) #? Proposed by me
    #max_images_per_month: Mapped[int] = mapped_column(Integer, nullable=False) #? Proposed by me
    