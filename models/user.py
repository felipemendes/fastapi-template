from uuid import UUID, uuid4

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String

from base import Base

class User(Base):
    __tablename__ = 'user'

    # Define the columns
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String)
    email = Column(String)
