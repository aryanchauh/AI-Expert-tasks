import requests
from bs4 import BeautifulSoup

# Define the URL to scrape
url = "https://www.shutterstock.com/?irclickid=QZM1rvV0uxyPTrhxo5wB93zZUkHToKS2F2GBzs0&irgwc=1&pl=274393-42119&utm_campaign=admitad%20GmbH%20-%20Shutterstock&utm_content=42119&utm_medium=Affiliate&utm_source=274393&utm_term=2075099"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Find and print the main content of the page
    main_content = soup.find(id="main-content")
    if main_content:
        print(main_content.text)
    else:
        print("Main content not found on the page.")
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)
