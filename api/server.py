import falcon

import lib.errors
import lib.db
import lib.redis

from resources.info import InfoResource
import resources.clubs
import resources.validations
import resources.verifications
import resources.users
import resources.sign

def handle_base_errors(ex, req: falcon.Request, res: falcon.Response, params: any):
    raise falcon.HTTPError(ex.code, ex.message)

def my_serializer(req, resp, exception):
    representation = None

    preferred = req.client_prefers(('application/json',))
    
    e_dict = exception.to_dict()
    resp.media = {
        "error": e_dict.get('title', 'internal server error'),
        "description": e_dict.get('description', None)
    }
    resp.content_type = "application/json"


application = falcon.API()
application.add_route('/info', InfoResource())

application.add_route('/priv/clubs', resources.clubs.List())
application.add_route('/priv/clubs_by_guild/{guild_id}', resources.clubs.ByGuildId())
application.add_route('/priv/clubs_by_guild/{guild_id}/members', resources.clubs.ByGuildIdMemberList())

application.add_route('/clubs/{club_id}', resources.clubs.Public())

application.add_route('/priv/users_by_discord/{user_id}', resources.users.DiscordUser())

application.add_route('/priv/verifications', resources.verifications.Private())
application.add_route('/priv/sign', resources.sign.Sign())
application.add_route('/verifications/{token}', resources.verifications.User())
application.add_route('/validations/{token}', resources.validations.User())

application.add_error_handler(lib.errors.BaseError, handle_base_errors)
application.set_error_serializer(my_serializer)