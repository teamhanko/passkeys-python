# Adding Passkey Login to Python(Flask) and React app with Hanko

This repo shows how you can add passkey login with Hanko Passkey API to your Flask backend and React frontend.

## Clone the repo

```bash
git clone https://github.com/teamhanko/passkeys-python.git
```

## Add the environment variables

Add the following environment variables to `.env` file in the python-backend directory.

```sh
PASSKEYS_API_KEY=your-hanko-passkey-api-key
PASSKEYS_TENANT_ID=your-hanko-passkey-tenant-id
```


## Install Dependencies

To run your project, you need to install dependencies for both the frontend and the backend. This project uses `pnpm` as the package manager.

### Frontend

1. Navigate to the frontend directory:

```bash
cd react-frontend
```

2. Install the frontend dependencies:

```bash
pnpm install
```

3. Run the frontend
   

```bash
pnpm install
```

### Backend

1. Navigate to the backend directory:

```bash
cd python-backend
```

2. Install the backend dependencies:

```bash
pip install -r requirements.txt
```

3. Run the backend

``` bash
flask run
```
