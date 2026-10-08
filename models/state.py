#!/usr/bin/python3
"""Defines the State class."""

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """State class."""

    if models.storage_t == "db":
        __tablename__ = "states"

        name = Column(String(128), nullable=False)
        cities = relationship(
            "City",
            backref="state",
            cascade="all, delete, delete-orphan"
        )
    else:
        name = ""

        @property
        def cities(self):
            """Return the list of City objects linked to this State."""
            from models.city import City

            return [
                city for city in models.storage.all(City).values()
                if city.state_id == self.id
            ]
