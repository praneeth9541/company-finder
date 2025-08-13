def get_companies_in_tech_park(api_key, tech_park_name):
    """
    Fetches a list of companies in a specified tech park using the Google Places API.
    """
    
    # The Google Places Text Search endpoint
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    
    # The parameters for our request
    params = {
        "query": f"companies in {tech_park_name}",
        "key": api_key
    }
    
    try:
        # Make the GET request to the API
        response = requests.get(url, params=params)
        response.raise_for_status() # Raise an exception for bad status codes (4xx or 5xx)
        
        # Parse the JSON response
        data = response.json()
        
        # Check if the request was successful
        if data['status'] == 'OK':
            companies = [place['name'] for place in data['results']]
            return companies
        else:
            print(f"Error from Google Places API: {data.get('error_message', 'No error message provided.')}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while making the API request: {e}")
        return None

if __name__ == "__main__":
    if not API_KEY or API_KEY == "YOUR_Google Maps_API_KEY":
        print("Please replace 'YOUR_Google Maps_API_KEY' with your actual API key.")
    else:
        company_list = get_companies_in_tech_park(API_KEY, TECH_PARK_NAME)
        
        if company_list:
            print(f"Found companies in {TECH_PARK_NAME}:")
            for company in company_list:
                print(f"- {company}")