# Path: app/strateger/routes.py

from fastapi import APIRouter, Depends, HTTPException, Request, Query
from sqlalchemy.orm import Session

from app.siteground.database import get_db_ordenes
from app.strateger.crud import get_orders
from app.utils.ip_check import is_ip_allowed

from loguru import logger
from typing import List

router = APIRouter()
