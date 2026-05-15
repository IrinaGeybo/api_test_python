from pydantic import BaseModel
from typing import List



class BookingDates(BaseModel):
    checkin: str
    checkout: str

class Booking(BaseModel):
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: BookingDates
    additionalneeds: str

class BookingModel(BaseModel):
    bookingid: int
    booking: Booking
