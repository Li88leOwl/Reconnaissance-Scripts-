import requests

def check_https_support(websites):
    for website in websites:
        url = f"https://{website}"
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                print(f"{url} supports HTTPS")
            else:
                print(f"{url} returned status code {response.status_code}")
        except requests.ConnectionError:
            print(f"{url} does not support HTTPS")

if __name__ == "__main__":
    # Add the websites you want to check in the list
    websites_to_check = ["example.com", "google.com", "github.com"]

    check_https_support(websites_to_check)
