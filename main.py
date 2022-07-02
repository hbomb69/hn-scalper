from classes.YahooAPIHelper import YahooAPIHelper
from classes.CSVImporter import CSVImporter


def main():
    """
    Starts the process
    """

    api_helper = YahooAPIHelper()
    csv_importer = CSVImporter()

    historic_data = csv_importer.get_historic_data()
    print(historic_data)

    quote = api_helper.get_quote()
    print(quote)


if __name__ == "__main__":
    main()
