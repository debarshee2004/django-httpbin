# Status Code App - HTTPBin-style Status Code and Redirect Endpoints

This app provides status code and redirect endpoints that mimic the behavior of httpbin.org's status code endpoints.

## Available Endpoints

### 1. Status Code
- **URL**: `/statuscode/status/{code}/`
- **Method**: GET
- **Description**: Responds with the given HTTP status code
- **Parameters**:
  - `code`: HTTP status code (100-599)
- **Response**: Returns status code details, headers, and request information
- **Example**: 
  ```bash
  # Return 200 OK
  curl "http://localhost:8000/statuscode/status/200/"
  
  # Return 404 Not Found
  curl "http://localhost:8000/statuscode/status/404/"
  
  # Return 500 Internal Server Error
  curl "http://localhost:8000/statuscode/status/500/"
  ```

### 2. Redirect
- **URL**: `/statuscode/redirect/{n}/`
- **Method**: GET
- **Description**: Redirects n times before returning a final response
- **Parameters**:
  - `n`: Number of redirects to perform
- **Response**: After n redirects, returns success message with redirect count
- **Example**: 
  ```bash
  # Redirect 3 times
  curl -L "http://localhost:8000/statuscode/redirect/3/"
  
  # Redirect 5 times
  curl -L "http://localhost:8000/statuscode/redirect/5/"
  ```

### 3. Redirect To
- **URL**: `/statuscode/redirect-to/`
- **Method**: GET
- **Description**: Redirects to a provided URL with optional status code
- **Query Parameters**:
  - `url`: Target URL to redirect to (required)
  - `status_code`: HTTP redirect status code (optional, defaults to 302)
- **Response**: Redirects to the specified URL
- **Example**: 
  ```bash
  # Redirect to Google with default 302 status
  curl -L "http://localhost:8000/statuscode/redirect-to/?url=https://google.com"
  
  # Redirect to example.com with 301 status
  curl -L "http://localhost:8000/statuscode/redirect-to/?url=https://example.com&status_code=301"
  ```

### 4. Deny
- **URL**: `/statuscode/deny/`
- **Method**: GET
- **Description**: Returns 403 Forbidden status
- **Response**: Returns access denied message with 403 status
- **Example**: 
  ```bash
  curl "http://localhost:8000/statuscode/deny/"
  ```

## Response Format

### Status Code Endpoint:
```json
{
  "code": 200,
  "description": "OK",
  "headers": {...},
  "url": "full_url",
  "origin": "client_ip"
}
```

### Redirect Endpoint (Final Response):
```json
{
  "message": "Redirected 3 times successfully",
  "final_url": "full_url",
  "total_redirects": 3,
  "headers": {...},
  "origin": "client_ip"
}
```

### Deny Endpoint:
```json
{
  "message": "Access Denied",
  "code": 403,
  "description": "Forbidden",
  "headers": {...},
  "url": "full_url",
  "origin": "client_ip"
}
```

## Supported Status Codes

The status code endpoint supports all standard HTTP status codes (100-599) with common descriptions:

- **2xx Success**: 200 (OK), 201 (Created), 202 (Accepted), 204 (No Content)
- **3xx Redirection**: 301 (Moved Permanently), 302 (Found), 304 (Not Modified), 307 (Temporary Redirect), 308 (Permanent Redirect)
- **4xx Client Errors**: 400 (Bad Request), 401 (Unauthorized), 403 (Forbidden), 404 (Not Found), 405 (Method Not Allowed), 408 (Request Timeout), 409 (Conflict), 429 (Too Many Requests)
- **5xx Server Errors**: 500 (Internal Server Error), 501 (Not Implemented), 502 (Bad Gateway), 503 (Service Unavailable), 504 (Gateway Timeout)

## Redirect Status Codes

The redirect-to endpoint supports these redirect status codes:
- **301**: Moved Permanently
- **302**: Found (default)
- **303**: See Other
- **307**: Temporary Redirect
- **308**: Permanent Redirect

## Features

- **No Database Storage**: All endpoints return data directly without storing anything
- **HTTPBin Compatibility**: Responses match the exact format and behavior of httpbin.org
- **Status Code Validation**: Ensures only valid HTTP status codes (100-599) are accepted
- **Redirect Counting**: Tracks redirect progress and provides final summary
- **Flexible Redirects**: Supports custom URLs and status codes for redirects
- **Header Extraction**: Returns all request headers in a standardized format
- **CSRF Exempt**: All endpoints are CSRF exempt for testing purposes

## Testing

You can test these endpoints using:
- cURL commands (examples provided above)
- Postman or similar API testing tools
- Browser developer tools
- Any HTTP client

### Testing Redirects with cURL:
```bash
# Follow redirects automatically
curl -L "http://localhost:8000/statuscode/redirect/3/"

# Don't follow redirects (see intermediate responses)
curl "http://localhost:8000/statuscode/redirect/3/"
```

## Notes

- All endpoints are CSRF exempt for testing purposes
- No data is stored in the database
- Responses mimic httpbin.org behavior exactly
- Redirect endpoints use Django's HttpResponseRedirect for proper HTTP redirects
- Status codes are validated to ensure they're within valid HTTP range
- The redirect endpoint automatically tracks progress using query parameters
