import requests
import pytest
from data.generator.booking_generator import BookingGenerator
from utils.functions import generate_checkin_checkout_dates



generator = BookingGenerator()

def test():
    checkin, checkout = generate_checkin_checkout_dates()
    info = next(generator.generate_booking(checkin=checkin, checkout=checkout))
    print(info.first_name)




