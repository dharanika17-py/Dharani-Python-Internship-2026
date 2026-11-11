import json
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
from urllib.parse import quote


def fetch_api(url):
    request = Request(
        url,
        headers={"User-Agent": "StudentCountryProject/1.0"}
    )

    with urlopen(request, timeout=20) as response:
        return json.loads(response.read().decode("utf-8"))


def get_country_info(country_name):
    if not country_name.strip():
        print("Please enter a country name.")
        return

    try:
        url = "https://api.worldbank.org/v2/country?format=json&per_page=400"
        data = fetch_api(url)

        if not isinstance(data, list) or len(data) < 2:
            print("Invalid API response.")
            return

        countries = data[1]

        country = next(
            (item for item in countries
             if item["name"].lower() == country_name.strip().lower()),
            None
        )

        if country is None:
            print("No matching country found.")
            return

        code = country["id"]

        population_url = (
            f"https://api.worldbank.org/v2/country/{quote(code)}"
            "/indicator/SP.POP.TOTL?format=json&mrnev=1"
        )

        population_data = fetch_api(population_url)

        population = "N/A"

        if isinstance(population_data, list) and len(population_data) > 1:
            records = population_data[1]

            if records:
                value = records[0].get("value")
                if value is not None:
                    population = f"{int(value):,}"

        print("\n===== COUNTRY INFORMATION =====")
        print("Name:", country["name"])
        print("Capital:", country["capitalCity"] or "N/A")
        print("Population:", population)
        print("Region:", country["region"]["value"])
        print("Income Level:", country["incomeLevel"]["value"])
        print("Country Code:", code)

    except HTTPError as error:
        print("API Error:", error.code)

    except URLError:
        print("Network error. Check your internet connection.")

    except (json.JSONDecodeError, KeyError, TypeError, IndexError):
        print("Invalid API response.")

    except TimeoutError:
        print("API request timed out.")

    except OSError as error:
        print("Connection error:", error)


while True:
    country = input("\nEnter country name (or exit): ").strip()

    if country.lower() == "exit":
        print("Thank you!")
        break

    get_country_info(country)