import requests

from bs4 import BeautifulSoup

def format_book_list_to_str(items):
    # ["first", "second", 'third']
    if not items:
        return
    
    if len(items) == 1:
        return items[0]
    
    return f"{', '.join(items[:-1])} and {items[-1]}"

url = "http://books.toscrape.com"

try:
    response = requests.get(url)
except requests.exceptions.RequestException as e:
    print(f"Oops! Something went wrong: {e}")
else:
    if response.status_code == 200:

        html = response.text

        soup = BeautifulSoup(html, "html.parser")

        # h1 = soup.find('h1')
        # print(f"h1 found: {h1}")
        # h1s = soup.find_all('h1')
        # print(f"h1s found: {h1s}")
        # ps = soup.find_all('p')
        # print(f"ps found: {ps}")

        # articles = soup.find_all('article', class_='product_pod')
        # for article in articles:
        #     image_container_div = article.find('div', class_="image_container")
        #     link = image_container_div.find('a').get('href')
        #     print(link)
        #     print()

        # links = soup.select('article.product_pod div.image_container a')
        # hrefs = [link.get("href") for link in links]
        # print(hrefs)
        
        # 1. Count total number of books
        articles = soup.find_all('article', class_='product_pod')
        # print(f"Total number of books: {len(articles)}")

        # 2. Calculate the average price
        prices = soup.select('article.product_pod div.product_price p.price_color')
        prices = [float(price.text[2:]) for price in prices]
        # average_price = sum(prices) / len(prices)
        # print(f"The average price is: {round(average_price, 2)}")

        # 3. Find the most expensive book
        book_titles = [book.select('h3 a')[0].text for book in articles]
        # print(book_titles)
        book_titles.append("New Book")
        prices.append(57.25)
        book_titles.append("Newest Book")
        prices.append(57.25)
        zipped = zip(book_titles, prices)
        highest_price = max(prices)
        most_expensive_books = [book for book, price in zipped if price == highest_price]
        print(f"The most expensive books are: {format_book_list_to_str(most_expensive_books)}")

    else:
        print("That was not supposed to happen!")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")