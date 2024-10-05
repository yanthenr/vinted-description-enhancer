from flask import Flask, render_template, request, make_response
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


if __name__ == "__main__":
    app.run(debug=True)
