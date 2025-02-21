# Build Client

- Prepare Firebase configuration in JSON format:

    ```json
    {
        "apiKey": "<YOUR_API_KEY>",
        "authDomain": "<YOUR_AUTH_DOMAIN>",
        "projectId": "<YOUR_PROJECT_ID>",
        "storageBucket": "<YOUR_STORAGE_BUCKET>",
        "messagingSenderId": "<YOUR_MESSAGING_SENDER_ID>",
        "appId": "<YOUR_APP_ID>",
        "measurementId": "<YOUR_MEASUREMENT_ID>"
    }
    

- Build the client :

    ```bash
    uv run --env-file=../.env python build.py
    ```
