from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/vypocet", methods=["POST"])
def vypocet():
    data = request.json
    tvar = data.get("tvar")
    jednotky = data.get("jednotky")
    vysledek = ""

    try:
        if tvar == "kvadr":
            a = float(data["a"])
            b = float(data["b"])
            c = float(data["c"])
            objem = a * b * c
            povrch = 2 * (a * b + a * c + b * c)
        elif tvar == "krychle":
            a = float(data["a"])
            objem = a**3
            povrch = 6 * (a**2)
        elif tvar == "koule":
            r = float(data["r"])
            objem = (4 / 3) * math.pi * r**3
            povrch = 4 * math.pi * r**2
        else:
            return jsonify({"error": "Neznámý tvar"}), 400

        vysledek = f"Objem: {objem:.2f} {jednotky}³, Povrch: {povrch:.2f} {jednotky}²"
        return jsonify({"vysledek": vysledek})

    except ValueError:
        return jsonify({"error": "Neplatné vstupní hodnoty"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=81, debug=True)
