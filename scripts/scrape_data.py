import requests
from bs4 import BeautifulSoup

def scrape_restaurant_data(html_content):
    try:
        response = requests.get(html_content)
        response.raise_for_status()  
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the HTML content: {e}")
        return []

    try:
        soup = BeautifulSoup(response.content, 'html.parser')
        restaurant_elements = soup.find_all('div', class_='restaurant')

        restaurant_data = []

        for restaurant in restaurant_elements:
            name = restaurant.find('h2', class_='name')
            address = restaurant.find('p', class_='address')
            phone = restaurant.find('p', class_='phone')
            email = restaurant.find('p', class_='email')
            menu_items = restaurant.find('ul', class_='menu')

            if not all([name, address, menu_items]):
                print("Missing required restaurant information.")
                continue

            restaurant_info = {
                'name': name.text.strip(),
                'address': address.text.strip(),
                'phone': phone.text.strip() if phone else None,
                'email': email.text.strip() if email else None,
                'menu_items': [item.text.strip() for item in menu_items.find_all('li')]
            }

            restaurant_data.append(restaurant_info)

        return restaurant_data

    except Exception as e:
        print(f"Error parsing the HTML content: {e}")
        return []

url = "https://www.yelp.com/search?find_desc=Restaurants&find_loc=San+Francisco%2C+CA"
# url = "https://www.zomato.com/mumbai/near-andheri-west-station-restaurants?ccp_id=7363&category=2"
restaurant_data = scrape_restaurant_data(url)
print(restaurant_data)
