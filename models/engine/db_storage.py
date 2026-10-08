#!/usr/bin/python3
"""Contains the DBStorage class."""

import models
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {
    "Amenity": Amenity,
    "City": City,
    "Place": Place,
    "Review": Review,
    "State": State,
    "User": User,
}


class DBStorage:
    """Interact with the MySQL database."""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object."""
        mysql_user = getenv("HBNB_MYSQL_USER")
        mysql_pwd = getenv("HBNB_MYSQL_PWD")
        mysql_host = getenv("HBNB_MYSQL_HOST")
        mysql_db = getenv("HBNB_MYSQL_DB")
        hbnb_env = getenv("HBNB_ENV")

        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(
                mysql_user, mysql_pwd, mysql_host, mysql_db
            ),
            pool_pre_ping=True
        )

        if hbnb_env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query objects from the current database session."""
        new_dict = {}

        for class_name, model_class in classes.items():
            if cls is None or cls is model_class or cls == class_name:
                objects = self.__session.query(model_class).all()

                for obj in objects:
                    key = "{}.{}".format(
                        obj.__class__.__name__,
                        obj.id
                    )
                    new_dict[key] = obj

        return new_dict

    def new(self, obj):
        """Add an object to the current database session."""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete an object from the current database session."""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Reload data from the database."""
        Base.metadata.create_all(self.__engine)

        session_factory = sessionmaker(
            bind=self.__engine,
            expire_on_commit=False
        )

        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Close the current database session."""
        self.__session.close()
