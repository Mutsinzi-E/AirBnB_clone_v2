#!/usr/bin/python3
"""Defines the Amenity class."""

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    """Amenity class."""

    if models.storage_t == "db":
        __tablename__ = "amenities"

        name = Column(String(128), nullable=False)
    else:
        name = ""
