from werkzeug.wrappers.response import Response as Res
import json, typing
from http import HTTPStatus
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
