from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import validates
import uuid
from slugify import slugify

# Create a declarative base class
Base = declarative_base()


# Define the abstract base class
class BaseModelWithUUID(Base):
    __tablename__ = "base_model"
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)
    uid = Column(
        String, unique=True, index=True, default=lambda: str(uuid.uuid4())
    )  # Corrected the default for uuid
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


class NameSlugDescriptionBaseModel(BaseModelWithUUID):
    __abstract__ = True

    name = Column(String, index=True)
    slug = Column(String, index=True)
    description = Column(String)

    @validates("name")
    def update_slug(self, key, name):
        self.slug = slugify(name)
        return name  # Make sure to return the name to complete the validation chain
