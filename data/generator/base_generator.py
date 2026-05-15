from faker import Faker

class BaseGenerator:

    def __init__(self):
        self.faker = Faker()

    def get_first_name(self, first_name):
        if first_name is None:
            return self.faker.first_name()
        return first_name
    
    def get_last_name(self, last_name):
        if last_name is None:
            return self.faker.last_name()
        return last_name
    
    def get_random_number(self, number):
        if number is None:
            return self.faker.random_int()
        return number
    
    def get_random_word(self, word):
        if word is None:
            return self.faker.word()
        return word
