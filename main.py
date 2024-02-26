from flask import Flask, Blueprint
from src.controller import Controller

app = Flask(import_name=__name__, static_folder="./assets/public")


api = Blueprint(url_prefix="/api", name=__name__, import_name="api")

Controller(app, api)


def main():

    # yt = YTMusic()

    # print(yt.search("caramelos de cianuro"))
    app.run("127.0.0.1", 3000)
    print("running")


if __name__ == "__main__":
    main()
