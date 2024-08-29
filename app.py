import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_all_urls(url):
  try:
    response = requests.get(url)
    response.raise_for_status() 
    soup = BeautifulSoup(response.content, 'html.parser')
    urls = []
    for link in soup.find_all('a'):
      href = link.get('href')
      if href:
        urls.append(href)
    return urls
  except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
    return []

# Example Usage
target_website = "https://www.indianyellowpages.com"
all_urls = get_all_urls(target_website)

if all_urls:
  df = pd.DataFrame(all_urls, columns=['URLs'])
  df.to_excel("extracted_urls.xlsx", index=False)
  print("URLs extracted and saved to 'extracted_urls.xlsx'")
else:
  print("No URLs found or an error occurred.")
