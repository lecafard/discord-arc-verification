discord verification bot
========================

https://arc-verification.unswsecurity.com


## Hosting instructions
1. Get a Mailgun API key (required for sending email, note: costs a small amount of money) and a Discord
bot key.
2. Using the exampledotenv file as a template, create a prod.env file with all the required details.
3. Use docker-compose 1.25 or above to run the stack. Command: `docker-compose --env-file prod.env up -p vbot -d`
4. Manually migrate using `./scripts/migrate.sh` because I haven't gotten around to doing that yet. Use
`docker inspect vbot_postgres_1` to get the IP address of the docker container. Then run
`DBHOST=<ip address> DBPASS=<POSTGRES_ROOT_PASSWORD inside prod.env> ./scripts/migrate.sh` to perform the
migration.
5. Restart the API service by running `docker-compose --env-file app.env up api -d` otherwise it won't
connect to a non-existent database.

## Notes
- This bot was designed to be able to service multiple clubs on multiple servers, but is currently only
being used by the UNSW Security Society.
- Still working on a more granular security model, but it should be fine for now.

## Discord configuration instructions
1. Enable developer mode on discord. Right click on your username on the bottom left and go into 
User Settings > Appearance > Developer Mode.
2. Modify the `scripts/club-template.json` file to your liking.
3. Run `curl -X POST -H "Content-Type: application/json" -d scripts/club-template.json" https://server_address/priv/clubs` to create the club.
4. Add the bot to your server by following the instructions on the Discord developer page.
5. A user with administrator permissions needs to run `$avsetadmin` on a channel which only moderators
are allowed to access.
6. From that channel, they will then need to run `$avsetverified @mention-the-role` to set the role for
verified users.

## Features
TODO

## TODO
- Automatic deletion if user doesn't verify within an hour
- More robust authentication between services.
