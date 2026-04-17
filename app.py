from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def generation():

    if request.method == "POST":

        year = int(request.form["year"])

        if year >= 2010:
            gen = "Alpha"

        elif year >= 1997:
            gen = "Z"

        elif year >= 1981:
            gen = "Millennial"

        else:
            gen = "Older generation"

        return f"Siz: {gen} avlodisiz"

    return render_template("index.html")

app.run(debug=True)
