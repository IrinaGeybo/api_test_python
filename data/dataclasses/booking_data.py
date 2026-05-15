from dataclasses import dataclass


@dataclass
class BookingDates:
    checkin: str = None
    checkout: str = None

@dataclass
class BookingData:
    first_name: str = None
    last_name: str = None
    total_price: int = None
    deposit_paid: bool = None
    booking_dates: BookingDates = None
    additional_needs: str = None