import requests
from pydantic import TypeAdapter, ValidationError
import allure



class Validate:
    @allure.step("Verify that the response matches the expected JSON schema")
    def validate(self, response, schema):
        try:
            schema.model_validate(response.json())
        except ValueError as e:
            raise ValueError((f"Invalid response format in {e}"))
    
# TypeAdapter(...): Это класс Pydantic,
# который позволяет использовать возможности
# валидации Pydantic для типов, не являющихся BaseModel
# (например, для списков, словарей, примитивов)
    @allure.step("Verify that the response matches the expected JSON schema")
    def validate_list(self, response, schema):
        try:
            adapter = TypeAdapter(list[schema])
            adapter.validate_python(response.json())
        except ValidationError as e:
            raise ValidationError(f"Invalid response format in {e}")

