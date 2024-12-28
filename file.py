# -*- coding: utf-8 -*-
import requests
import json

def print_banner():
    banner = """
============================================================
        Google Search Query Automator
          Powered by Google Custom Search API
============================================================
"""
    print(banner)

def google_search(api_key, cse_id, query, num_results=10):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        'key': api_key,
        'cx': cse_id,
        'q': query,
        'num': min(num_results, 10)
    }

    print("[INFO] Searching for: {}".format(query))
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            results = []
            for item in data.get("items", []):
                result = {
                    'title': item.get("title"),
                    'link': item.get("link"),
                    'snippet': item.get("snippet")
                }
                results.append(result)
            return results
        else:
            print("[ERROR] HTTP Error: {}".format(response.status_code))
            return []
    except Exception as e:
        print("[ERROR] Exception during search: {}".format(e))
        return []

def display_results(results):
    if not results:
        print("[INFO] No results found!")
        return

    print("\nSearch Results:")
    print("=" * 50)
    for idx, result in enumerate(results, start=1):
        title = result['title'].encode('utf-8', 'ignore')
        link = result['link']
        
        snippet = result['snippet'].encode('utf-8', 'ignore')

        print("[{}] {}".format(idx, title))
        print("    URL: {}".format(link))
        print("    Snippet: {}\n".format(snippet))

    print("=" * 50)

def main():
    print_banner()

    # Enter API Key and CSE ID
    api_key = "apikey_"  # Replace with your actual API Key
    cse_id = "cse_id"    # Replace with your actual CSE ID

    # Input search keywords and number of results
    query = raw_input("Enter your search query: ").strip()

    # Ensure the number of results is within the valid range
    while True:
        try:
            num_results = int(raw_input("Enter the number of results you want (1-10): "))
            if 1 <= num_results <= 10:
                break
            else:
                print("Please enter a number between 1 and 10.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    results = google_search(api_key, cse_id, query, num_results)
    display_results(results)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[INFO] Exiting...")
