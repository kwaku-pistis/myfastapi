from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String)
    username = Column(String)
    email = Column(String, unique=True)
    phone_number = Column(String, unique=True)
    uid = Column(String, unique=True)
    user_type = Column(String)
    user_role = Column(String)
    
    # items = relationship("Item", back_populates="owner")
    
    def __repr__(self):
        return "<User(full_name='%s', username='%s', email='%s', uid='%s', phone_number='%s', user_type='%s', user_role='%s')>" % (
                             self.full_name, self.username, self.email, self.uid, self.phone_number, self.user_type, self.user_role)
        
        
# class Item(Base):
#     __tablename__ = "items"

#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, index=True)
#     description = Column(String, index=True)
#     owner_id = Column(Integer, ForeignKey("users.id"))

#     owner = relationship("User", back_populates="items")