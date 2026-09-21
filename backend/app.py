from flask import Flask, request, render_template

app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        location = request.form.get("location")
        return location
    else:
        return "Failure"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)