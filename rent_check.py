import requests
from bs4 import BeautifulSoup
import argparse

# Validation 
def validate_bedroom(value):
    int_value = int(value)
    if int_value not in [1, 3]:
        raise argparse.ArgumentTypeError("Number of bedrooms must be either 1 or 3")
    return int_value

def validate_location(value):
    if value.lower() == 'true':
        return True
    elif value.lower() == 'false':
        return False
    else:
        raise argparse.ArgumentTypeError("Invalid value for boolean option. Use 'true' or 'false'.")

# Arguments
parser = argparse.ArgumentParser(description="Find monthly rent")
parser.add_argument('-c', '--cityname', type=str, required=True, help="Name of the city")
parser.add_argument('-b', '--bedroom', choices=[1, 3], type=validate_bedroom, required=True, help="Number of bedrooms. Options are 1 or 3")
parser.add_argument('-C', '--citycenter', type=validate_location, required=True, help="In or outside city center. true or false")
args = parser.parse_args()

# bedroom
bedroom = args.bedroom
if bedroom == 1:
    apart_type = f"Apartment ({bedroom} bedroom)"
elif bedroom == 3:
    apart_type = f"Apartment ({bedroom} bedrooms)"

# city center
citycenter = args.citycenter
if citycenter == True:
    location = "in City Centre"
elif citycenter == False:
    location = "Outside of Centre"

# request
city = args.cityname.title()
URL = f"https://www.numbeo.com/cost-of-living/in/{city}"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

# Find all <tr> elements
all_rows = soup.find_all('tr')

# Iterate through each <tr> and check if it contains the desired information
for row in all_rows:
    td_text = ''.join(td.get_text(strip=True) for td in row.find_all('td', recursive=False))
    if apart_type in td_text and location in td_text:
        price_value = row.find('td', class_='priceValue').text.strip()
        print(f"Price for {apart_type} in {city} {location}: {price_value}")
        break     
else:
    print("Cannot find any details about this city.")
