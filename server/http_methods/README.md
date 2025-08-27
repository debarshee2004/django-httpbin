# HTTP Methods App - HTTPBin-style Request Method Endpoints

This app provides HTTP method endpoints that mimic the behavior of httpbin.org's request method endpoints.

## Available Endpoints

### 1. GET Method
- **URL**: `/http_methods/get/`
- **Method**: GET
- **Description**: Returns request data for GET requests
- **Response**: Returns query parameters, headers, origin IP, and URL
- **Example**: 
  ```bash
  curl "http://localhost:8000/http_methods/get/?param1=value1&param2=value2"
  ```

### 2. POST Method
- **URL**: `/http_methods/post/`
- **Method**: POST
- **Description**: Returns posted data for POST requests
- **Response**: Returns query parameters, form data, files, JSON data, headers, origin IP, and URL
- **Example**: 
  ```bash
  curl -X POST -H "Content-Type: application/json" \
       -d '{"key": "value"}' \
       "http://localhost:8000/http_methods/post/"
  ```

### 3. PUT Method
- **URL**: `/http_methods/put/`
- **Method**: PUT
- **Description**: Returns PUT data for PUT requests
- **Response**: Returns query parameters, form data, files, JSON data, headers, origin IP, and URL
- **Example**: 
  ```bash
  curl -X PUT -H "Content-Type: application/json" \
       -d '{"key": "value"}' \
       "http://localhost:8000/http_methods/put/"
  ```

### 4. PATCH Method
- **URL**: `/http_methods/patch/`
- **Method**: PATCH
- **Description**: Returns PATCH data for PATCH requests
- **Response**: Returns query parameters, form data, files, JSON data, headers, origin IP, and URL
- **Example**: 
  ```bash
  curl -X PATCH -H "Content-Type: application/json" \
       -d '{"key": "value"}' \
       "http://localhost:8000/http_methods/patch/"
  ```

### 5. DELETE Method
- **URL**: `/http_methods/delete/`
- **Method**: DELETE
- **Description**: Returns request data for DELETE requests
- **Response**: Returns query parameters, headers, origin IP, and URL
- **Example**: 
  ```bash
  curl -X DELETE "http://localhost:8000/http_methods/delete/?param1=value1"
  ```



## Response Format

### GET, DELETE Methods:
```json
{
  "args": {"query_parameters": "values"},
  "headers": {...},
  "origin": "client_ip",
  "url": "full_url",
  "method": "HTTP_METHOD"
}
```

### POST, PUT, PATCH Methods:
```json
{
  "args": {"query_parameters": "values"},
  "data": "raw_data",
  "files": {"file_data": "..."},
  "form": {"form_data": "..."},
  "headers": {...},
  "json": {"parsed_json": "..."},
  "origin": "client_ip",
  "url": "full_url",
  "method": "HTTP_METHOD"
}
```



## Features

- **No Database Storage**: All endpoints return data directly without storing anything
- **HTTPBin Compatibility**: Responses match the exact format and behavior of httpbin.org
- **Method-Specific Data**: Each method returns appropriate data (e.g., form data for POST/PUT/PATCH)
- **Query Parameter Support**: All endpoints accept and return query parameters
- **Header Extraction**: Returns all request headers in a standardized format
- **CSRF Exempt**: All endpoints are CSRF exempt for testing purposes
- **File Upload Support**: POST, PUT, and PATCH methods handle file uploads
- **JSON Parsing**: Automatically parses JSON content when Content-Type is application/json

## Testing

You can test these endpoints using:
- cURL commands (examples provided above)
- Postman or similar API testing tools
- Browser developer tools
- Any HTTP client

## Notes

- All endpoints are CSRF exempt for testing purposes
- No data is stored in the database
- Responses mimic httpbin.org behavior exactly
- File uploads are supported for POST, PUT, and PATCH methods
- JSON data is automatically parsed when the correct Content-Type header is set
