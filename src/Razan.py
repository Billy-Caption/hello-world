import os

import requests


def get_mars_weather():
    url = f"{os.getenv('NASA_API_ROOT')}/insight_weather/?api_key={os.getenv('NASA_API_KEY')}&feedtype=json&ver=1.0"
    response = requests.get(url)
    if response.status_code == 200:
        if not response.text:
            raise Exception("API returned an empty response — the InSight Weather API was decommissioned in 2022")
        data = response.json()
        return data
    else:
        raise Exception(f"Failed to fetch Mars weather data: {response.status_code} — {response.text}")


if __name__ == "__main__":
    mars_weather = get_mars_weather()
    print(mars_weather)
