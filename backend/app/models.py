from sqlalchemy import Column, Integer, String, Text, Numeric, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Issue(Base):
    __tablename__ = 'issues'
    id = Column(Integer, primary_key=True, index=True)
    tracking_id = Column(String(50), unique=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text)
    category = Column(String(80))
    status = Column(String(30), default='open', index=True)
    lat = Column(Numeric(9,6))
    lon = Column(Numeric(9,6))
    image_url = Column(String(500))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
