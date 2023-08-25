import requests
from bs4 import BeautifulSoup

def scrape(url):
    try:
        # HTTP GET request to the website
        response = requests.get(url)

        # if the request was successful
        if response.status_code == 200:
            # Parseing the HTML content of the website
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find all quote elements on the web page
            quotes = soup.find_all('div', class_='quoteText')

            # Extract and print 
            for quote in quotes:
                # Get the quote text
                text = quote.text.strip().split('\n')[0].strip()

                # Get the author name
                author = quote.find('span', class_='authorOrTitle').text.strip()

                print(f"Quote: {quote}")
                print(f"Author: {author}")
                print('-' * 50)

        else:
            print(f"Failed to fetch data. Status Code: {response.status_code}")

    except requests.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    
    url = "https://www.goodreads.com/quotes"

    scrape(url)
