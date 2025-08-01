from database import Base
from sqlalchemy import Column, Integer, Boolean, Text, String, ForeignKey, FLOAT
from sqlalchemy_utils.types import ChoiceType
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__='users'
    id = Column(Integer, primary_key=True)
    username = Column(String(25),unique=True)
    email = Column(String(80),unique=True)
    password = Column(Text, nullable=True)
    is_staff = Column(Boolean, default=False)
    is_active = Column(Boolean, default=False)
    orders= relationship('Order', back_populates='users')
    def __repr__(self):
        return f"<User {self.username}>"
    


class Product(Base):  
    __tablename__='products'
    id=Column(Integer, primary_key=True) 
    name=Column(String(25),unique=True) 
    category=Column(String(25),unique=True)
    description=Column(String(80),unique=True) 
    price=Column(FLOAT)
    def __repr__(self):
        return f"<Product {self.name}>"
    
class Order(Base):
    ORDER_STATUSES=(
    ('PENDING','pending'), ('IN-TRANSIT', 'in-transit'), ('DELIVERED', 'delivered')
    )
    PIZZA_SIZES = (
        ('SMALL', 'small'),
        ('MEDIUM', "medium"),
        ('LARGE','large'),
        ('EXTRA-LARGE','extra-large')
    )
    __tablename__='orders'
    id = Column(Integer, primary_key=True)
    quantity = Column(Integer, nullable=False)
    order_status = Column(ChoiceType(choices=ORDER_STATUSES), default='PENDING')
    pizza_size = Column(ChoiceType(choices=PIZZA_SIZES), default='SMALL')
    user_id = Column(Integer, ForeignKey('users.id'))
    users = relationship('User', back_populates='orders')
    def __repr__(self):
        return f"<Order {self.id}>"