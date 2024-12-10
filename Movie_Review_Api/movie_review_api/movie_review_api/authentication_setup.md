# Authentication Setup for Movie Review API

## Overview
The API uses JWT-based authentication to secure endpoints. Users must authenticate to access protected resources.

---

## Setup Steps

1. **Install Dependencies**:
   - `djangorestframework`
   - `djangorestframework-simplejwt`

2. **Enable JWT Authentication**:
   - Add `rest_framework` and `rest_framework_simplejwt` to `INSTALLED_APPS`.
   - Configure `DEFAULT_AUTHENTICATION_CLASSES` in `settings.py`.

3. **Add JWT Token Endpoints**:
   - `POST /api/token/`: Obtain an access and refresh token.
   - `POST /api/token/refresh/`: Refresh the access token.

---

## Testing the Authentication

### Obtain a JWT Token
Send a `POST` request to `/api/token/` with the username and password:
```bash
curl -X POST http://127.0.0.1:8000/api/token/ \
-H "Content-Type: application/json" \
-d '{"username": "yourusername", "password": "yourpassword"}'
