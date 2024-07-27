# HOW TO USE THE ENDPOINT

- send post data to this url -> http://127.0.0.1:5000/authenticate_browser
- Request body should include (device_id, username, password)
- For successful login use, tomsmith as the username and SuperSecretPassword! as the password, device id can be any string.
- Finally the route returns a dummy access token and site_name as the payload.