# Login-Automation

This is a Python-based API project designed to automate the login process for a mobile application. The API will simulate user interactions and handles session registration, browser authentication, and authorization token retrieval, providing a seamless and automated way to authenticate users.

## Features

- **Session Registration**
- **Browser Authentication**
- **Authorization Token Retrieval**

### 1. Session Registration Route Testing.

- You can test this by sending a POST request to http://localhost:5000/register_session with the required JSON body.

Example JSON request body for testing:

```json
{
  "device_id": "abcdefg"
}
```

For a successful request, the following will be a response

```json
{
  "message": "Session registered successfully",
  "user_id": 101
}
```

`NB` : Don't forget to copy `API_URI` and `SECRET_KEY` variables from `.env.example` file to your `.env` file.

## Contributing

Contributions are welcome! Please follow these guidelines:

- **Branching:** Always create a new branch from the `develop` branch for your feature.
- **Pull Requests:** Submit a pull request to merge your changes into the `develop` branch. Ensure your pull request includes a detailed description of the changes.
- **No Direct Pushes to Master:** Do not push directly to the `master` branch. All changes must be reviewed and approved via pull requests to the `develop` branch.

# Communication

- **Use GitHub issues to discuss tasks and track progress.**
