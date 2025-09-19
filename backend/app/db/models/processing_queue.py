from app.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, Datetime, String, ForeignKey
from datetime import datetime

class ProcessingQueue(Base):
    __tablename__ = "processing_queue"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    image_id: Mapped[int] = mapped_column(ForeignKey("images.id"), nullable=False)
    status: Mapped[str] = mapped_column(String(50), nullable=False)
    retries_left: Mapped[int] = mapped_column(Integer, nullable=False, default=3)
    attempts: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    priority: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    started_at: Mapped[Datetime] = mapped_column(Datetime, nullable=False)
    completed_at: Mapped[Datetime] = mapped_column(Datetime, nullable=False)
    last_attempt_at: Mapped[Datetime] = mapped_column(Datetime, nullable=False)
    error_message: Mapped[str] = mapped_column(String, nullable=True)
    created_at: Mapped[Datetime] = mapped_column(Datetime, nullable=False, default=datetime.now)
