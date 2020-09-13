#
# from sanic import Sanic
# from sanic.response import json
# from sanic.request import Request
# from sanic_jwt_extended import (
#     JWTManager,
#     jwt_required,
#     create_access_token,
#     create_refresh_token,
# )
# import uuid
# from sanic_jwt_extended.tokens import Token
#
# app = Sanic("New Sanic App")
#
# # Setup the Sanic-JWT-Extended extension
# app.config["JWT_SECRET_KEY"] = "some-secret"
# JWTManager(app)
#
#
#
# @app.route("/login", methods=["POST"])
# async def login(request: Request):
#     if not request.json:
#         return json({"msg": "Missing JSON in request"}, status=400)
#
#     username = request.json.get("username", None)
#     password = request.json.get("password", None)
#     if not username:
#         return json({"msg": "Missing username parameter"}, status=400)
#     if not password:
#         return json({"msg": "Missing password parameter"}, status=400)
#
#     if username != "test" or password != "test":
#         return json({"msg": "Bad username or password"}, status=403)
#
#     # Identity can be any data that is json serializable
#     access_token = await create_access_token(identity=username, app=request.app)
#     refresh_token = await create_refresh_token(
#         identity=str(uuid.uuid4()), app=request.app
#     )
#     return json(
#         dict(access_token=access_token, refresh_token=refresh_token), status=200
#     )
#
#
#
#
# if __name__ == "__main__":
#     app.run()