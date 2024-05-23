# Path: app/siteground/base.py
# Description: Base class for SQLAlchemy models

from sqlalchemy.ext.declarative import declarative_base

# Base for alarms database
BaseAlarmas = declarative_base()

# Base for orders database
BaseOrdenes = declarative_base()
