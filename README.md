# Integrating Passkey Authentication in a Python Flask App

This repository demonstrates how to add passkey login functionality to your Flask backend and React frontend using the Hanko Passkey API. Passkey authentication is a secure and user-friendly alternative to traditional password-based authentication, providing a seamless login experience for users.


## Prerequisites

Before you begin, ensure you have the following:

* Python installed (version 3.0.0 or later)
* Node.js installed (version 20.0.0 or later)
* Hanko Passkey API key and tenant ID from [Hanko Cloud](https://cloud.hanko.io/)

## Getting Started

1. Clone the Repository

```bash
git clone https://github.com/teamhanko/passkeys-python.git
```

2. Set Up Environment Variables

Create a `.env` file in the `python-backend` directory and add the following environment variables:

```sh
PASSKEYS_API_KEY=your-hanko-passkey-api-key
PASSKEYS_TENANT_ID=your-hanko-passkey-tenant-id
```

Replace `your-hanko-passkey-api-key` and `your-hanko-passkey-tenant-id` with your actual Hanko Passkey API key and tenant ID.


3. Install Dependencies

#### Frontend

1. Navigate to the frontend directory:

```bash
cd react-frontend
```

2. Install the frontend dependencies using `pnpm`:

```bash
pnpm install
```

3. Start the frontend development server:

```bash
pnpm start
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
flask run
```

## Usage

Once the frontend and backend servers are running, you can access the application by navigating to `http://localhost:5173` in your browser. The application will guide you through the passkey authentication process, allowing you to securely log in and access protected routes.

## Support

Feel free to reach out to us on [Discord](https://hanko.io/community) if you get into any issues.

## License

This project is licensed under the MIT License.


