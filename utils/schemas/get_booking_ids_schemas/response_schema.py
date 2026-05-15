from pydantic import BaseModel

class GetBookingIdsSchema(BaseModel):
    bookingid: int