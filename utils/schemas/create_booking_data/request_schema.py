from pydantic import BaseModel
from typing import List


# class BookingDatesRequestSchema(BaseModel):
#     checkin: str
#     checkout: str


# class BookingDataRequestSchema(BaseModel):
#     first_name: str 
#     last_name: str 
#     total_price: int 
#     deposit_paid: bool 
#     booking_dates: List[BookingDatesRequestSchema]
#     additional_needs: str = None



class BookingDatesRequestSchema(BaseModel):
    checkin: str
    checkout: str


class BookingDataRequestSchema(BaseModel):
    first_name: str 
    last_name: str 
    total_price: int 
    deposit_paid: bool 
    booking_dates: BookingDatesRequestSchema
    additional_needs: str = None
