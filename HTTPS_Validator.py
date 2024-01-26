import requests

def check_https_support(websites):
    for website in websites:
        url = f"https://{website}"
        try:
            response = requests.get(url, timeout=10, allow_redirects=True)
            if response.status_code == 200:
                print(f"{url} supports HTTPS")
            elif response.status_code == 301 or response.status_code == 302:
                # Follow redirects and check the final URL
                final_url = response.url
                print(f"{url} redirects to {final_url}")
                if final_url.startswith("https://"):
                    print(f"{final_url} supports HTTPS")
                else:
                    print(f"{final_url} does not fully support HTTPS")
            else:
                print(f"{url} returned status code {response.status_code}")
        except requests.ConnectionError:
            print(f"{url} could not establish a connection")

if __name__ == "__main__":
    # Add the websites you want to check in the list
    websites_to_check = ["example.com", "google.com", "github.com"]

    check_https_support(websites_to_check)
