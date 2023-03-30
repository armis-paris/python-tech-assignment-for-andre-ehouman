import pandas as pd

from fastapi import HTTPException


class CustomerRepositoryService:

    def __init__(self):
        self.__customer_list = pd.DataFrame({'name': ['kurt'],
                                             'surname': ['cobain'],
                                             'age': [27],
                                             'mail_domain': ['gmail.com'],
                                             'mail_address': ['kurt.cobain@gmail.com']})

    def register_customer(self, customer: pd.DataFrame):
        if customer['mail_address'][0] in list(self.__customer_list['mail_address']):
            raise HTTPException(status_code=400, detail='this mail address already exists')
        self.__customer_list = pd.concat([self.__customer_list, customer])

    def fetch_number_of_customers(self) -> int:
        return len(self.__customer_list)
