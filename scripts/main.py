import json
from config import RESTAURANT_URL
from scrape_data import scrape_restaurant_data
from enrich_data import enrich_data_with_openai
from validate_data import validate_data

def store_data_in_file(data, filename):
    try:
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print(f"Error saving data to file: {e}")

def main():
    try:
        scraped_data = scrape_restaurant_data(RESTAURANT_URL)
        
        validated_data = validate_data(scraped_data)
        
        enriched_data = enrich_data_with_openai(validated_data)
        
        store_data_in_file(enriched_data, 'data/restaurant_data.json')

    except Exception as e:
        print(f"An error occurred in the main process: {e}")

if __name__ == '__main__':
    main()
