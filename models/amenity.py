#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from os import getenv


class Amenity(BaseModel, Base):
    """Amenities"""
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship(
        "Place", secondary="place_amenity")
    # we may add/adjust here for many-to-many relationship
    # maybe add to above line back_populates="amenities"
