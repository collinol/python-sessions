from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func, select
from sqlalchemy.orm import relationship, backref

Base = declarative_base()

class Department(Base):
    __tablename__ = "department"
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Employees(Base):
    __tablename__ = "employee"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    hired_on = Column(DateTime, default=func.now())
    created_at = Column
    department_id = Column(Integer, ForeignKey("department.id"))
    department = relationship(
        Department,
        backref=backref(
            'employees',
            cascade='delete,all'
        )
    )