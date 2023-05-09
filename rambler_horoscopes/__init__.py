from contextlib import suppress
from typing import List, Optional

import httpx_cache
import orjson  # pylint:disable=import-error
import pkg_resources
from bs4 import BeautifulSoup  # pylint:disable=import-error

from rambler_horoscopes.types import Horoscope, Zodiac
from rambler_horoscopes.types.enum import HoroscopePeriod, HoroscopeType, RequestMethod
from rambler_horoscopes.types.enum import Zodiac as ZodiacEnum

try:
    __version__ = pkg_resources.get_distribution("songlink_api").version
except pkg_resources.DistributionNotFound:
    __version__ = ""


class RamblerHoroscopes:
    """
    A fast and asynchronous wrapper for the Rambler Horoscopes API written in Python.
    """

    def __init__(
        self,
        api_url: str = "https://horoscopes.rambler.ru/api/front/v3/horoscope/",
        api_timeout: int = 60,
        use_cache: bool = True,
        cache_time: int = 3600,
    ):
        self.api_url = api_url
        self.api_timeout = api_timeout
        self.use_cache = use_cache
        self.cache_time = cache_time

    async def _make_request(
        self,
        method: RequestMethod,
        url: str,
        params: Optional[dict] = None,
        data: Optional[dict] = None,
    ):
        """
        Asynchronously sends an HTTP request and returns the response content as a JSON object.

        This function uses the httpx_cache.AsyncClient to send the request with the specified
        method, url, params and data. It also sets the headers with the User-Agent and
        cache-control values based on the self attributes. It uses the httpx_cache.FileCache
        to cache the responses if self.use_cache is True. It uses the orjson library to
        serialize and deserialize the data and response content. It also sets the timeout for
        the request based on the self.api_timeout attribute.

        Args:
            method: A RequestMethod enum member that represents the HTTP request method to use.
            url: A string that represents the URL of the resource to request.
            params: An optional dictionary that contains the query parameters to append to the URL.
            data: An optional dictionary that contains the data to send in the request body.

        Returns:
            A JSON object that represents the response content.

        Raises:
            httpx.HTTPError: If an error occurs while sending or receiving the HTTP request.
            orjson.JSONDecodeError: If an error occurs while decoding the response content.
        """
        async with httpx_cache.AsyncClient(
            headers={
                "User-Agent": f"rambler_horoscopes/v{__version__}",
                "cache-control": f"max-age={self.cache_time}"
                if self.use_cache
                else "no-cache",
            },
            cache=httpx_cache.FileCache(),
        ) as client:
            request = client.build_request(
                method=method.value,
                url=url,
                params={k: v for k, v in params.items() if v is not None}
                if params is not None
                else None,
                data=orjson.dumps(data) if data is not None else None,
                timeout=self.api_timeout,
            )
            response = await client.send(request)
            return orjson.loads(response.content)

    async def get_zodiac(self, zodiac: ZodiacEnum):
        """
        Returns a Zodiac object that contains the information about the given zodiac sign.

        Args:
            - `zodiac`: A Zodiac enumeration member that represents the zodiac sign to get information about.

        Returns:
            A Zodiac object that contains the information about the given zodiac sign.

        Raises:
            - `httpx.HTTPError`: If an error occurs while sending or receiving the HTTP request.
            - `orjson.JSONDecodeError`: If an error occurs while decoding the response content.
        """

        data = await self._make_request(
            method=RequestMethod.GET,
            url=self.api_url + "description/" + zodiac.value + "/",
        )
        output_dicted = {"zodiac": zodiac}

        for content in data["content"]["text"]:
            if content["type"] != "paragraph":
                break
            if not hasattr(output_dicted, "description"):
                output_dicted["description"] = str()
            output_dicted["description"] += content["content"] + "\n"
        if output_dicted.get("description") is not None:
            output_dicted["description"] = BeautifulSoup(
                output_dicted["description"], "html.parser"
            ).text.strip()

        if len(data["content"]["highlighted"]["list"][0]["items"]) >= 1:
            for i in range(len(data["content"]["highlighted"]["list"][0]["items"])):
                match data["content"]["highlighted"]["list"][0]["items"][i]["name"]:
                    case "Родились":
                        output_dicted["born"] = str(
                            data["content"]["highlighted"]["list"][0]["items"][i][
                                "text"
                            ]
                        ).lower()
                    case "Стихия":
                        output_dicted["element"] = str(
                            data["content"]["highlighted"]["list"][0]["items"][i][
                                "text"
                            ]
                        ).lower()

            if data["content"]["summary"].get("trait") is not None:
                output_dicted["trait"] = ", ".join(
                    data["content"]["summary"]["trait"]
                ).lower()
            if data["content"]["summary"].get("planet") is not None:
                output_dicted["planet"] = ", ".join(
                    data["content"]["summary"]["planet"]
                ).lower()
            if data["content"]["summary"].get("house") is not None:
                output_dicted["house"] = ", ".join(
                    data["content"]["summary"]["house"]
                ).lower()
            if data["content"]["summary"].get("tarot") is not None:
                output_dicted["tarot"] = ", ".join(
                    data["content"]["summary"]["tarot"]
                ).lower()
            if data["content"]["summary"].get("color") is not None:
                output_dicted["color"] = ", ".join(
                    data["content"]["summary"]["color"]
                ).lower()
            if data["content"]["summary"].get("stone") is not None:
                output_dicted["stone"] = ", ".join(
                    data["content"]["summary"]["stone"]
                ).lower()
            if data["content"]["summary"].get("flower") is not None:
                output_dicted["flower"] = ", ".join(
                    data["content"]["summary"]["flower"]
                )
            if data["content"]["summary"].get("compatibility") is not None:
                with suppress(ValueError):
                    output_dicted["compatibility"] = list(
                        map(
                            lambda e: ZodiacEnum.from_name(  # pylint:disable=unnecessary-lambda
                                e
                            ),
                            data["content"]["summary"]["compatibility"],
                        )
                    )

        return Zodiac(**output_dicted)

    async def get_available_types(self, zodiac: ZodiacEnum) -> List[HoroscopeType]:
        """
        Returns a list of HoroscopeType members that are available for the given zodiac sign.

        Args:
            - `zodiac`: A Zodiac enumeration member that represents the zodiac sign to get available
                horoscopes for.

        Returns:
            A list of HoroscopeType members that are available for the given zodiac sign.

        Raises:
            - `httpx.HTTPError`: If an error occurs while sending or receiving the HTTP request.
            - `orjson.JSONDecodeError`: If an error occurs while decoding the response content.
        """
        data = await self._make_request(
            method=RequestMethod.GET,
            url=self.api_url + HoroscopeType.GENERAL + "/" + zodiac.value + "/today/",
        )
        output = [HoroscopeType.GENERAL]
        for card in data["cards"]:
            for story in card["stories"]:
                horoscope_type = story["link"].split("/")[2]
                if horoscope_type in list(HoroscopeType):
                    output.append(HoroscopeType(horoscope_type))
                if horoscope_type == "erotic":
                    output.append(HoroscopeType.LOVE)
                if horoscope_type == "sex-horoscope":
                    output.append(HoroscopeType.SEX)
        return sorted(output, key=lambda e: list(HoroscopeType).index(e))

    async def get_available_periods(
        self, zodiac: ZodiacEnum, horoscope_type: HoroscopeType = HoroscopeType.GENERAL
    ) -> List[HoroscopePeriod]:
        """
        Returns a list of HoroscopePeriod members that are available for the
        given zodiac sign and horoscope type.

        Args:
            - `zodiac`: A Zodiac enumeration member that represents the zodiac sign to get
                available periods for.
            - `horoscope_type`: An optional HoroscopeType member that represents the
                type of horoscope to get available periods for. Defaults to HoroscopeType.GENERAL.

        Returns:
            A list of HoroscopePeriod members that are available for the given zodiac sign and horoscope type.

        Raises:
            - `httpx.HTTPError`: If an error occurs while sending or receiving the HTTP request.
            - `orjson.JSONDecodeError`: If an error occurs while decoding the response content.
        """
        data = await self._make_request(
            method=RequestMethod.GET,
            url=self.api_url + horoscope_type.value + "/" + zodiac.value + "/today/",
        )
        output = [HoroscopePeriod.TODAY]
        for bubble in data["content"]["bubbles"]["list"]:
            horoscope_period = bubble["link"].split("/")[
                3 if horoscope_type != HoroscopeType.GENERAL else 2
            ]
            if horoscope_period in list(HoroscopePeriod):
                output.append(HoroscopePeriod(horoscope_period))
        return sorted(output, key=lambda e: list(HoroscopePeriod).index(e))

    async def get_horoscope(
        self,
        zodiac: ZodiacEnum,
        horoscope_type: HoroscopeType = HoroscopeType.GENERAL,
        period: HoroscopePeriod = HoroscopePeriod.TODAY,
    ):
        """
        Returns a Horoscope object that contains the horoscope for the given zodiac sign, type and period.

        Args:
            - `zodiac`: A ZodiacEnum member that represents the zodiac sign to get the horoscope for.
            - `horoscope_type`: An optional HoroscopeType member that represents the type of horoscope
                to get. Defaults to HoroscopeType.GENERAL.
            - `period`: An optional HoroscopePeriod member that represents the period of the horoscope
                to get. Defaults to HoroscopePeriod.TODAY.

        Returns:
            A Horoscope object that contains the horoscope for the given zodiac sign, type and period.

        Raises:
            - `httpx.HTTPError`: If an error occurs while sending or receiving the HTTP request.
            - `orjson.JSONDecodeError`: If an error occurs while decoding the response content.
        """

        data = await self._make_request(
            method=RequestMethod.GET,
            url=self.api_url + horoscope_type.value + "/" + zodiac.value + "/today/",
        )
        output_dicted = {"zodiac": zodiac, "type": horoscope_type, "period": period}

        for content in data["content"]["text"]:
            if content["type"] != "paragraph":
                break
            if not hasattr(output_dicted, "text"):
                output_dicted["text"] = str()
            output_dicted["text"] += content["content"] + "\n"
        if output_dicted.get("text") is not None:
            output_dicted["text"] = BeautifulSoup(
                output_dicted["text"], "html.parser"
            ).text.strip()
        return Horoscope(**output_dicted)
