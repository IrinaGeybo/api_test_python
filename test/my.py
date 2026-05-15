from dataclasses import dataclass
from faker import Faker
from pydantic import BaseModel



fake = Faker()


@dataclass
class BookingData1:
    name: str = None
    last_name: str = None
    country: str = None


class BaseGenerator:
    pass

    def generate_booking(
            self, first_name=None,
            last_name=None,
            total_price=None,
            deposit_paid=True,
            booking_dates=None,
            checkin=None,
            checkout=None,
            additional_needs=None
    ):
        yield BookingData(
            first_name=self.get_first_name(first_name),
            last_name=self.get_last_name(last_name),
            total_price=self.get_random_number(total_price),
            deposit_paid=deposit_paid,
            booking_dates=self.generate_booking_dates(booking_dates, checkin, checkout),
            additional_needs=self.get_random_word(additional_needs)

        )



class BookingDataGenerator2(BaseGenerator):
    fake = Faker()
    def generate_booking_data(
            self, name=None,
            last_name=None,
            country=None):
            yield BookingData1(
            name=self.fake.name(),
            last_name=self.fake.last_name(),
            country=self.fake.country()
        )

generator = BookingDataGenerator2()

# создаем экземпляр класса с помошью генератора
booking_data = next(generator.generate_booking_data(name="Ирина"))
print(f"Тип booking data получаемое с помощью генератора - {type(booking_data)}")

# реобразуем класс в словарь
dict_booking_data = { key: value for key, value in booking_data.__dict__.items() }
print(dict_booking_data)


# создаем схему на основе которой мы хотим создать тело запроса, чтобы создать схему надо  сказать BaseModel from pydantic


class BookingDataschema(BaseModel):
    name: str = None
    last_name: str = None
    country: str = None



booking_data = BookingDataschema(**dict_booking_data).model_dump_json()
print(booking_data)
print(type(booking_data))



