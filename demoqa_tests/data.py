from dataclasses import dataclass


@dataclass
class User:
    first_name: str
    last_name: str
    subjects: list[str]
    email: str
    gender: str
