import falcon
from falcon.media.validators import jsonschema
from . import Resource, require_private_auth
from views.sign import sign_schema
import store.token
from config import web_url

@falcon.before(require_private_auth)
class Sign(Resource):
    @jsonschema.validate(sign_schema)
    def on_post(self, req: falcon.Request, res: falcon.Response):
        path = req.media["path"]
        method = req.media["method"]
        token = store.token.generate_priv(path, method)

        self.send_response(res, {
            "url": f"{web_url}/priv/{path}{'&' if '?' in path else '?'}signed_token={token}",
            "expires": store.token.EXPIRES_PRIV
        })