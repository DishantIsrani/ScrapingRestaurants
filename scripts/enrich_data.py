import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def enrich_data_with_openai(restaurant_data):
    enriched_data = []
    
    for restaurant in restaurant_data:
        try:
            dietary_offerings = generate_dietary_offerings(restaurant['menu_items'])
            customer_reviews = get_customer_reviews(restaurant['name'])
            allergens = extract_allergens(customer_reviews)

            restaurant['dietary_offerings'] = dietary_offerings
            restaurant['allergens'] = allergens
            
            enriched_data.append(restaurant)
        
        except Exception as e:
            print(f"Error enriching data for {restaurant['name']}: {e}")
    
    return enriched_data

def generate_dietary_offerings(menu_items):
    prompt = f"Identify the dietary offerings (e.g., vegan, vegetarian, gluten-free) from the following menu items:\n{menu_items}"
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", 
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=100
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"Error generating dietary offerings: {e}")
        return "Error: Unable to generate dietary offerings"

def extract_allergens(reviews):
    prompt = f"Extract allergens mentioned in the following customer reviews:\n{reviews}"
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", 
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=100
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"Error extracting allergens: {e}")
        return "Error: Unable to extract allergens"

def get_customer_reviews(restaurant_name):
    try:
    
        return "Customer reviews for " + restaurant_name
    except Exception as e:
        print(f"Error fetching customer reviews for {restaurant_name}: {e}")
        return "Error: Unable to fetch customer reviews"
