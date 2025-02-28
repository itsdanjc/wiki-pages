from flask import current_app, request
from werkzeug.wrappers.response import Response as Res
from werkzeug.http import HTTP_STATUS_CODES
import json, typing
from http import HTTPStatus
from datetime import datetime, timezone

class Response(Res):
    """This response object is similar to Flask's default but designed for API responses.  
     
    It wraps `werkzeug.wrappers.response.Response` with the mimetype `application/json` set.  
     
    As a general rule, API requests should use `api.response.make_response()`  
    to generate responses.
    """

    def __init__(
        self,
        response: object,
        status: int | str | HTTPStatus | None = None,
        headers: typing.Mapping[str, str | typing.Iterable[str]]
            | typing.Iterable[tuple[str, str]]
            | None = None,
        direct_passthrough: bool = False,
        sort_keys: bool = True
    ) -> None:
        
        if response is None:
            raise TypeError(f"{type(response).__name__} not json sterilizable.")
        
        response = json.dumps(
            response, 
            sort_keys = sort_keys, 
            ensure_ascii = True
        )
        
        super().__init__(
            response = response,
            status = status,
            headers = headers,
            content_type = "application/json",
            direct_passthrough = direct_passthrough
        )

def handle_error(exc: Exception) -> Response:
    """Handles API errors by returning a JSON response with appropriate status codes.
    
    Designed for `Flask.register_error_handler()`

    Logs exceptions for server errors (5xx).
    """
    status_code = getattr(exc, "code", 500)
    timestamp_now = datetime.now(tz=timezone.utc)

    current_app.logger.info(f'\"{request.method} {request.path}\" - {status_code}')
    if status_code >= 500:
        current_app.log_exception(exc)

    return Response(
        response = {
            "request_url": request.url,
            "status": status_code,
            "message": HTTP_STATUS_CODES.get(status_code, "Unknown Error"),
            "timestamp": timestamp_now.isoformat(),
        },
        headers = {
            "Cache-Control": "no-store, no-cache, must-revalidate, proxy-revalidate",
            "Pragma": "no-cache",
            "Referrer-Policy": "no-referrer"
        },
        status = status_code
    )

def make_response(
        message: str, 
        status: int | str | HTTPStatus, 
        headers: dict | None = None, 
        **content
) -> Response:
    """Construct a standardized JSON response for API endpoints.

    This function serializes your response message and any additional content into JSON format, 
    automatically appending a UTC timestamp. It also sets the HTTP status code and allows for custom headers:

        def my_route():
            return make_response('success', 200)

    Customize headers and include extra data by passing a headers dictionary and additional keyword arguments:

        def my_route():
            return make_response(
                'success',
                200,
                headers={"Cache-Control": "no-cache"},
                details="Upload file successfully"
            )
    """
    timestamp_now = datetime.now(tz=timezone.utc)
    current_app.logger.info(f'\"{request.method} {request.path}\" - {status}')
    default = {
        "Cache-Control": "public, max-age=3600, must-revalidate",
        "Referrer-Policy": "strict-origin-when-cross-origin"
    }

    if headers:
        default.update(headers)

    return Response(
        response = {
            "status": status,
            "message": message,
            "timestamp": timestamp_now.isoformat(),
            **content
        },
        headers = default,
        status = status
    )