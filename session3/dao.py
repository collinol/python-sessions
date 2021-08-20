
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Tables import Employees, Department, Managers
Base = declarative_base()

class DaoBase:
    def __init__(self):
        self.engine = create_engine('sqlite:///orm_in_detail.sqlite')
        session = sessionmaker()
        session.configure(bind=self.engine)
        Base.metadata.create_all(self.engine)
        self.session = session()
        # ^ repo/team specific (redshift) configuration

    def populate_data(self):
        d = Department(name="IT")
        d2 = Department(name="Product")
        emp1 = Employees(name="John", department=d)
        emp2 = Employees(name="Mike", department=d)
        emp3 = Employees(name="Alice", department=d2)
        emp4 = Employees(name="Bob", department=d2)
        emp5 = Employees(name="John", department=d2)
        self.session.add(d)
        self.session.commit()
        self.session.add(emp1)
        self.session.add(emp2)
        self.session.add(emp3)
        self.session.add(emp4)
        self.session.add(emp5)
        self.session.commit()

    def query_all(self, query):
        return self.session.execute(query).fetchall()

    def query_one(self, query):
        return self.session.execute(query).fetchone()