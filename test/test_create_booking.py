from data.urls import Urls
import requests
from utils.validate import Validate
from utils.assertions import Assertions
from data.generator.booking_generator import BookingGenerator
from modules.create_booking_module import CreateBookingModule
from dotenv import load_dotenv
from utils.functions import generate_checkin_checkout_dates, generate_negative_checkin_dates
from utils.schemas.create_booking_data.response_schema import BookingModel
import allure
from http import HTTPStatus
#from utils.logger import log
#from loguru import logger

load_dotenv()


class Test:

    urls=Urls()
    validate=Validate()
    assertion=Assertions()
    generator=BookingGenerator()
    module = CreateBookingModule()


    @allure.title("Create booking data. Do not use fixture.")
    @allure.feature('Booking Management')
    @allure.story('Create booking')
    def test_create_booking2(self):
        with allure.step("Prepare dynamic booking data and dates"):
            checkin, checkout = generate_checkin_checkout_dates()
            info=next(self.generator.generate_booking(checkin=checkin, checkout=checkout))
            data = self.module.create_data(info=info)
        with allure.step("Get server response"):
            response=requests.post(
                url=f"{self.urls.URL}",
                headers={
                    "Content-Type": "application/json",
                    "Accept": "application/json"
                },
                json=data
            )
        self.assertion.assert_status_code(response, HTTPStatus.OK)
        self.validate.validate(response, BookingModel)



    @allure.title("Creating a booking data. In this test we use fixture.We check that the response schema is correct.")
    @allure.feature('Booking Management')
    @allure.story('Create booking')
    def test_create_booking3(self, generate_booking_data):
        data=generate_booking_data
        response = requests.post(
            url=self.urls.URL,
            headers={
                "Content-Type": "application/json",
                "Accept": "application/json"
                },
            json=data
        )
        self.assertion.assert_status_code(response, HTTPStatus.OK)
        self.validate.validate(response, BookingModel)



    @allure.title("Creating a booking data. In this test we use fixture. Get_response_create_booking")
    @allure.feature('Booking Management')
    @allure.story('Create booking')
    def test_create_booking4(self, get_response_create_booking):
        response = get_response_create_booking
        self.assertion.assert_status_code(response, HTTPStatus.OK)
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