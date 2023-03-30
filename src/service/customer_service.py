import pandas as pd

from src.service.customer_repository_service import CustomerRepositoryService
from fastapi import HTTPException


class CustomerService:
    def __init__(self):
        self.__customer_repository_service = CustomerRepositoryService()

    def register_customer(self, name: str, surname: str, age: int, mail_address: str) -> int:
        if name is None or len(name) == 0:
            raise HTTPException(status_code=400, detail='this field is not valid or must be filled')
        if surname is None or len(surname) == 0:
            raise HTTPException(status_code=400, detail='this field is not valid or must be filled')
        if age is None or age < 12:
            raise HTTPException(status_code=400, detail='this field is not valid or must be superior to 12')
        if '@' not in mail_address:
            raise HTTPException(status_code=400, detail='this mail_address is not valid or must be filled')

        name = name.lower()
        surname = surname.lower()
        mail_domain = mail_address.split('@')[1]
        c = pd.DataFrame({'name': [name],
                          'surname': [surname],
                          'age': [age],
                          'mail_domain': [mail_domain],
                          'mail_address': [mail_address]})
        self.__customer_repository_service.register_customer(c)
        return self.__customer_repository_service.fetch_number_of_customers()
