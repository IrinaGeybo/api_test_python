from data.urls import Urls
import allure
import requests
from utils.validate import Validate
from utils.assertions import Assertions
from http import HTTPStatus
from utils.schemas.get_booking.response_schema import GetBookingResponseSchema


class Test:
    urls=Urls()
    validate=Validate()
    assertion=Assertions()

    @allure.title("Get list of booking")
    @allure.feature("Booking Management")
    def test_get_booking(self, get_booking_id):
        with allure.step("Send a GET request to get a server response"):
            response=requests.get(
                url=f"{self.urls.URL}/{get_booking_id}"
            )
        with allure.step("Verify that the server response status code is 200"):
            self.assertion.assert_status_code(response, HTTPStatus.OK)
        with allure.step("Verify that the response matches the expected JSON schema"):
            self.validate.validate(response, GetBookingResponseSchema)