import requests
import json
from configs.yahoo_config import yahoo_config


class YahooAPIHelper:
    """
    Connects to the Yahoo Finance API and pulls quotes for you.
    get_quote() is your entrypoint here.
    """

    def __init__(self):
        self._config = yahoo_config
        self._config_checks_out = self._check_config()
        print("Yahoo API Helper instantiated")

    def get_quote(self, symbols: str = "GME") -> dict:
        """
        Gets the current price of one or more stock symbols

        :param symbols: a comma separated list of stock symbols
        :return: the prices of the stocks and basic context info
        """

        quote_endpoint = self._config["quote_endpoint"]
        params = self._prepare_quote_params(symbols)

        response = self._get_from_api(url=quote_endpoint, params=params)
        response = self._parse_quote(response)

        return response

    def _get_from_api(self, url: str, params: dict, headers: dict = None ) -> str:
        """
        Performs a GET from the API

        :param url: the endpoint you want to hit
        :param params: the query params for the GET
        :param headers: your api headers, authentication etc - defaults from config used when empty

        :return: the response from the API
        """

        if not headers:
            headers = self._prepare_headers()

        response = requests.request("GET", url, headers=headers, params=params)

        return response.text

    def _prepare_headers(self) -> dict:
        """
        Prepares headers dict from config
        """

        headers = {
            "x-api-key": self._config['x-api-key']
        }

        return headers

    @staticmethod
    def _prepare_quote_params(symbols: str) -> dict:
        """
        Prepares params for quote.

        :param symbols: A comma-separated list of symbols to get quotes for.
        :return: the params to be sent to the api
        """

        params = {

            "symbols": symbols

        }

        return params

    def _check_config(self) -> bool:
        """
        Performs some rudimentary checks on the config file, raises errors if they don't pass.
        Prevents running the program without proper configs.

        :return: True when everything checks out.
        """

        checklist = [
            "x-api-key" in self._config,
            "quote_endpoint" in self._config
        ]

        checks_out = all(checklist)

        if not checks_out:
            raise ValueError("yahoo_config.py is not set up properly")

        return checks_out

    def _parse_quote(self, quote_json: str) -> dict:
        """
        The quotes returned by the API are predictably JSON. We need to extract the info we need for easier digestion.

        :param quote_json: The response from a quote call.
        :return: A simplified view of the response
        """

        quote_dict = json.loads(quote_json)

        quote_result = quote_dict["quoteResponse"]["result"][0]

        keys_to_keep = self._config["QUOTE_RESULTS_TO_KEEP"]

        filtered_dict = {k: quote_result[k] for k in keys_to_keep if k in quote_result}

        return filtered_dict


if __name__ == "__main__":

    api_helper = YahooAPIHelper()

    quote = api_helper.get_quote()
