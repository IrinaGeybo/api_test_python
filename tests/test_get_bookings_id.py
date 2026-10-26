from data.urls import Urls
import requests
from utils.validate import Validate
from utils.schemas.get_booking_ids_schemas.response_schema import GetBookingIdsSchema
from utils.assertions import Assertions
from http import HTTPStatus
import allure


class Test: 

    urls= Urls()
    validate=Validate()
    assertion=Assertions()

    @allure.feature("Booking Management")
    @allure.story("Get All Booking IDs")
    def test_get_booking_ids(self):
        with allure.step("Get server response"):
            response = requests.get(self.urls.URL)
        self.assertion.assert_status_code(response, HTTPStatus.OK)
        self.validate.validate_list(response, GetBookingIdsSchema)

