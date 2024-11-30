from faker import Faker
class User:
    @staticmethod
    def create_user_data():
        fake = Faker()

        registrations_data = {
            "email": fake.email(),
            "password": fake.password(),
            "name": fake.name()}
        return registrations_data

    data_correct = {
        "email": 'test_1124@yandex.ru',
        "password": "password"}

    data_negative = {
        "email": 'tests_261124@yandex.ru',
        "password": "password"}

    data_full = {
        "email": 'test_1124@yandex.ru',
        "password": "password",
        "name": "Username"}

    data_not_email = {
        "email": '',
        "password": "password",
        "name": "Username"}

    data_not_password = {
        "email": 'test_1124@yandex.ru',
        "password": "",
        "name": "Username"}

    data_not_name = {
        "email": 'test_1124@yandex.ru',
        "password": "password",
        "name": ""}

    data_upd = {
        "email": 'test_1124@yandex.ru',
        "password": "password",
        "name": "otherName"}