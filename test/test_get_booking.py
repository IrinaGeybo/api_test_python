from data.urls import Urls
import allure
import pytest
import requests
from utils.validate import Validate
from utils.assertions import Assertions
from http import HTTPStatus
from utils.schemas.get_booking.response_schema import GetBookingResponseSchema



urls=Urls()
validate=Validate()
assertion=Assertions()

@allure.feature("Get booking data")
def test_get_booking(get_booking_id):
    response=requests.get(url=f"{urls.URL}/{get_booking_id}")
    print(f"достаем данные по id - {get_booking_id}")
    print(f"Достали букинг по id - {response.json()}")
    validate.validate(response, GetBookingResponseSchema)
    assertion.assert_status_code(response, HTTPStatus.OK)
