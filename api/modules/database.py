from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Integer, String, DateTime, ForeignKey, Boolean, Numeric, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql import func
from datetime import datetime
import string,random
import logging
import os
from dotenv import load_dotenv

load_dotenv()

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

logging.basicConfig(level=logging.INFO, format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s', datefmt='%Y-%m-%d:%H:%M:%S')

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    except:
        db.close()


class BaseMixin(object):
    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}



class Product(BaseMixin,Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False,unique=True)
    uom = Column(String,nullable=False)
    category_name = Column(String,nullable=False)
    is_producible = Column(Boolean,nullable=False)
    is_purchasable = Column(Boolean,nullable=False)
    type = Column(String,nullable=False,default='product')
    additional_info = Column(String,nullable=False)
    purchase_uom = Column(String,nullable=True,default=None)
    purchase_uom_conversion_rate = Column(Numeric,default=None,nullable=True)
    batch_tracked = Column(Boolean,nullable=False,default=False)
    created = Column(DateTime(timezone=True),nullable=False, default=func.now())
    updated_at = Column(DateTime(timezone=True),default=func.now())


class ProductVariant(BaseMixin,Base):
    __tablename__ = 'product_variants'


    id = Column(Integer, primary_key=True)
    sku = Column(String,nullable=False,unique=True)
    sales_price = Column(Numeric,nullable=False)
    product_id = Column(Integer,ForeignKey(Product.id))
    type = Column(String,nullable=False,default='product')
    created_at = Column(DateTime(timezone=True),nullable=False, default=func.now())
    updated_at = Column(DateTime(timezone=True),default=func.now())
    product_id = Column(Integer, ForeignKey=Product.id)


class ConfigAttributes(BaseMixin,Base):
    __tablename__ = 'config_attributes'

    id = Column(Integer,primary_key=True)
    config_name = Column(String,nullable=False)
    config_value = Column(String,nullable=False)
    product_id = Column(Integer,ForeignKey(Product.id))