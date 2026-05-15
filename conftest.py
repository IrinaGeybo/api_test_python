import pytest
import requests
import os
from dotenv import load_dotenv
from data.urls import Urls
import random
from utils.functions import generate_checkin_checkout_dates
from data.generator.booking_generator import BookingGenerator
from modules.create_booking_module import CreateBookingModule
from data.generator.base_generator import BaseGenerator
# после импортирования dotenv нашу функцию необходимо вызвать
load_dotenv()


admin = os.environ.get("USERNAME_ADMIN")
password = os.environ.get("PASSWORD_ADMIN")
urls=Urls()
generator=BookingGenerator()
module = CreateBookingModule()

@pytest.fixture
def get_token():
    data={
        "username": admin,
        "password": password
    }
    response = requests.post(urls.URL_AUTH, json=data)
    token = response.json()["token"]
    return token


@pytest.fixture
def get_headers():
    data={
        "username": admin,
        "password": password
    }
    response = requests.post(urls.URL_AUTH, json=data)
    token = response.json()["token"]
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    return headers



@pytest.fixture
def get_booking_id():
    response = requests.get(
        url=f'{urls.URL}'
    )
    random_book_id = random.choice(response.json())["bookingid"]
    return random_book_id

@pytest.fixture
def generate_correct_booking_data():
    checkin, checkout = generate_checkin_checkout_dates()
    info = next(generator.generate_booking(checkin=checkin, checkout=checkout))
    data = module.create_data(info=info)
    return data


@pytest.fixture
def get_response_create_booking(generate_correct_booking_data):
        data=generate_correct_booking_data
        print(f"Распечатываем data - {data}")
        response = requests.post(urls.URL,
            headers={
                "Content-Type": "application/json",
                "Accept": "application/json"
                },
                json=data
            )
        return response