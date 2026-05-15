from data.urls import Urls
import pytest
import requests
from utils.validate import Validate
from utils.schemas.get_booking_ids_schemas.response_schema import GetBookingIdsSchema
from utils.assertions import Assertions
from http import HTTPStatus
import allure
# https://restful-booker.herokuapp.com/apidoc/index.html#api-Booking-GetBookings


class Test: 

    urls= Urls
    validate=Validate
    assertion=Assertions

    @allure.feature("Gets booking id")
    @allure.story("Story gets booking id")
    def test_get_booking_ids(self):
        response=requests.get(self.urls.URL)
        print(response.json())
        self.validate.validate_list(self, response, GetBookingIdsSchema)
        self.assertion.assert_status_code(self, response, HTTPStatus.OK)
