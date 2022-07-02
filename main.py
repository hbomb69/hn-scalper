from classes.YahooAPIHelper import YahooAPIHelper


def main():
    """
    Starts the process
    """

    api_helper = YahooAPIHelper()

    quote = api_helper.get_quote()

    print(quote)


if __name__ == "__main__":
    main()
