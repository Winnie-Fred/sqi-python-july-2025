import requests

import bs4

# url = "https://edu.sqi.ng"

# response = requests.get(url)

# # captcha

# # turing test: Alan Turing

# soup = bs4.BeautifulSoup(response.text, 'html.parser')
# formatter = bs4.formatter.HTMLFormatter(indent=4)

# with open("sqi-home.html", "w", encoding="utf-8") as f:
#     f.write(soup.prettify(formatter=formatter))




# url = "https://www.jumia.com.ng/"
url = "https://www.fiverr.com/"


try:
    response = requests.get(url)
except requests.exceptions.RequestException as e:
    print(f"Oops! Something went wrong: {e}")
else:
    # captcha

    # turing test: Alan Turing
    if response.status_code == 200:
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        formatter = bs4.formatter.HTMLFormatter(indent=4)

        with open("jumia-home.html", "w", encoding="utf-8") as f:
            f.write(soup.prettify(formatter=formatter))
    else:
        print("That was not supposed to happen:")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")


