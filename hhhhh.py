import requests
def get_data(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return f"Error: {response.status_code}"
    except requests.exceptions.RequestException as e:
            return f"Error: {e}"
space = get_data("https://api.github.com/")
print(space)

