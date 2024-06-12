# Path: app/siteground/base.py
# Description: Base class for SQLAlchemy models

from sqlalchemy.ext.declarative import declarative_base

# Base for alarms database
BaseAlarmas = declarative_base()

# Base for strategies database
BaseEstrategias = declarative_base()
