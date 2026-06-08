from pydantic import BaseModel

class UpdateBookingDatesRequestSchema(BaseModel):
    checkin: str
    checkout: str


class UpdateBookingDataRequestSchema(BaseModel):
    first_name: str
    last_name: str
    total_price: int
    deposit_paid: bool
    booking_dates: UpdateBookingDatesRequestSchema
    additional_needs: str = None
