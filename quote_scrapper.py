import requests
from bs4 import BeautifulSoup
from time import sleep
from csv import DictWriter

BASE_URL = 'http://quotes.toscrape.com/'


def scrape_quotes():
	all_quotes = []
	url = "/page/1"

	while url:
		res = requests.get(f"{BASE_URL}{url}")
		
		print(f"Now Scrapping {BASE_URL}{url}...")

		soup = BeautifulSoup(res.text, "html.parser")
		quotes = soup.select(".quote")

		for q in quotes:
			bio_link = q.find("a")["href"]

			all_quotes.append({
				"text": q.find(class_="text").get_text(),
				"author": q.find(class_="author").get_text(),
				"bio": get_bio(bio_link)
				})

		next_btn = soup.find(class_="next")
		url = next_btn.find("a")["href"] if next_btn else None
		sleep(0.05)
	
	return all_quotes

def get_bio(bio_link):
	res = requests.get(f"{BASE_URL}{bio_link}")
	soup = BeautifulSoup(res.text, "html.parser")
	
	birth_date = soup.find(class_="author-born-date").get_text()
	birth_place = soup.find(class_="author-born-location").get_text()
	
	return f"{birth_date} {birth_place}"


#write quotes to csv file
def write_quotes(quotes):
	with open("quotes.csv", "w") as file:
		headers = ["text","author","bio"]
		csv_writer = DictWriter(file, fieldnames=headers)
		csv_writer.writeheader()
		for q in quotes:
			csv_writer.writerow(q)

all_quotes = scrape_quotes()
write_quotes(all_quotes)

