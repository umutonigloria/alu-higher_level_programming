#!/usr/bin/python3
"""Import urllib library."""
import urllib.request
import base64  # Import base64 library for encoding credentials

"""fetch the url then."""
if __name__ == "__main__":
    # Define the URL and credentials (replace 'username' and 'password' with actual values)
    url = "https://intranet.hbtn.io/status"
    username = "your_username"
    password = "your_password"

    # Create a password manager to handle authentication
    password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None, url, username, password)
    handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
    opener = urllib.request.build_opener(handler)
    urllib.request.install_opener(opener)

    try:
        # Open the URL with authentication
        with urllib.request.urlopen(url) as response:
            html = response.read()
            print("Body response:")
            print("\t- type: {}".format(type(html)))
            print("\t- content: {}".format(html))
            print("\t- utf8 content: {}".format(html.decode("utf-8")))
    except urllib.error.HTTPError as e:
        # Handle HTTP errors, if any
        print(f"HTTP Error {e.code}: {e.reason}")

