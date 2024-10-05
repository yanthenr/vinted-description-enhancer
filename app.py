from flask import Flask, render_template, request
import threading
from waitress import serve
import webbrowser
from AutomaticTranslation import GenerateDescription

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def translate():

    if request.method == "POST":

        # Get form input
        input_description = request.form.get("input_description")
        input_tags = request.form.get("input_tags")
        input_language = request.form.get("input_language")
        target_languages = request.form.getlist("target_languages")
        # Generate description
        generated_description = GenerateDescription(input_description, input_tags, input_language, target_languages)

        return render_template(
            "index.html",
            input_description=input_description,
            input_tags = input_tags,
            input_language = input_language,
            target_languages = target_languages,
            generated_description = generated_description
        )

    return render_template(
        "index.html",
        target_languages = ["en", "nl", "fr", "es", "it", "de"],
        input_description = "Write your description here..."
    )

def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000/")

if __name__ == "__main__":
    threading.Timer(1, open_browser).start() 
    app.run()
