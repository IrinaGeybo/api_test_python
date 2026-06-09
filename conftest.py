import allure
import pytest
import requests
import os
from dotenv import load_dotenv
from data.urls import Urls
import random
from utils.functions import generate_checkin_checkout_dates
from data.generator.booking_generator import BookingGenerator
from modules.create_booking_module import CreateBookingModule
load_dotenv()
from faker import Faker



urls=Urls()
generator=BookingGenerator()
module = CreateBookingModule()
faker=Faker()

@pytest.fixture
def get_token():
    admin = os.getenv("USERNAME_ADMIN")
    password = os.getenv("PASSWORD_ADMIN")
    data={
        "username": admin,
        "password": password
    }
    response = requests.post(urls.URL_AUTH, json=data)
    token = response.json()["token"]
    return token


@pytest.fixture
def get_headers():
    admin = os.getenv("USERNAME_ADMIN")
    password = os.getenv("PASSWORD_ADMIN")
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
def generate_booking_data():
    checkin, checkout = generate_checkin_checkout_dates()
    info = next(generator.generate_booking(checkin=checkin, checkout=checkout))
    data = module.create_data(info=info)
    return data


@pytest.fixture
def get_response_create_booking(generate_booking_data):
    data=generate_booking_data
    response = requests.post(urls.URL,
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json"
        },
        json=data
    )
    return response


@pytest.fixture
def get_booking_id_after_creating_booking(generate_booking_data):
    with allure.step("create the request body"):
        data=generate_booking_data
    with allure.step("Send a PUT request to update the reservation details"):
        response = requests.post(
            urls.URL,
            headers={
                "Content-Type": "application/json",
                "Accept": "application/json"
            },
            json=data
        )
    with allure.step(f"Extract and save booking_id"):
        booking_id = response.json()["bookingid"]
    return booking_id