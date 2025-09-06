# Django REST Framework Demo API

A comprehensive demonstration project showcasing the power and flexibility of Django REST Framework (DRF) through a collection of HTTP testing endpoints similar to httpbin.org. This project serves as both a learning resource and a testing utility for understanding HTTP protocols, REST API patterns, and Django REST Framework capabilities.

## 📚 Table of Contents

- [Overview](#overview)
- [Project Architecture](#project-architecture)
- [Django REST Framework Deep Dive](#django-rest-framework-deep-dive)
- [Application Modules](#application-modules)
- [API Endpoints](#api-endpoints)
- [Advanced Features](#advanced-features)
- [Setup and Installation](#setup-and-installation)
- [Contributing](#contributing)

## 🎯 Overview

This project demonstrates various HTTP concepts and Django REST Framework patterns through practical, testable endpoints. It's designed to help developers understand:

- **HTTP Methods**: GET, POST, PUT, DELETE, PATCH operations
- **Status Codes**: Understanding different HTTP response codes
- **Authentication**: Basic, Bearer, and Digest authentication schemes
- **Data Formats**: JSON, XML, HTML, and binary responses
- **Headers & Cookies**: HTTP header manipulation and cookie handling
- **Streaming**: Real-time data streaming and large file handling
- **Compression**: GZIP and deflate compression techniques
- **Caching**: HTTP caching strategies and cache control

## 🏗️ Project Architecture

### Directory Structure

```
django-rest-framework/
├── pyproject.toml              # UV project configuration and dependencies
├── requirements.txt            # Python dependencies (legacy support)
├── uv.lock                    # UV lock file for reproducible builds
├── README.md                  # This file
└── server/                    # Django project root
    ├── manage.py              # Django management script
    ├── db.sqlite3             # SQLite database
    ├── server/                # Main Django configuration
    │   ├── __init__.py
    │   ├── settings.py        # Django settings and DRF configuration
    │   ├── urls.py           # Root URL configuration
    │   ├── wsgi.py           # WSGI application entry point
    │   └── asgi.py           # ASGI application entry point
    ├── api/                   # Core API endpoints
    ├── auth/                  # Authentication demonstrations
    ├── cookies/               # Cookie handling endpoints
    ├── http_methods/          # HTTP method demonstrations
    ├── inspection/            # Request inspection utilities
    └── statuscode/            # HTTP status code testing
```

### Technology Stack

- **Django 5.2.4**: Modern Python web framework
- **Django REST Framework 3.16.0**: Powerful toolkit for building Web APIs
- **drf-yasg 1.21.10**: Automatic Swagger/OpenAPI documentation generation
- **djangorestframework-simplejwt 5.5.1**: JWT authentication for DRF
- **Python 3.12+**: Latest Python features and performance improvements

## 🚀 Django REST Framework Deep Dive

### What is Django REST Framework?

Django REST Framework (DRF) is a powerful and flexible toolkit for building Web APIs in Django. It provides:

1. **Serialization**: Converting complex data types (Django models, querysets) to native Python datatypes that can be easily rendered into JSON, XML, or other content types.

2. **Authentication & Permissions**: Built-in authentication schemes (Session, Token, JWT) and fine-grained permission systems.

3. **ViewSets & Routers**: High-level abstractions for handling CRUD operations with automatic URL routing.

4. **Content Negotiation**: Automatic handling of different content types and formats based on client requests.

5. **Browsable API**: Interactive web-based API explorer for testing and documentation.

### Core DRF Concepts Demonstrated

#### 1. **APIView vs Function-Based Views**

The project demonstrates both approaches:

**Function-Based Views** (in `api/views.py`):

```python
@api_view(["GET"])
def home(request):
    return Response({"message": "Welcome to the API!"}, status=status.HTTP_200_OK)
```

**Class-Based APIViews** (throughout other modules):

```python
class GetView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({...})
```

#### 2. **Serializers and Data Validation**

While not extensively used in this demo project (as it focuses on HTTP testing), the `auth` module demonstrates serializer usage:

```python
class TokenValidationSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=500)
    secret = serializers.CharField(max_length=100)
```

#### 3. **Authentication Classes**

The project implements custom authentication classes mimicking httpbin.org behavior:

- **HTTPBinBasicAuthentication**: HTTP Basic Auth
- **HTTPBinBearerAuthentication**: Bearer Token Auth
- **HTTPBinDigestAuthentication**: HTTP Digest Auth

#### 4. **Content Negotiation**

Different content types are handled across endpoints:

- JSON responses (default)
- XML responses (`api/xml/`)
- HTML responses (`api/html/`)
- Binary data (`api/bytes/`, `api/gzip/`)
- Streaming responses (`api/stream/`, `api/drip/`)

#### 5. **Status Code Handling**

The `statuscode` module demonstrates proper HTTP status code usage and custom error responses.

## 📱 Application Modules

### 1. **API Module** (`api/`)

Core functionality and utility endpoints:

- **Home & Health**: Basic API status endpoints
- **Data Formats**: JSON, XML, HTML, UTF-8 content
- **Binary Data**: Byte streams, compression (GZIP/deflate)
- **Streaming**: Real-time data streaming with customizable parameters
- **Caching**: HTTP cache control demonstrations
- **Utilities**: Base64 encoding/decoding, robots.txt

### 2. **HTTP Methods Module** (`http_methods/`)

Comprehensive HTTP method demonstrations:

- **GET**: Query parameter handling and header inspection
- **POST**: Form data and JSON body processing
- **PUT**: Resource replacement operations
- **PATCH**: Partial resource updates
- **DELETE**: Resource deletion with confirmation
- **OPTIONS**: CORS preflight and method discovery

### 3. **Authentication Module** (`auth/`)

Security and authentication patterns:

- **Basic Authentication**: Username/password verification
- **Bearer Token**: JWT and token-based authentication
- **Digest Authentication**: MD5-based challenge-response
- **Token Validation**: Custom token verification logic

### 4. **Status Code Module** (`statuscode/`)

HTTP status code testing and understanding:

- **Custom Status Codes**: Return any HTTP status code (100-599)
- **Redirect Handling**: Various redirect scenarios
- **Error Simulation**: Client and server error conditions
- **Status Descriptions**: Human-readable status explanations

### 5. **Inspection Module** (`inspection/`)

Request analysis and debugging:

- **Header Inspection**: Complete request header analysis
- **IP Detection**: Client IP address identification
- **User Agent**: Browser and client identification
- **UUID Generation**: Unique identifier creation

### 6. **Cookies Module** (`cookies/`)

HTTP cookie manipulation:

- **Cookie Reading**: Retrieve all request cookies
- **Cookie Setting**: Dynamic cookie creation
- **Cookie Deletion**: Cookie removal operations

## 🔗 API Endpoints

### Core API Endpoints (`/api/`)

| Endpoint                | Method | Description                    |
| ----------------------- | ------ | ------------------------------ |
| `/api/`                 | GET    | Welcome message and API status |
| `/api/health/`          | GET    | Health check endpoint          |
| `/api/json/`            | GET    | JSON response example          |
| `/api/xml/`             | GET    | XML formatted response         |
| `/api/html/`            | GET    | HTML content response          |
| `/api/encoding/utf8/`   | GET    | UTF-8 encoded content          |
| `/api/bytes/{n}/`       | GET    | Random binary data (n bytes)   |
| `/api/drip/`            | GET    | Streaming data with delays     |
| `/api/delay/{seconds}/` | GET    | Delayed response simulation    |
| `/api/stream/{lines}/`  | GET    | JSON streaming (n lines)       |
| `/api/gzip/`            | GET    | GZIP compressed response       |
| `/api/deflate/`         | GET    | Deflate compressed response    |
| `/api/base64/{value}/`  | GET    | Base64 decoding                |
| `/api/cache/`           | GET    | Cache control demonstration    |

### HTTP Methods (`/http_methods/`)

| Endpoint                  | Methods | Description                 |
| ------------------------- | ------- | --------------------------- |
| `/http_methods/get/`      | GET     | GET request analysis        |
| `/http_methods/post/`     | POST    | POST data processing        |
| `/http_methods/put/`      | PUT     | PUT request handling        |
| `/http_methods/patch/`    | PATCH   | PATCH request processing    |
| `/http_methods/delete/`   | DELETE  | DELETE request confirmation |
| `/http_methods/anything/` | ALL     | Accepts any HTTP method     |

### Authentication (`/auth/`)

| Endpoint                           | Method | Description                 |
| ---------------------------------- | ------ | --------------------------- |
| `/auth/basic-auth/{user}/{pass}/`  | GET    | HTTP Basic Authentication   |
| `/auth/bearer/`                    | GET    | Bearer token authentication |
| `/auth/digest-auth/{user}/{pass}/` | GET    | HTTP Digest Authentication  |
| `/auth/validate-token/`            | POST   | Custom token validation     |

### Status Codes (`/statuscode/`)

| Endpoint                     | Method | Description                 |
| ---------------------------- | ------ | --------------------------- |
| `/statuscode/status/{code}/` | GET    | Return specific HTTP status |
| `/statuscode/redirect/{n}/`  | GET    | Redirect n times            |
| `/statuscode/random-status/` | GET    | Random status code          |

### Inspection (`/inspection/`)

| Endpoint                  | Method | Description              |
| ------------------------- | ------ | ------------------------ |
| `/inspection/headers/`    | GET    | Request headers analysis |
| `/inspection/ip/`         | GET    | Client IP address        |
| `/inspection/user-agent/` | GET    | User agent information   |
| `/inspection/uuid/`       | GET    | Generate UUID            |

### Cookies (`/cookies/`)

| Endpoint           | Method | Description                  |
| ------------------ | ------ | ---------------------------- |
| `/cookies/`        | GET    | Display all cookies          |
| `/cookies/set/`    | GET    | Set cookies via query params |
| `/cookies/delete/` | GET    | Delete specified cookies     |

## 🔧 Advanced Features

### 1. **Swagger/OpenAPI Documentation**

The project includes automatic API documentation via drf-yasg:

- **Swagger UI**: Interactive API explorer at `/swagger/`
- **ReDoc**: Clean documentation at `/redoc/`
- **OpenAPI Schema**: Machine-readable API specification

Every endpoint is decorated with `@swagger_auto_schema` providing:

- Parameter descriptions
- Response schemas
- Example requests/responses
- Authentication requirements

### 2. **CSRF Protection Handling**

The project demonstrates proper CSRF handling in DRF:

```python
@method_decorator(csrf_exempt, name="dispatch")
class SomeView(APIView):
    # CSRF exemption for API endpoints
```

### 3. **Custom Authentication Classes**

Implementation of httpbin.org-style authentication:

```python
class HTTPBinBasicAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.META.get('HTTP_AUTHORIZATION')
        if not auth_header or not auth_header.startswith('Basic '):
            return None
        # ... authentication logic
```

### 4. **Streaming Responses**

Demonstrates large data handling and real-time streaming:

```python
def drip_view(request):
    def generator():
        for _ in range(numbytes):
            time.sleep(interval)
            yield b"*"
    return StreamingHttpResponse(generator())
```

### 5. **Content Compression**

Shows how to handle different compression algorithms:

- GZIP compression for bandwidth optimization
- Deflate compression for alternative compression needs
- Binary data handling for file transfers

## 🚀 Setup and Installation

### Prerequisites

- Python 3.12 or higher
- UV (recommended) or pip for dependency management
- Git for version control

### Installation with UV (Recommended)

UV is a fast Python package installer and resolver, written in Rust. It's designed to be a drop-in replacement for pip and pip-tools.

1. **Install UV** (if not already installed):

   ```powershell
   # On Windows
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

   # Or via pip
   pip install uv
   ```

2. **Clone the repository**:

   ```powershell
   git clone https://github.com/debarshee2004/django-rest-framework.git
   cd django-rest-framework
   ```

3. **Create and activate virtual environment with UV**:

   ```powershell
   # UV automatically manages virtual environments
   uv venv

   # Activate the virtual environment
   .venv\Scripts\Activate.ps1  # Windows PowerShell
   # or
   .venv\Scripts\activate.bat  # Windows Command Prompt
   ```

4. **Install dependencies**:

   ```powershell
   # UV will automatically create a virtual environment and install dependencies
   uv pip install -r requirements.txt

   # Or install from pyproject.toml
   uv pip install -e .
   ```

5. **Navigate to server directory and run migrations**:

   ```powershell
   cd server
   python manage.py migrate
   ```

6. **Create a superuser** (optional):

   ```powershell
   python manage.py createsuperuser
   ```

7. **Start the development server**:
   ```powershell
   python manage.py runserver
   ```

### Installation with pip (Alternative)

If you prefer using traditional pip:

1. **Clone and navigate**:

   ```powershell
   git clone https://github.com/debarshee2004/django-rest-framework.git
   cd django-rest-framework
   ```

2. **Create virtual environment**:

   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

3. **Install dependencies**:

   ```powershell
   pip install -r requirements.txt
   ```

4. **Setup Django**:
   ```powershell
   cd server
   python manage.py migrate
   python manage.py runserver
   ```

### Accessing the API

Once the server is running, you can access:

- **API Base**: http://localhost:8000/api/
- **Swagger Documentation**: http://localhost:8000/swagger/
- **ReDoc Documentation**: http://localhost:8000/redoc/
- **Django Admin**: http://localhost:8000/admin/ (if superuser created)

### Testing the API

You can test the API using various tools:

1. **Swagger UI**: Interactive testing at `/swagger/`
2. **curl**: Command-line testing
   ```bash
   curl http://localhost:8000/api/json/
   ```
3. **Postman**: Import OpenAPI spec from `/swagger/?format=openapi`
4. **httpie**: Human-friendly command-line tool
   ```bash
   http GET localhost:8000/api/json/
   ```

## 🤝 Contributing

Contributions are welcome! This project is designed to be educational, so improvements that enhance learning are particularly appreciated:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Make your changes**: Follow Django and DRF best practices
4. **Add tests**: Ensure your changes are tested
5. **Update documentation**: Keep README and docstrings current
6. **Commit changes**: `git commit -m 'Add amazing feature'`
7. **Push to branch**: `git push origin feature/amazing-feature`
8. **Open a Pull Request**: Describe your changes and their benefits

### Areas for Contribution

- Additional HTTP testing endpoints
- More authentication methods
- Performance optimizations
- Better error handling
- Enhanced documentation
- Test coverage improvements
- Docker configuration
- Example client implementations

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Inspired by [httpbin.org](https://httpbin.org/) - A simple HTTP request & response service
- Django REST Framework community for excellent documentation
- All contributors who help improve this educational resource

---

**Happy coding!** 🚀 This project demonstrates the power and flexibility of Django REST Framework while providing practical examples for HTTP protocol understanding.
