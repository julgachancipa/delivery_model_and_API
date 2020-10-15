from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Order(Base):

    __tablename__ = 'orders'

    order_id = Column(Integer, primary_key=True)
    store_id = Column(Integer, nullable=False)
    to_user_distance = Column(Float, nullable=False)
    to_user_elevation = Column(Float, nullable=False)
    total_earning = Column(Integer, nullable=False)
    created_at = Column(String, nullable=False)
    taken = Column(Integer, nullable=False)
