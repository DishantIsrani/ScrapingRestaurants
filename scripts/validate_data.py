def validate_data(restaurant_data):
    valid_data = []
    for restaurant in restaurant_data:
        if restaurant['phone'] and restaurant['email']:
            valid_data.append(restaurant)
    return valid_data