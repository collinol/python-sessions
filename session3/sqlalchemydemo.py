from sqlalchemy import select, func, and_, literal_column as col
from sqlalchemy.orm import join
from Tables import Employees, Department, Managers
from daobase import DaoBase
import pdb


class EmployeeDao(DaoBase):
    def __init__(self):
        super().__init__()
    
    def get_employees(self):
        query = select([Employees.name])
        print(self.query_all(query))

    def get_employees_under_manager(self, manager):
        query = select(
            [
                Employees.name
            ]
        ).select_from(join(
            Managers,
            Employees,
            Managers.manages == Employees.name
        )).where(Managers.name == manager)
        print(self.query_all(query))

    def get_total_employees(self):
        query = select([
            func.count(Employees)
        ])
        print(self.query_all(query))

    def get_count_of_employees(self):
        query = select([
            Employees.name,
            func.count(Employees.name)
        ]).group_by(Employees.name)
        print(self.query_all(query))

    def get_count_of_employees_named(self, name):
        query = select([
            Employees.name,
            func.count(Employees.name)
        ]).group_by(Employees.name).where(Employees.name == name)
        print(self.query_all(query))

    def get_count_of_employee_names_in_dept(self, name, dept):

        query = select([
            Employees.name,
            func.count(Employees.name)
        ]).group_by(Employees.name).where(
            and_(
                Employees.name == name,
                Employees.department_id == dept
            )
        )
        pdb.set_trace()
        print(self.query_all(query))

if __name__ == '__main__':
    employees = EmployeeDao()
    employees.get_count_of_employee_names_in_dept("Alice", 1)
