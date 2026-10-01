#!/usr/bin/python3
"""Defines the City class."""

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """City class."""

    if models.storage_t == "db":
        __tablename__ = "cities"

        state_id = Column(
            String(60),
            ForeignKey("states.id"),
            nullable=False
        )
        name = Column(String(128), nullable=False)

        places = relationship(
            "Place",
            backref="city",
            cascade="all, delete, delete-orphan"
        )
    else:
        state_id = ""
        name = ""
