from flask import Flask, Blueprint
from src.modules.yt_music.YTMusicController import bp 

class Controller:
    
    def __init__(self, app: Flask, api: Blueprint) -> None:
        
        api.register_blueprint(bp)
        app.register_blueprint(api)
        
        
