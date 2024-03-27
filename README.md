# Integrating Passkey Authentication in a Python Flask App

This repository demonstrates how to add passkey login functionality to your Flask backend and React frontend using the Hanko Passkey API. Passkey authentication is a secure and user-friendly alternative to traditional password-based authentication, providing a seamless login experience for users.

![Passkey demo](/passkey.gif)

## Prerequisites

Before you begin, ensure you have the following:

- Python installed (version 3.0.0 or later)
- Node.js installed (version 20.0.0 or later)
- Hanko Passkey API key and tenant ID from [Hanko Cloud](https://cloud.hanko.io/)

> **Note:**
> You'll need to create a Passkey Project on Hanko Cloud with the App URL `http://localhost:5173`. See our docs to learn how to setup a [passkey project](https://hanko.mintlify.app/passkey-api/setup-passkey-project).

## Getting Started

1. Clone the repository

```bash
git clone https://github.com/teamhanko/passkeys-python.git
```

2. Set up environment variables

Create a `.env` file in the `python-backend` directory and add the following environment variables:

```sh
PASSKEY_API_KEY=your-hanko-passkey-api-key
PASSKEY_TENANT_ID=your-hanko-passkey-tenant-id
```

Replace `your-hanko-passkey-api-key` and `your-hanko-passkey-tenant-id` with your actual Hanko Passkey API key and tenant ID.

#### Frontend

1. Navigate to the frontend directory:

```bash
cd react-frontend
```

2. Install the frontend dependencies using your preferred package manager (e.g., `npm`, `pnpm`, `yarn`, or `bun`). For this project, we've used `pnpm`:

```bash
pnpm install
```

3. Start the frontend development server:

```bash
pnpm dev
```

#### Backend

1. Navigate to the backend directory:

```bash
cd python-backend
```

2. Install the backend dependencies using `pip`:

```bash
pip install -r requirements.txt
```

3. Start the backend server:

```bash
flask run --port=8000
```

## Usage

1. Start the application:
   
   * Ensure that both the frontend and backend servers are running.

   * Access the application by navigating to http://localhost:5173 in your web browser.
  
2. Log in with a pre-configured user: Navigate to login page, login with one of the pre-configured users.

```json
    {
        "id": "b3fbbdbd-6bb5-4558-9055-3b54a9469629",
        "email": "john.doe@example.com",
        "password": "password123",
    },
    {
        "id": "22c81b3d-1e7d-4a72-a6b0-ad946e0c0965",
        "email": "sergio_mq@example.com",
        "password": "very_secure_password",
    },
    {
        "id": "55c81b3d-1e7d-4a72-a6b0-ad946e0c0965",
        "email": "ab@g.com",
        "password": "123",
    }
```

3. Register a passkey:
   
   * After logging in, register a passkey for the logged-in user.


4. Log out:
   * After the passkey registration is successful, log out of the application.

5. Login with with a passkey

   * On the login page, choose sign in with a passkey option to authenticate using a passkey.

## Support

Feel free to reach out to us on [Discord](https://hanko.io/community) if you get into any issues.

## License

This project is licensed under the MIT License.
