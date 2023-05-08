from typing import List, Optional

from pydantic import BaseModel  # pylint:disable=import-error

from rambler_horoscopes.types.enum import HoroscopePeriod, HoroscopeType
from rambler_horoscopes.types.enum import Zodiac as ZodiacEnum


class Zodiac(BaseModel):  # pylint:disable=too-few-public-methods
    """
    A class that represents a zodiac sign and its attributes.

    This class inherits from the BaseModel class and defines the fields
    for a zodiac sign and its attributes, such as description, element,
    planet, color, etc. It also uses the Zodiac enumeration to represent
    the id and compatibility fields.

    Attributes:
        - `zodiac`: A Zodiac enumeration member that represents the identifier of the zodiac sign.
        - `description`: A string that represents a brief description of the zodiac sign.
        - `born`: A string that represents the date range of the zodiac sign.
        - `element`: A string that represents the element associated with the zodiac sign.
        - `trait`: A string that represents the main trait of the zodiac sign.
        - `planet`: A string that represents the ruling planet of the zodiac sign.
        - `house`: A string that represents the astrological house of the zodiac sign.
        - `tarot`: A string that represents the tarot card of the zodiac sign.
        - `color`: A string that represents the lucky color of the zodiac sign.
        - `stone`: A string that represents the lucky stone of the zodiac sign.
        - `flower`: A string that represents the lucky flower of the zodiac sign.
        - `compatibility`: A Zodiac enumeration member that represents the most compatible zodiac
            sign for this sign.
    """

    zodiac: ZodiacEnum
    description: str
    born: str
    element: str
    trait: Optional[str] = None
    planet: Optional[str] = None
    house: Optional[str] = None
    tarot: Optional[str] = None
    color: Optional[str] = None
    stone: Optional[str] = None
    flower: Optional[str] = None
    compatibility: List[ZodiacEnum] = []


class Horoscope(BaseModel):
    """
    A class that represents a horoscope for a zodiac sign.

    This class inherits from the BaseModel class and defines the fields
    for a horoscope, such as id, type, period and text. It also uses the
    Zodiac, HoroscopeType and HoroscopePeriod enumerations to represent
    the id, type and period fields.

    Attributes:
        - `id`: A ZodiacEnum member that represents the identifier of the
            zodiac sign for which the horoscope is given.
        - `type`: A HoroscopeType member that represents the type of the
            horoscope, such as erotic, career, woman, etc.
        - `period`: A HoroscopePeriod member that represents the period of
            the horoscope, such as yesterday, today, tomorrow, weekly, monthly, etc.
        - `text`: A string that represents the text of the horoscope.
    """

    zodiac: ZodiacEnum
    type: HoroscopeType
    period: HoroscopePeriod
    text: str
