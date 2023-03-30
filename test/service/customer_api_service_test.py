import unittest
from fastapi import FastAPI
from src.application.customer_api import CustomerAPI
from src.service.customer_service import CustomerService
from starlette.testclient import TestClient


def build_application() -> FastAPI:
    customer_service = CustomerService()
    return CustomerAPI(customer_service)


client = TestClient(app=build_application())


class TextProcessServiceTest(unittest.TestCase):

    def test_customer_register(self):
        add_customer_andre = client.get(
            url="/customer-service/api/v1/register-customer",
            params={
                "name": "andre",
                "surname": "ehouman",
                "age": 29,
                "mail_address": "andre.ehouman@yahoo.com"
            }
        )
        assert add_customer_andre.status_code == 200
        assert add_customer_andre.json()["number_of_customers"] == 2

        add_customer_massara = client.get(
            url="/customer-service/api/v1/register-customer",
            params={
                "name": "massara",
                "surname": "nemlin",
                "age": 29,
                "mail_address": "massara.nemlin@yahoo.com"
            }
        )
        assert add_customer_massara.status_code == 200
        assert add_customer_massara.json()["number_of_customers"] == 3

        add_customer_with_email_already_existing = client.get(
            url="/customer-service/api/v1/register-customer",
            params={
                "name": "toprak",
                "surname": "ucar",
                "age": 29,
                "mail_address": "massara.nemlin@yahoo.com"
            }
        )
        assert add_customer_with_email_already_existing.status_code == 400
        assert add_customer_with_email_already_existing.json()["detail"] == "this mail address already exists"

        add_customer_with_age_less_than_12 = client.get(
            url="/customer-service/api/v1/register-customer",
            params={
                "name": "myriam",
                "surname": "ehouman",
                "age": 10,
                "mail_address": "myriam.ehouman@yahoo.com"
            }
        )
        assert add_customer_with_age_less_than_12.status_code == 400
        assert add_customer_with_age_less_than_12.json()["detail"] == "this field is not valid or must be superior to 12"
