import requests
import hashlib

def check_email_breached(email):
    # Hash the email address using SHA-1
    hashed_email = hashlib.sha1(email.encode()).hexdigest().upper()
    
    # Take the first 5 characters of the hashed email to use as the API endpoint
    api_url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{hashed_email[:5]}"
    
    # Make the request to the API
    response = requests.get(api_url, headers={"User-Agent": "Python script"})
    
    # Check if the status code is 200 (OK)
    if response.status_code == 200:
        # If the email has been breached, return the breach details
        print("Your email has been breached. Here are the details:")
        print(response.text)
    elif response.status_code == 404:
        # If the email has not been breached, return a message indicating so
        print("Your email has not been breached. Stay safe!")
    else:
        # If an error occurs, print the status code
        print(f"An error occurred. Status code: {response.status_code}")

# Example usage:
email_to_check = input("Enter your email address to check if it has been breached: ")
check_email_breached(email_to_check)
