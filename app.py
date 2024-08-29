import requests
from bs4 import BeautifulSoup

def get_all_urls(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors

        soup = BeautifulSoup(response.content, 'html.parser')

        urls = []
        for link in soup.find_all('a'):
            href = link.get('href')
            if href:
                urls.append(href)

        return urls

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return []  # Return an empty list in case of errors

# Example usage
target_website = "https://www.indianyellowpages.com/ahmedabad/"  # Replace with the website you want to scrape
all_urls = get_all_urls(target_website)

if all_urls:
    print("URLs found:")
    for url in all_urls:
        print(url)
else:
    print("No URLs found or an error occurred.")
