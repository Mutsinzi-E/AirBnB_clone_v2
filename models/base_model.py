#!/usr/bin/python3
"""Defines the BaseModel class."""

import uuid
from datetime import datetime

import models
from sqlalchemy import Column, DateTime, String
from sqlalchemy.ext.declarative import declarative_base


time = "%Y-%m-%dT%H:%M:%S.%f"

if models.storage_t == "db":
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """Base class for all AirBnB models."""

    if models.storage_t == "db":
        id = Column(String(60), primary_key=True)
        created_at = Column(DateTime, default=datetime.utcnow)
        updated_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance."""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)

            if isinstance(getattr(self, "created_at", None), str):
                self.created_at = datetime.strptime(
                    self.created_at, time
                )
            elif not hasattr(self, "created_at"):
                self.created_at = datetime.utcnow()

            if isinstance(getattr(self, "updated_at", None), str):
                self.updated_at = datetime.strptime(
                    self.updated_at, time
                )
            elif not hasattr(self, "updated_at"):
                self.updated_at = datetime.utcnow()

            if getattr(self, "id", None) is None:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at

            if models.storage_t != "db":
                models.storage.new(self)

    def __str__(self):
        """Return the string representation of the instance."""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
        )

    def save(self):
        """Update updated_at and save the object."""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

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

    def delete(self):
        """Delete the current instance from the storage."""
        models.storage.delete(self)
