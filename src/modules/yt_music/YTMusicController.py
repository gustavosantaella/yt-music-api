from flask import Blueprint, request, Response
from ytmusicapi import YTMusic
import src.constants as c
bp = Blueprint(name="yt", url_prefix="/yt", import_name=__name__)
yt = YTMusic()

@bp.get("/home")
def home():
    return yt.get_home()


@bp.get("/search")
def search():
    query = request.args
    if "song" not in query:
        return Response("Bad request", 400)

        
    return yt.search(query['song'], limit=c.LIMIT_PER_PAGE)