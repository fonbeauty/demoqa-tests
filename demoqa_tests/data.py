from dataclasses import dataclass


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    mobile_number: str
    birthday_year: int
    birthday_month: str
    birthday_day: int
    subjects: list[str]
    picture: str
    address: str
    state: str
    city: str
    hobbi_sports: bool = False
    hobbi_reading: bool = False
    hobbi_music: bool = False
