# created from response - used to create database and project
#  should run without error
#  if not, check for decimal, indent, or import issues

import decimal

import logging



logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

import sqlalchemy



from sqlalchemy.sql import func  # end imports from system/genai/create_db_models_inserts/create_db_models_prefix.py

from logic_bank.logic_bank import Rule

from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, Float, DateTime, Text, UniqueConstraint
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
import datetime
import os

Base = declarative_base()

class Customer(Base):
    """description: Represents a customer with personal and credit information."""

    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    credit_limit = Column(Float, nullable=False)
    balance = Column(Float, nullable=False, default=0.0)

class Order(Base):
    """description: Represents an order created by a customer, containing multiple items."""

    __tablename__ = 'order'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customer.id'), nullable=False)
    date_created = Column(DateTime, default=datetime.datetime.now)
    date_shipped = Column(DateTime, nullable=True)
    amount_total = Column(Float, nullable=False, default=0.0)
    notes = Column(Text, nullable=True)

class Product(Base):
    """description: Represents a product available for purchase."""

    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    unit_price = Column(Float, nullable=False)

class Item(Base):
    """description: Represents an item in an order, linked to a product."""

    __tablename__ = 'item'
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('order.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('product.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    unit_price = Column(Float, nullable=False)
    amount = Column(Float, nullable=False, default=0.0)

class Address(Base):
    """description: Represents an address associated with a customer, can be billing or shipping."""

    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customer.id'), nullable=False)
    street = Column(String, nullable=False)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)
    zip_code = Column(String, nullable=False)
    is_billing = Column(Integer, nullable=False)

class Supplier(Base):
    """description: Represents a supplier that provides products."""

    __tablename__ = 'supplier'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

class SupplierProduct(Base):
    """description: Junction table linking suppliers to provided products."""

    __tablename__ = 'supplier_product'
    id = Column(Integer, primary_key=True)
    supplier_id = Column(Integer, ForeignKey('supplier.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('product.id'), nullable=False)

class Payment(Base):
    """description: Represents a payment made by a customer towards their balance."""

    __tablename__ = 'payment'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customer.id'), nullable=False)
    date = Column(DateTime, default=datetime.datetime.now)
    amount = Column(Float, nullable=False)

class Review(Base):
    """description: Represents a review by a customer for a product."""

    __tablename__ = 'review'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customer.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('product.id'), nullable=False)
    rating = Column(Integer, nullable=False)
    comment = Column(Text, nullable=True)

class OrderStatus(Base):
    """description: Represents the status of an order."""

    __tablename__ = 'order_status'
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('order.id'), nullable=False)
    status = Column(String, nullable=False)

class Promotion(Base):
    """description: Represents a promotion associated with products or orders."""

    __tablename__ = 'promotion'
    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    discount_percentage = Column(Float, nullable=False)

class ProductPromotion(Base):
    """description: Junction table linking promotions to the products affected by them."""

    __tablename__ = 'product_promotion'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('product.id'), nullable=False)
    promotion_id = Column(Integer, ForeignKey('promotion.id'), nullable=False)

# Database Initialization
DB_PATH = 'system/genai/temp/model.sqlite'
if not os.path.exists(os.path.dirname(DB_PATH)):
    os.makedirs(os.path.dirname(DB_PATH))

engine = create_engine(f'sqlite:///system/genai/temp/create_db_models.sqlite', echo=False)
Base.metadata.create_all(engine)

# Sample Data Insertion
Session = sessionmaker(bind=engine)
session = Session()

# Add sample customers
customers = [
    Customer(name='John Doe', credit_limit=1000.0),
    Customer(name='Jane Smith', credit_limit=2000.0)
]
session.add_all(customers)
session.commit()

# Add sample products
products = [
    Product(name='Widget A', unit_price=20.0),
    Product(name='Widget B', unit_price=30.0)
]
session.add_all(products)
session.commit()

# Add sample orders
orders = [
    Order(customer_id=1, amount_total=100.0, notes="First Order"),
    Order(customer_id=2, amount_total=200.0, notes="Second Order")
]
session.add_all(orders)
session.commit()

# Add items to orders
items = [
    Item(order_id=1, product_id=1, quantity=3, unit_price=20.0, amount=60.0),
    Item(order_id=1, product_id=2, quantity=2, unit_price=30.0, amount=40.0),
    Item(order_id=2, product_id=1, quantity=5, unit_price=20.0, amount=100.0)
]
session.add_all(items)
session.commit()

# Add sample data for other tables
addresses = [
    Address(customer_id=1, street="123 Elm St", city="Somewhere", state="NY", zip_code="10001", is_billing=1),
    Address(customer_id=2, street="456 Oak St", city="Anywhere", state="CA", zip_code="90001", is_billing=0),
]

suppliers = [
    Supplier(name='Supply Co'),
]

supplier_products = [
    SupplierProduct(supplier_id=1, product_id=1)
]

payments = [
    Payment(customer_id=1, amount=400.0),
]

reviews = [
    Review(customer_id=1, product_id=1, rating=5, comment="Great product!"),
]

order_statuses = [
    OrderStatus(order_id=1, status='Pending'),
]

promotions = [
    Promotion(description='Summer Sale', discount_percentage=10.0),
]

product_promotions = [
    ProductPromotion(product_id=1, promotion_id=1),
]

session.add_all(addresses + suppliers + supplier_products + payments + reviews + order_statuses + promotions + product_promotions)
session.commit()
session.close()
# from logic_bank.rule_type import Rule

def declare_logic():
    """
    Declare LogicBank rules enforcement for business constraints.
    """
    Rule.constraint(validate=Customer,
                    as_condition=lambda row: row.balance <= row.credit_limit,
                    error_msg="Customer's balance exceeds the credit limit.")
                    
    Rule.sum(derive=Customer.balance, 
             as_sum_of=Order.amount_total, 
             where=lambda row: row.date_shipped is None)
             
    Rule.sum(derive=Order.amount_total, 
             as_sum_of=Item.amount)
             
    Rule.formula(derive=Item.amount,
                 as_expression=lambda row: row.quantity * row.unit_price)
                 
    Rule.copy(derive=Item.unit_price, 
              from_parent=Product.unit_price)
