from sanic_jwt import Initialize
from sanic.response import json
from sanic_jwt import exceptions
from sanic import Sanic

app = Sanic("JWT APP")

class User:

    def __init__(self, id, username, password):
        self.user_id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return "User(id='{}')".format(self.user_id)

    def to_dict(self):
        return {"user_id": self.user_id, "username": self.username}


users = [User(1, "user1", "abcxyz"), User(2, "user2", "abcxyz")]

username_table = {u.username: u for u in users}
userid_table = {u.user_id: u for u in users}


async def authenticate1(request):
    return dict(user_id='some_id')


async def authenticate(request, *args, **kwargs):
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    if not username or not password:
        raise exceptions.AuthenticationFailed("Missing username or password.")

    user = username_table.get(username, None)
    if user is None:
        raise exceptions.AuthenticationFailed("User not found.")

    if password != user.password:
        raise exceptions.AuthenticationFailed("Password is incorrect.")

    return user

@app.route("/login", methods=["POST"])
async def login(request):
    user = authenticate(request)
    if not request.json:
        return json({"msg": "Missing JSON in request"}, status=400)

    res = {}
    arr = request.json
    # res = map(lambda j: res[j.get("name", None)] = j.get("strVal", "boolVal"), arr)

    for j in arr:
        res[j.get("name", None)] = j.get("strVal", "boolVal")
    return json(res)


Initialize(app, authenticate=authenticate)


if __name__ == "__main__":

    app.run(host="0.0.0.0", port=8000)






