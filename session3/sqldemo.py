#api = api/employee/{id}/update -> EmployeeDao.update()
from dao import DaoBase
from sqlalchemy import select, func, and_, literal_column as col
from sqlalchemy.orm import join
from Tables import Employees, Department, Managers
from daobase import DaoBase

class EmployeeDao(DaoBase):
    def __init__(self):
        super().__init__()

    def get_employees(self):
        query = select(
            [
                Employees.name,
            ]
        )
        print(self.query_all(query))


    def get_count_of_employee_names_in_dept(self, name, dept):
        query = select(
            [
                Employees.name,
                func.count(Employees.name)
            ]
        ).group_by(Employees.name).where(
            and_(
                Employees.name == name,
                Employees.department_id == dept
            )
        )
        print(self.query_all(query))

    def get_count_of_employees_named(self, name):
        import pdb
        pdb.set_trace()
        query = select([
            func.distinct(Employees.name),
            func.count(Employees.name)
        ]).group_by(Employees.name).where(Employees.name == name)
        print(self.query_all(query))



if __name__ == '__main__':
    employees = EmployeeDao()
    employees.get_count_of_employees_named("John")