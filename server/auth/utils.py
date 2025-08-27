import hashlib
import secrets


def generate_digest_challenge(realm="HTTPBin", qop="auth", algo="MD5"):
    """Generate digest authentication challenge"""
    nonce = secrets.token_hex(16)
    opaque = secrets.token_hex(16)

    challenge = (
        f'realm="{realm}", qop="{qop}", nonce="{nonce}", '
        f'opaque="{opaque}", algorithm="{algo}"'
    )
    return challenge, nonce, opaque


def validate_digest_response(username, password, method, uri, auth_dict):
    """Validate digest authentication response"""
    realm = auth_dict.get("realm", "HTTPBin")
    nonce = auth_dict.get("nonce")
    response = auth_dict.get("response")
    qop = auth_dict.get("qop")
    nc = auth_dict.get("nc")
    cnonce = auth_dict.get("cnonce")
    algorithm = auth_dict.get("algorithm", "MD5")

    if not all([nonce, response]):
        return False

    # Calculate expected response based on algorithm
    if algorithm.upper() == "MD5":
        ha1 = hashlib.md5(
            f"{username}:{realm}:{password}".encode()
        ).hexdigest()
        ha2 = hashlib.md5(f"{method}:{uri}".encode()).hexdigest()
    elif algorithm.upper() == "SHA-256":
        ha1 = hashlib.sha256(
            f"{username}:{realm}:{password}".encode()
        ).hexdigest()
        ha2 = hashlib.sha256(f"{method}:{uri}".encode()).hexdigest()
    else:
        # Default to MD5 for unsupported algorithms
        ha1 = hashlib.md5(
            f"{username}:{realm}:{password}".encode()
        ).hexdigest()
        ha2 = hashlib.md5(f"{method}:{uri}".encode()).hexdigest()

    if qop:
        expected = hashlib.md5(
            f"{ha1}:{nonce}:{nc}:{cnonce}:{qop}:{ha2}".encode()
        ).hexdigest()
    else:
        expected = hashlib.md5(f"{ha1}:{nonce}:{ha2}".encode()).hexdigest()

    return response == expected


def extract_request_headers(request):
    """Extract all headers from request"""
    headers = {}
    for key, value in request.META.items():
        if key.startswith("HTTP_"):
            header_name = key[5:].replace("_", "-").title()
            headers[header_name] = value
        elif key in ["CONTENT_TYPE", "CONTENT_LENGTH"]:
            header_name = key.replace("_", "-").title()
            headers[header_name] = value
    return headers
