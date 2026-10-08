#!/usr/bin/python3
"""Defines the BaseModel class."""

import uuid
from datetime import datetime

import models
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base


if models.storage_t == "db":
    Base = declarative_base()
else:
    Base = object

time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """Base class for all AirBnB models."""

    if models.storage_t == "db":
        id = Column(
            String(60),
            unique=True,
            primary_key=True,
            nullable=False
        )
        created_at = Column(
            DateTime,
            default=datetime.utcnow,
            nullable=False
        )
        updated_at = Column(
            DateTime,
            default=datetime.utcnow,
            nullable=False
        )

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue

                if key == "created_at" or key == "updated_at":
                    if isinstance(value, str):
                        value = datetime.strptime(value, time)

                setattr(self, key, value)

    def __str__(self):
        """Return the string representation of the instance."""
        attributes = self.__dict__.copy()
        attributes.pop("_sa_instance_state", None)
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            attributes
        )

    def save(self):
        """Update updated_at and save the object."""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def delete(self):
        """Delete the current instance from storage."""
        models.storage.delete(self)

    def to_dict(self):
        """Return a dictionary representation of the instance."""
        new_dict = self.__dict__.copy()

        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(time)

        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime(time)

        new_dict["__class__"] = self.__class__.__name__
        new_dict.pop("_sa_instance_state", None)

        return new_dict
