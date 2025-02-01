import google.generativeai as genai
from flask import Flask, render_template, request

genai.configure(api_key="AIzaSyBtynYSn0v065Kias0pDAg0hg_8MuvBD2o")
model = genai.GenerativeModel("gemini-1.5-flash")

flask_app = Flask(__name__)


@flask_app.route("/", methods=["GET", "POST"])
def ai_roadmap():
    if request.method == "POST":
        car = request.form["car"]
        price = request.form["price"]
        response = model.generate_content(f" give me cars sold in indian market of brand {car} for  {price} price in rupees.\
                                            Return response in HTML format,\
                                          use Table tags for the same,\
                                          you can use bootstrap classes for styling")

        resp = response.text[7:]
        resp = resp[:-4]
        return render_template("ai_roadmap.html", roadmap=resp)
    return render_template("user_input.html")


if __name__ == "__main__":
    flask_app.run(debug=True)
