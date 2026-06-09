from data.urls import Urls
import requests
from utils.validate import Validate
from utils.assertions import Assertions
from http import HTTPStatus
from data.generator.booking_generator import BookingGenerator
from modules.create_booking_module import CreateBookingModule
from dotenv import load_dotenv
from utils.schemas.update_booking_schema.response_schema import UpdateBookingSchema
import allure
from faker import Faker

load_dotenv()


class TestUpdateBooking:

    urls=Urls()
    validate=Validate()
    assertion=Assertions()
    generator=BookingGenerator()
    module = CreateBookingModule()
    faker = Faker()

    @allure.feature("Booking Management")
    @allure.story("Update Booking")
    def test_update_booking(self, get_booking_id_after_creating_booking, get_token, generate_booking_data):
        booking_id=get_booking_id_after_creating_booking
        data = generate_booking_data
        with allure.step("Sending a PUT request to update a reservation"):
            response = requests.put(
                url=f"{self.urls.URL}/{booking_id}",
                json=data,
                cookies={"token": get_token},
                headers={
                    "Content-Type": "application/json",
                    "Accept": "application/json"
                }
            )
        self.assertion.assert_status_code(response, HTTPStatus.OK)
        self.validate.validate(response, UpdateBookingSchema)
        with allure.step("Compare the sent payload and the server's entire response."):
            assert response.json() == data