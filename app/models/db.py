from dataclasses import dataclass, asdict
from datetime import date, datetime, timedelta
from pymysql import IntegrityError
from sqlalchemy import Boolean, CHAR, Column, Date, ForeignKey, JSON, String, Text, BigInteger, DateTime, Integer, Enum, SmallInteger
from sqlalchemy import func
from sqlalchemy.dialects.mysql import INTEGER, TIMESTAMP
from sqlalchemy.orm import DeclarativeBase, Mapped
from sqlalchemy.orm import mapped_column, relationship
from app.utils.date import jakarta_now

import enum

class Base(DeclarativeBase):
    created_at: Mapped[datetime] = mapped_column(DateTime, default=jakarta_now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=jakarta_now, onupdate=jakarta_now)

@dataclass
class User(Base):
    __tablename__ = "master_users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

@dataclass
class Doctor(Base):
    __tablename__="master_doctor"

@dataclass
class Patient(Base):
    __tablename__="master_patients"

@dataclass
class MasterEvent(Base):
    __tablename__="master_events"


