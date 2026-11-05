from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from .database import Base

class Monitor(Base):
    __tablename__ = "monitors"
    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, nullable=False, unique=True)
    name = Column(String, nullable=False)
    interval_seconds = Column(Integer, default=60)
    timeout_ms = Column(Integer, default=5000)
    created_at = Column(DateTime, default=datetime.utcnow)
