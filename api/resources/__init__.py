import falcon
from config import api_secret
import store.token

class Resource(object):
    def send_response(self, res: falcon.Response, data: any = None, status: falcon.HTTPStatus = falcon.HTTP_OK) -> None:
        res.status = status
        res.media = {
            "data": data
        }

    def send_error(self, res: falcon.Response, error: str, status: falcon.HTTPStatus = falcon.HTTP_INTERNAL_SERVER_ERROR) -> None:
        res.status = status
        res.media = {
            'error': error
        }
        
    def send_404(req: falcon.Request, res: falcon.Response):
        res.status = falcon.HTTP_NOT_FOUND
        res.media = {
            'error': 'not found'
        }

def require_private_auth(req: falcon.Request, res: falcon.Response, resource: Resource, params):
    qs = falcon.uri.parse_query_string(req.query_string)
    if "signed_token" in qs:
        data = store.token.validate("priv", qs["signed_token"])
        if not data or data.get("mtd", "") != req.method or "/priv/" + data.get("pth", "") != req.path:
            raise falcon.HTTPUnauthorized('unauthorized')
    elif req.headers.get('AUTHORIZATION', '') != f'Bearer srv.{api_secret}':
        raise falcon.HTTPUnauthorized('unauthorized')