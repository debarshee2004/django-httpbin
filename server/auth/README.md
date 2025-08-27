# Auth App - HTTPBin-style Authentication Endpoints

This app provides authentication endpoints that mimic the behavior of httpbin.org's authentication endpoints.

## Available Endpoints

### 1. Basic Authentication
- **URL**: `/auth/basic-auth/{username}/{password}/`
- **Method**: GET
- **Description**: Requires HTTP Basic Authentication with the specified username and password
- **Response**: Returns authentication details and request information
- **Example**: 
  ```bash
  curl -u "user:pass" "http://localhost:8000/auth/basic-auth/user/pass/"
  ```

### 2. Hidden Basic Authentication
- **URL**: `/auth/hidden-basic-auth/{username}/{password}/`
- **Method**: GET
- **Description**: Same as basic auth but returns 404 instead of 401 for unauthorized requests
- **Response**: Returns authentication details or 404 error
- **Example**:
  ```bash
  curl -u "user:pass" "http://localhost:8000/auth/hidden-basic-auth/user/pass/"
  ```

### 3. Bearer Token Authentication
- **URL**: `/auth/bearer/`
- **Method**: GET
- **Description**: Requires Bearer token in Authorization header
- **Response**: Returns token validation and request information
- **Example**:
  ```bash
  curl -H "Authorization: Bearer your-token-here" "http://localhost:8000/auth/bearer/"
  ```

### 4. Digest Authentication
- **URL**: `/auth/digest-auth/{qop}/{username}/{password}/{algo}/{stale_after}/`
- **Method**: GET
- **Description**: Implements HTTP Digest Authentication
- **Parameters**:
  - `qop`: Quality of Protection (auth, auth-int)
  - `username`: Username for authentication
  - `password`: Password for authentication
  - `algo`: Algorithm (MD5, SHA-256)
  - `stale_after`: Stale after timestamp
- **Response**: Returns authentication details or 401 with digest challenge
- **Example**:
  ```bash
  curl --digest -u "user:pass" "http://localhost:8000/auth/digest-auth/auth/user/pass/MD5/0/"
  ```

### 5. Token Validation
- **URL**: `/auth/validate-token/`
- **Method**: POST
- **Description**: Validates tokens from request body or Authorization header
- **Response**: Returns token validation results
- **Example**:
  ```bash
  curl -X POST -H "Content-Type: application/json" \
       -d '{"token": "your-token"}' \
       "http://localhost:8000/auth/validate-token/"
  ```

## Response Format

All endpoints return JSON responses with the following structure:

```json
{
  "authenticated": true,
  "user": "username",
  "method": "auth_method",
  "headers": {...},
  "url": "full_url",
  "origin": "client_ip",
  "args": {...}
}
```

## Authentication Headers

- **Basic Auth**: `Authorization: Basic base64(username:password)`
- **Bearer Token**: `Authorization: Bearer token`
- **Digest Auth**: `Authorization: Digest realm="HTTPBin", qop="auth", nonce="...", opaque="...", algorithm="MD5"`

## Testing

You can test these endpoints using:
- cURL commands
- Postman
- Browser developer tools
- Any HTTP client

## Notes

- All endpoints are CSRF exempt for testing purposes
- No data is stored in the database
- Responses mimic httpbin.org behavior exactly
- Digest authentication supports MD5 and SHA-256 algorithms
