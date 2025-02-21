import os
from flask import Flask, render_template
import json

app = Flask(__name__)

if __name__ == "__main__":

    # make directory build if not exists
    if not os.path.exists("build"):
        os.mkdir("build")
    # output render_template("index.html") to index.html
    with app.app_context():
        with open('firebase_config.json') as json_data:
            d = json.load(json_data)
            with open("build/index.html", "w") as f:
                f.write(render_template("index.html", firebase_config=d, socket_endpoint=os.environ.get("SOCKET_ENDPOINT"), socket_path=os.environ.get("SOCKET_PATH")))
        # output render_template("mobile.html") to mobile.html
        
    # copy static css file to build
    if not os.path.exists("build/static"):
        os.mkdir("build/static")
    os.system("cp -r static/*.css build/static")