from app.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, ForeignKey

class FaceEmbeddings(Base):
    __tablename__ = "face_embeddings"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    image_id: Mapped[int] = mapped_column(ForeignKey("images.id"), nullable=False)
    face_embedding: Mapped[str] = mapped_column(String, nullable=False)  