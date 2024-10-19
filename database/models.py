# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  October 19, 2024 23:15:11
# Database: sqlite:////tmp/tmp.WzoKg68Wjz/IamAduck/database/db.sqlite
# Dialect:  sqlite
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX
from flask_login import UserMixin
import safrs, flask_sqlalchemy
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *



class Customer(SAFRSBaseX, Base):
    """
    description: Represents a customer with personal and credit information.
    """
    __tablename__ = 'customer'
    _s_collection_name = 'Customer'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    credit_limit = Column(Float, nullable=False)
    balance = Column(Float, nullable=False)

    # parent relationships (access parent)

    # child relationships (access children)
    AddresList : Mapped[List["Addres"]] = relationship(back_populates="customer")
    OrderList : Mapped[List["Order"]] = relationship(back_populates="customer")
    PaymentList : Mapped[List["Payment"]] = relationship(back_populates="customer")
    ReviewList : Mapped[List["Review"]] = relationship(back_populates="customer")



class Product(SAFRSBaseX, Base):
    """
    description: Represents a product available for purchase.
    """
    __tablename__ = 'product'
    _s_collection_name = 'Product'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    unit_price = Column(Float, nullable=False)

    # parent relationships (access parent)

    # child relationships (access children)
    ProductPromotionList : Mapped[List["ProductPromotion"]] = relationship(back_populates="product")
    ReviewList : Mapped[List["Review"]] = relationship(back_populates="product")
    SupplierProductList : Mapped[List["SupplierProduct"]] = relationship(back_populates="product")
    ItemList : Mapped[List["Item"]] = relationship(back_populates="product")



class Promotion(SAFRSBaseX, Base):
    """
    description: Represents a promotion associated with products or orders.
    """
    __tablename__ = 'promotion'
    _s_collection_name = 'Promotion'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    discount_percentage = Column(Float, nullable=False)

    # parent relationships (access parent)

    # child relationships (access children)
    ProductPromotionList : Mapped[List["ProductPromotion"]] = relationship(back_populates="promotion")



class Supplier(SAFRSBaseX, Base):
    """
    description: Represents a supplier that provides products.
    """
    __tablename__ = 'supplier'
    _s_collection_name = 'Supplier'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # parent relationships (access parent)

    # child relationships (access children)
    SupplierProductList : Mapped[List["SupplierProduct"]] = relationship(back_populates="supplier")



class Addres(SAFRSBaseX, Base):
    """
    description: Represents an address associated with a customer, can be billing or shipping.
    """
    __tablename__ = 'address'
    _s_collection_name = 'Addres'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    customer_id = Column(ForeignKey('customer.id'), nullable=False)
    street = Column(String, nullable=False)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)
    zip_code = Column(String, nullable=False)
    is_billing = Column(Integer, nullable=False)

    # parent relationships (access parent)
    customer : Mapped["Customer"] = relationship(back_populates=("AddresList"))

    # child relationships (access children)



class Order(SAFRSBaseX, Base):
    """
    description: Represents an order created by a customer, containing multiple items.
    """
    __tablename__ = 'order'
    _s_collection_name = 'Order'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    customer_id = Column(ForeignKey('customer.id'), nullable=False)
    date_created = Column(DateTime)
    date_shipped = Column(DateTime)
    amount_total = Column(Float, nullable=False)
    notes = Column(Text)

    # parent relationships (access parent)
    customer : Mapped["Customer"] = relationship(back_populates=("OrderList"))

    # child relationships (access children)
    ItemList : Mapped[List["Item"]] = relationship(back_populates="order")
    OrderStatuList : Mapped[List["OrderStatu"]] = relationship(back_populates="order")



class Payment(SAFRSBaseX, Base):
    """
    description: Represents a payment made by a customer towards their balance.
    """
    __tablename__ = 'payment'
    _s_collection_name = 'Payment'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    customer_id = Column(ForeignKey('customer.id'), nullable=False)
    date = Column(DateTime)
    amount = Column(Float, nullable=False)

    # parent relationships (access parent)
    customer : Mapped["Customer"] = relationship(back_populates=("PaymentList"))

    # child relationships (access children)



class ProductPromotion(SAFRSBaseX, Base):
    """
    description: Junction table linking promotions to the products affected by them.
    """
    __tablename__ = 'product_promotion'
    _s_collection_name = 'ProductPromotion'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    product_id = Column(ForeignKey('product.id'), nullable=False)
    promotion_id = Column(ForeignKey('promotion.id'), nullable=False)

    # parent relationships (access parent)
    product : Mapped["Product"] = relationship(back_populates=("ProductPromotionList"))
    promotion : Mapped["Promotion"] = relationship(back_populates=("ProductPromotionList"))

    # child relationships (access children)



class Review(SAFRSBaseX, Base):
    """
    description: Represents a review by a customer for a product.
    """
    __tablename__ = 'review'
    _s_collection_name = 'Review'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    customer_id = Column(ForeignKey('customer.id'), nullable=False)
    product_id = Column(ForeignKey('product.id'), nullable=False)
    rating = Column(Integer, nullable=False)
    comment = Column(Text)

    # parent relationships (access parent)
    customer : Mapped["Customer"] = relationship(back_populates=("ReviewList"))
    product : Mapped["Product"] = relationship(back_populates=("ReviewList"))

    # child relationships (access children)



class SupplierProduct(SAFRSBaseX, Base):
    """
    description: Junction table linking suppliers to provided products.
    """
    __tablename__ = 'supplier_product'
    _s_collection_name = 'SupplierProduct'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    supplier_id = Column(ForeignKey('supplier.id'), nullable=False)
    product_id = Column(ForeignKey('product.id'), nullable=False)

    # parent relationships (access parent)
    product : Mapped["Product"] = relationship(back_populates=("SupplierProductList"))
    supplier : Mapped["Supplier"] = relationship(back_populates=("SupplierProductList"))

    # child relationships (access children)



class Item(SAFRSBaseX, Base):
    """
    description: Represents an item in an order, linked to a product.
    """
    __tablename__ = 'item'
    _s_collection_name = 'Item'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    order_id = Column(ForeignKey('order.id'), nullable=False)
    product_id = Column(ForeignKey('product.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    unit_price = Column(Float, nullable=False)
    amount = Column(Float, nullable=False)

    # parent relationships (access parent)
    order : Mapped["Order"] = relationship(back_populates=("ItemList"))
    product : Mapped["Product"] = relationship(back_populates=("ItemList"))

    # child relationships (access children)



class OrderStatu(SAFRSBaseX, Base):
    """
    description: Represents the status of an order.
    """
    __tablename__ = 'order_status'
    _s_collection_name = 'OrderStatu'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    order_id = Column(ForeignKey('order.id'), nullable=False)
    status = Column(String, nullable=False)

    # parent relationships (access parent)
    order : Mapped["Order"] = relationship(back_populates=("OrderStatuList"))

    # child relationships (access children)
