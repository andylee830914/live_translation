import os
from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
from azure_translation import Captioning
import user_config_helper
import threading
import uuid

app = Flask(__name__)
socketio = SocketIO(app)
roomid = str(uuid.uuid4())

config = {
    "subscription_key": os.environ.get("AZURE_SPEECH_KEY"),
    "region": os.environ.get("AZURE_SPEECH_REGION"),
    "detect_languages": ["en-US", "zh-TW", "ja-JP"],
    "target_languages": ["zh-Hant", "en", "ja"],
    "captioning_mode": user_config_helper.CaptioningMode.REALTIME,
    "phrases": [],
    "socketio": "http://127.0.0.1:3000/",
    "roomid": roomid,
}

@app.route('/')
def display():
    language = request.args.get("language")
    if language is None:
        language = 'original'
    return render_template("index.html", language=language)
    
@app.route("/mobile")
def display_mobile():
    return render_template("mobile.html")

@app.route("/tv")
def display_tv():
    language = request.args.get("language")
    if language is None:
        language = 'original'
    return render_template("tv.html", language=language)


@socketio.on('connect')
def handle_message(data):
    print("connected")
    if len(config["target_languages"]) > 0:
        emit("available_languages", {"languages": ["Original"] + config["target_languages"]})
        emit("webcaption", {"language":"zh-TW","text":"字幕測試","translations":{"en":"subtitle test", "ja":"日本語テスト"}})
    else:
        emit("available_languages", {"languages": ["Original"]})
        emit("webcaption", {"language":"zh-TW","text":"字幕測試"})

@socketio.on(roomid)
def send_caption(data):
    emit("webcaption", data, broadcast=True)


def start_captioning():
    captioning = Captioning(config)
    if len(config["target_languages"]) > 0:
        captioning.translation_continuous_with_lid_from_microphone()
    else:
        captioning.transcription_continuous_with_lid_from_microphone()

if __name__ == '__main__':
    thread = threading.Thread(target=start_captioning)
    thread.start()
    socketio.run(app, host="0.0.0.0", port=3000)