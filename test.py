import requests

# The raw GitHub URL for the word list
url = "https://githubusercontent.com"

# Fetch the data
response = requests.get(url)

if response.status_code == 200:
    # Split the long string by newlines to get individual words
    word_list = response.text.splitlines()
    print(f"Successfully loaded {len(word_list)} words!")
    print(f"First 5 words: {word_list[:5]}")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
