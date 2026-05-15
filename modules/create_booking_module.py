from modules.base_module import BaseModule
from data.dataclasses.booking_data import BookingData, BookingDates



class CreateBookingModule(BaseModule):

    def create_data(self, info: BookingData):
        data = {
            "firstname": info.first_name,
            "lastname": info.last_name,
            "totalprice": info.total_price,
            "depositpaid": info.deposit_paid,
            "bookingdates": {
                "checkin": info.booking_dates.checkin,
                "checkout": info.booking_dates.checkout
            },
            "additionalneeds": info.additional_needs
        }
        return data