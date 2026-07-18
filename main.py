import re
from datetime import datetime
from tabulate import tabulate
import json

def get_forecast_data():
    import undetected_chromedriver as uc
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from bs4 import BeautifulSoup
    import time

    options = uc.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--log-level=3')

    print("Launching browser in GUI mode...")
    driver = uc.Chrome(options=options, version_main=149)


    try:
        print("Opening website... Waiting to bypass Cloudflare protection automatically...")
        driver.get("https://world-weather.info/")

        time.sleep(7)

        print("Adding cookies and refreshing the page to apply Celsius setting...")
        driver.add_cookie({'name': 'celsius', 'value': '1'})
        driver.refresh()

        print("Waiting for the weather data (resorts) to load...")
        # الانتظار حتى يظهر العنصر المطلوب
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "resorts"))
        )

        # استخراج البيانات بواسطة BeautifulSoup
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        resorts = soup.find_all("div", id="resorts")

        re_cities = r'">([\w\s]+)<\/a><span>'
        cities = re.findall(re_cities, str(resorts))

        re_temps = r'<span>(\+\d+|-\d+)<span'
        temps = re.findall(re_temps, str(resorts))
        temps = [int(temp) for temp in temps]

        conditions_tags = soup.find_all('span', class_='tooltip')
        conditions = [condition.get('title') for condition in conditions_tags]

        data = zip(cities, temps, conditions)

        return data


    except Exception as e:
        print(f"\n[!] Operation failed. Error type: {type(e).__name__}")

    finally:
        time.sleep(3)
        driver.quit()

def get_forecast_txt():
    data = get_forecast_data()

    if data:
        today = datetime.today().strftime('%d/%m/%Y')
        with open("output.txt", "w", encoding="utf-8") as f:
            f.write('Popular Cities Forecast' + '\n')
            f.write(today + '\n')
            f.write('='*23 + '\n')
            table = tabulate(data, headers=['City', 'Temp.', 'Condition'], tablefmt='fancy_grid')
            f.write(table)


def get_forecast_json():
    data = get_forecast_data()
    if data:
        today = datetime.today().strftime('%d/%m/%Y')

        cities = [{'city': city, 'temp': temp, 'condition': condition} for city, temp, condition in data]
        data_json = {'title': 'Popular Cities Forecast', 'date': today, 'data': cities}
        with open("output.json", "w", encoding="utf-8") as f:
            json.dump(data_json, f, ensure_ascii=False)


if __name__ == '__main__':
    get_forecast_txt()
    get_forecast_json()