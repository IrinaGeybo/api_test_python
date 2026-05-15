# from datetime import datetime, timedelta
# import random
# import requests
# import pytest
# from http import HTTPStatus
# # from data.generator.booking_generator import BookingGenerator
# import json
# # from modules.base_module import BaseModule
# # from modules.create_booking_data_module import CreateBookingDataModule
# # from modules.create_booking_module import CreateBookingModule
# from dotenv import load_dotenv
# from utils.functions import generate_checkin_checkout_dates
from pydantic import BaseModel, field_validator


# today = datetime.now()
# print(f"Today - {today}") # 2026-04-07 10:39:32.909150
# random_days = random.randint(-60, 60)
# print(f"random_day - {random_days}")


# checkin  = today + timedelta(days=random_days)
# print(f"Checkin - {checkin}")


# # calculate time 5 days from now
# future = today + timedelta(days=5)
# print(f"Future date - {future}")

# future = future.strftime('%Y-%d-%m')
# print(f"Отформатированное время future - {future}")
# future_hours = today + timedelta(hours=6)
# print(future_hours)





# # def generate_checkin_checkout_dates(checkin=None, checkout=None):
# #     random_days=random.randit(-60, 60)
# #     today=datetime.now()
    

# #     if checkin is None:
# #         checkin = today + timedelta(days=random_days)
# #         checkin = checkin.strftime('%Y-%m-%d')

# #     if checkout is None:
# #         checkout_date = datetime.strptime(checkin, "%Y-%m-%d") + timedelta(days=random.randit(1, 60))
# #         checkout = checkout_date.strftime('%Y-%m-%d')

# #     return checkin, checkout




# class MyClass:
#     class_attribute = "Class"

#     def __init__(self):
#         self.instance_attribute = "Instance"




# my_object = MyClass()

# print(f"Распечатываем my_object - {my_object}")
# print(f"Распечатываем my_object.__dict__ - {my_object.__dict__}")
# print(MyClass.__dict__)



# class Person:
#     def __init__(self, name, lastname):
#         self.name = name
#         self.lastname = lastname

#     def greet(self):
#         return f"Hello {self.name}"
    

# Irina = Person("Ira", "Geibo")

# print(f"Распечатываем Irina.__dict__ - {Irina.__dict__}")


# data_dict = {
#     key: value for key, value in Irina.__dict__.items()
# }

# print(data_dict)

# print(Irina.__dict__["name"])
# #  def create_request_body(self, schema, data_class_instance):
# #         data_dict = {
# #             key: value for key, value in data_class_instance.__dict__.items()
# #         }
# #         return schema(**data_dict).model_dump_json()


# # Добавление атрибутов к экземпляру класса
# Irina.__dict__["current_city"] = "Toronto"

# print(Irina.current_city)
# print(Irina.__dict__)

# # Удаление атрибутов
# del Irina.__dict__["current_city"]

# print(Irina.__dict__)
# print(Irina.__dict__.items())


# my_dict = {"name": "Vasia", "age": 99}
# print(my_dict.items())


# for key, value in my_dict.items():
#     print(f"Ключ - {key}, значение - {value}") 

# import requests
# from bs4 import BeautifulSoup


# response=requests.get("https://www.geeksforgeeks.org/python/response-raise_for_status-python-requests/")
# soup = BeautifulSoup(response.content, "html.parser")
# print(soup)

# print(soup.title.text)

# print(soup.find("p").text)

# links = [a["href"] for a in soup.find_all("a")]
# print(links)








# load_dotenv()






# generator=BookingGenerator()

# booking_info=generator.generate_booking()
# print(f"booking_info - {booking_info}")





class Dog(BaseModel):
    age: int

    @field_validator('age')
    def check_age(cls, value):
        if value < 18:
            raise ValueError('Возраст должен быть больше 18 лет')
        return value
    

dog1=Dog(age=19)


import math

print(dir(math))

name="irina"

def hello(name):
    print(f"Привет {name}")


print(hello.__name__)
