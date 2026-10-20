# ShopSphere starter project

A small starter for an e-commerce application. Dockerfiles are intentionally not included.

## Contents
- `frontend/`: Vite-powered minimal frontend
- `backend/`: Flask API and MySQL connection
- `database/`: initial SQL schema and demo products
- `nginx/`: Nginx routing example

## Important notes
- The Nginx config expects a built frontend at `/usr/share/nginx/html` and a backend hostname `backend` reachable on port 5000. These names are typical when services share a container network; they are not automatically available when running everything directly on the host.
- The sample database credentials are for local development only. Use environment variables and a secrets manager for real deployments.
- The API currently supports listing products and a health endpoint. Authentication, checkout, orders, input validation, and production security still need to be implemented.

## Run the backend locally
1. Create a MySQL database/user and apply `database/init.sql` with a MySQL account allowed to create/use the database.
2. In a terminal:
   ```bash
   cd backend
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   export DB_HOST=127.0.0.1 DB_PORT=3306 DB_NAME=shopsphere DB_USER=shopsphere DB_PASSWORD='your-local-password'
   python app.py
   ```
3. Check `http://127.0.0.1:5000/health`.

## Run the frontend locally
1. Install Node.js and npm.
2. In another terminal:
   ```bash
   cd frontend
   npm install
   npm run dev
   ```
3. Vite's dev server runs on port 5173. To make `/api` work during local development, add a Vite proxy configuration or run Nginx with a reachable backend. The provided Nginx config is for a built/static deployment, not Vite's dev server.
