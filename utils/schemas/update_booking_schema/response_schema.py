from pydantic import BaseModel


class UpdateBookingDatesSchema(BaseModel):
    checkin: str
    checkout: str

class UpdateBookingSchema(BaseModel):
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: UpdateBookingDatesSchema
    additionalneeds: str

