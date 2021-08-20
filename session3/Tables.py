from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func, select
from sqlalchemy.orm import relationship, backref, join
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Department(Base):
    __tablename__ = 'department'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Employees(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    # Use default=func.now() to set the default hiring time
    # of an Employee to be the current time when an
    # Employee record was created
    hired_on = Column(DateTime, default=func.now())
    department_id = Column(Integer, ForeignKey('department.id'))
    # Use cascade='delete,all' to propagate the deletion of a Department onto its Employees
    department = relationship(
        Department,
        backref=backref('employees',
                        uselist=True,
                        cascade='delete,all'))


class Managers(Base):
    __tablename__ = "managers"
    id = Column(Integer, primary_key=True)
    name = Column(String, ForeignKey(Employees.id))
    manages = Column(String, ForeignKey(Employees.id))
