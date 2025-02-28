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

    # Log server errors
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