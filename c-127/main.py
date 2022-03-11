from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import csv
import time

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
page = requests.get(START_URL)
headers = ['Name', 'Distance', 'Mass', 'Radius']
stars_data = []
soup = BeautifulSoup(page.text, "html.parser")
temp_list = []
time.sleep(10)

def scrape():
    table = soup.find("table")

    for tr in table.find_all("tr"):
        td = tr.find_all("td")
        row = [i.text.rstrip() for i in td]
        temp_list.append(row)

    for i in range(1,len(temp_list)):
        name = temp_list[i][1]
        distance = temp_list[i][3]
        mass = temp_list[i][5]
        radius = temp_list[i][6]
        stars_data.append((name, distance, mass, radius))

    with open('result.csv', 'w', encoding='utf-8') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(stars_data)

scrape()