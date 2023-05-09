from enum import Enum


class RequestMethod(str, Enum):
    """An enumeration of the HTTP request methods.

    Each member of this class is a string that represents the name of a HTTP request
    method in uppercase.

    Attributes:
        - `GET`: The GET method requests a representation of the specified resource.
            Requests using GET should only retrieve data and should have no other effect.
        - `POST`: The POST method is used to submit an entity to the specified resource,
            often causing a change in state or side effects on the server.
        - `PUT`: The PUT method replaces all current representations of the target
            resource with the request payload.
        - `DELETE`: The DELETE method deletes the specified resource.
        - `HEAD`: The HEAD method asks for a response identical to that of a GET request,
            but without the response body.
        - `OPTIONS`: The OPTIONS method is used to describe the communication options
            for the target resource.
        - `PATCH`: The PATCH method is used to apply partial modifications to a resource.
    """

    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    HEAD = "HEAD"
    OPTIONS = "OPTIONS"
    PATCH = "PATCH"


class Zodiac(str, Enum):
    """
    An enumeration of the 12 zodiac signs.

    Each member of this class is a string that represents the name of a zodiac sign in lowercase.

    Attributes:
        - `ARIES`: The first sign of the zodiac, symbolized by the ram.
        - `TAURUS`: The second sign of the zodiac, symbolized by the bull.
        - `GEMINI`: The third sign of the zodiac, symbolized by the twins.
        - `CANCER`: The fourth sign of the zodiac, symbolized by the crab.
        - `LEO`: The fifth sign of the zodiac, symbolized by the lion.
        - `VIRGO`: The sixth sign of the zodiac, symbolized by the maiden.
        - `LIBRA`: The seventh sign of the zodiac, symbolized by the scales.
        - `SCORPIO`: The eighth sign of the zodiac, symbolized by the scorpion.
        - `SAGITTARIUS`: The ninth sign of the zodiac, symbolized by the archer.
        - `CAPRICORN`: The tenth sign of the zodiac, symbolized by the goat.
        - `AQUARIUS`: The eleventh sign of the zodiac, symbolized by the water-bearer.
        - `PIESCES`: The twelfth sign of the zodiac, symbolized by the fish.
    """

    ARIES = "aries"  # Овен
    TAURUS = "taurus"  # Телец
    GEMINI = "gemini"  # Близнецы
    CANCER = "cancer"  # Рак
    LEO = "leo"  # Лев
    VIRGO = "virgo"  # Дева
    LIBRA = "libra"  # Весы
    SCORPIO = "scorpio"  # Скорпион
    SAGITTARIUS = "sagittarius"  # Стрелец
    CAPRICORN = "capricorn"  # Козерог
    AQUARIUS = "aquarius"  # Водолей
    PIESCES = "pisces"  # Рыбы

    def get_name(self) -> str:  # pylint:disable=too-many-return-statements
        """
        Returns the name of the zodiac sign in Russian.

        This method uses a match statement to return the corresponding name of
        the zodiac sign in Russian based on the value of self.

        Returns:
            A string that represents the name of the zodiac sign in Russian.

        Raises:
            ValueError: If self is not a valid Zodiac member.
        """
        match self:
            case Zodiac.ARIES:
                return "Овен"
            case Zodiac.TAURUS:
                return "Телец"
            case Zodiac.GEMINI:
                return "Близнецы"
            case Zodiac.CANCER:
                return "Рак"
            case Zodiac.LEO:
                return "Лев"
            case Zodiac.VIRGO:
                return "Дева"
            case Zodiac.LIBRA:
                return "Весы"
            case Zodiac.SCORPIO:
                return "Скорпион"
            case Zodiac.SAGITTARIUS:
                return "Стрелец"
            case Zodiac.CAPRICORN:
                return "Козерог"
            case Zodiac.AQUARIUS:
                return "Водолей"
            case Zodiac.PIESCES:
                return "Рыбы"
            case _:
                raise ValueError(f"Invalid Zodiac member: {self}")

    @staticmethod
    def from_name(name: str) -> "Zodiac":  # pylint:disable=too-many-return-statements
        """
        Returns the Zodiac member that corresponds to the given name in Russian.

        This method uses a match statement to return the corresponding Zodiac member
        based on the lowercase version of the name argument.

        Args:
            - `name`: A string that represents the name of the zodiac sign in Russian.

        Returns:
            A Zodiac member that corresponds to the given name.

        Raises:
            ValueError: If the name is not a valid zodiac sign in Russian.
        """
        match name.lower():
            case "овен":
                return Zodiac.ARIES
            case "телец":
                return Zodiac.TAURUS
            case "близнецы":
                return Zodiac.GEMINI
            case "рак":
                return Zodiac.CANCER
            case "лев":
                return Zodiac.LEO
            case "дева":
                return Zodiac.VIRGO
            case "весы":
                return Zodiac.LIBRA
            case "скорпион":
                return Zodiac.SCORPIO
            case "стрелец":
                return Zodiac.SAGITTARIUS
            case "козерог":
                return Zodiac.CAPRICORN
            case "водолей":
                return Zodiac.AQUARIUS
            case "рыбы":
                return Zodiac.PIESCES
            case _:
                raise ValueError(f"Invalid Zodiac member: {name}")


class HoroscopeType(str, Enum):
    """
    An enumeration of the types of horoscopes.

    Each member of this class is a string that represents the
    name of a type of horoscope in lowercase.

    Attributes:
        - `EROTIC`: The erotic horoscope, which gives insights
            into the sexual and romantic aspects of life.
        - `SEX`: The sex horoscope, which gives advice on how
            to improve the sexual compatibility and satisfaction
            with the partner.
        - `CAREER`: The career horoscope, which gives guidance
            on the professional and financial aspects of life.
        - `WOMAN`: The woman horoscope, which gives tips on how
            to enhance the feminine qualities and deal with the
            challenges of being a woman.
        - `MAN`: The man horoscope, which gives suggestions on
            how to boost the masculine traits and cope with the
            difficulties of being a man.
    """

    GENERAL = "general"
    LOVE = "love"
    SEX = "sex"
    CAREER = "career"
    WOMAN = "woman"
    MAN = "man"

    def get_name(self) -> str:  # pylint:disable=too-many-return-statements
        """
        Returns the name of the horoscope type in Russian.

        This method uses a match statement to return the corresponding name
        of the horoscope type in Russian based on the value of self.

        Returns:
            A string that represents the name of the horoscope type in Russian.

        Raises:
            - `ValueError`: If self is not a valid HoroscopeType member.
        """
        match self:
            case HoroscopeType.GENERAL:
                return "Общий"
            case HoroscopeType.LOVE:
                return "Любовный"
            case HoroscopeType.SEX:
                return "Сексуальный"
            case HoroscopeType.CAREER:
                return "Финансовый"
            case HoroscopeType.WOMAN:
                return "Женский"
            case HoroscopeType.MAN:
                return "Мужской"
            case _:
                raise ValueError(f"Invalid HoroscopeType member: {self}")


class HoroscopePeriod(str, Enum):
    """
    An enumeration of the periods of horoscopes.

    Each member of this class is a string that represents the name
    of a period of horoscope in lowercase.

    Attributes:
        - `YESTERDAY`: The yesterday period, which gives the horoscope for the previous day.
        - `TODAY`: The today period, which gives the horoscope for the current day.
        - `TOMORROW`: The tomorrow period, which gives the horoscope for the next day.
        - `WEEKLY`: The weekly period, which gives the horoscope for the current week.
        - `MONTHLY`: The monthly period, which gives the horoscope for the current month.
    """

    YESTERDAY = "yesterday"
    TODAY = "today"
    TOMORROW = "tomorrow"
    WEEKLY = "weekly"
    MONTHLY = "monthly"

    def get_name(self) -> str:  # pylint:disable=too-many-return-statements
        """
        Returns the name of the horoscope period in Russian.

        This method uses a match statement to check the value of the enum member
        and returns the corresponding name as a string. If the value is not a valid
        member of the enum, it raises a ValueError.

        Returns:
            The name of the horoscope period in Russian.

        Raises:
            ValueError: If self is not a valid HoroscopePeriod member.
        """
        match self:
            case HoroscopePeriod.YESTERDAY:
                return "Вчера"
            case HoroscopePeriod.TODAY:
                return "Сегодня"
            case HoroscopePeriod.TOMORROW:
                return "Завтра"
            case HoroscopePeriod.WEEKLY:
                return "Недельный"
            case HoroscopePeriod.MONTHLY:
                return "Месячный"
            case _:
                raise ValueError(f"Invalid HoroscopePeriod member: {self}")
