import requests
from data.urls import Urls
import pytest
import requests
from utils.validate import Validate
from utils.assertions import Assertions
from http import HTTPStatus
from data.generator.booking_generator import BookingGenerator
from utils.schemas.create_booking_data.request_schema import BookingDataRequestSchema
import json
from modules.base_module import BaseModule
from modules.create_booking_data_module import CreateBookingDataModule
from modules.create_booking_module import CreateBookingModule
from dotenv import load_dotenv
from utils.functions import generate_checkin_checkout_dates, generate_negative_checkin_dates
from utils.schemas.create_booking_data.response_schema import BookingModel
import allure


load_dotenv()



class Test:

    urls=Urls()
    validate=Validate()
    assertion=Assertions()
    generator=BookingGenerator()
    module = CreateBookingModule()



    @allure.title("Create booking data. Do not use fixture. We check that the response scheme is correct.")
    @allure.feature('Create booking data. Do not use fixture')
    def test_create_booking2(self):
        checkin, checkout = generate_checkin_checkout_dates()
        info=next(self.generator.generate_booking(checkin=checkin, checkout=checkout))
        data = self.module.create_data(info=info)
        response=requests.post("https://restful-booker.herokuapp.com/booking",
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json"
        },
        json=data
        )
        bookingid=response.json()["bookingid"]
        print(f"Распечатываем ответ response.json() - {response.json()}")
        print(f"Распечатываем bookingid - {bookingid}")
        with allure.step("Проверяем схему ответа"):
            self.validate.validate(response, BookingModel)



    @allure.title("Creating a booking data. In this test we use fixture.We check that the response scheme is correct.")
    @allure.feature('Create booking')
    def test_create_booking3(self, generate_correct_booking_data):
        data=generate_correct_booking_data
        print(f"Распечатываем data - {data}")
        response = requests.post(self.urls.URL,
            headers={
                "Content-Type": "application/json",
                "Accept": "application/json"
                },
                json=data
            )
        bookingid = response.json()["bookingid"]
        print(f"Распечатываем ответ response.json() - {response.json()}")
        print(f"Распечатываем bookingid - {bookingid}")
        with allure.step("Проверяем схему ответа"):
            self.validate.validate(response, BookingModel)



    @allure.title("Creating a booking data. In this test we use fixture. Get_response_create_booking")
    @allure.feature('Create booking')
    def test_create_booking4(self, get_response_create_booking):
        response = get_response_create_booking
        with allure.step("Проверяем схему ответа"):
            self.validate.validate(response, BookingModel)



    # def test_create_booking_neg(self):
    #     checkin, checkout = generate_negative_checkin_dates()
    #     info = next(self.generator.generate_booking(checkin=checkin, checkout=checkout))
    #     data = self.module1.create_data(info=info)
    #     print(f"info созданное с помощь. генератора - {info}")
    #     print(type(info))
    #     print(f"Распечатываем data - {data}")
    #
    #     print(f"Checkin, Checkout - {checkin}, {checkout}")
    #
    #     response = requests.post("https://restful-booker.herokuapp.com/booking",
    #                              headers={
    #                                  "Content-Type": "application/json",
    #                                  "Accept": "application/json"
    #                              },
    #                              json=data
    #                              )
    #     print(f"Распечатываем ответ response.json() - {response.json()}")
    #     print(f"Распечатываем bookingid - {response.json()["bookingid"]}")
    #     self.validate.validate(response, BookingModel)