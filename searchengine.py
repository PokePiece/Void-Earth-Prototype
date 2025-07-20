#AIzaSyBIJBPEO7kc4x_qeCe_NgIafmRi2pEgMNc
#Google API Key
#id d51c54d71d0544094

import requests

def google_search(query, api_key, cse_id):
    # Construct the URL for the search query
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={api_key}&cx={cse_id}"

    # Send the request to Google Custom Search
    response = requests.get(url)

    # If the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        results = response.json()
        
        # Extract the top result
        if "items" in results:
            top_result = results["items"][0]
            title = top_result["title"]
            snippet = top_result["snippet"]
            link = top_result["link"]

            # Print the result (You can customize this part)
            print(f"Title: {title}")
            print(f"Snippet: {snippet}")
            print(f"Link: {link}")
        else:
            print("No results found.")
    else:
        print("Error in the search request:", response.status_code)

if __name__ == "__main__":
    # Your API key and Custom Search Engine ID
    api_key = "AIzaSyBIJBPEO7kc4x_qeCe_NgIafmRi2pEgMNc"
    cse_id = "d51c54d71d0544094"

    # Query to search
    query = input("Enter a search query: ")

    google_search(query, api_key, cse_id)
