import requests
from flask import Flask, request, render_template

app = Flask(__name__)

api_pepet = "58b1f3086105a30639a60822d010dff5"

@app.route("/", methods=["GET", "POST"])
def home():
    data_cuaca = None

    if request.method == "POST":
        kota = request.form["kota"]

        url = f"https://api.openweathermap.org/data/2.5/weather?q={kota}&appid={api_pepet}&units=metric"
        respon = requests.get(url)
        data = respon.json()

        if data["cod"] == 200:
            data_cuaca = {
                "kota": kota,
                "temp": data["main"]["temp"],
                "weather": data["weather"][0]["description"],
                "humidity": data["main"]["humidity"]
            }
        else:
            data_cuaca = {"error": "Kota tidak ditemukan"}

    return render_template("index.html", cuaca=data_cuaca)

if __name__ == "__main__":
    app.run(debug=False)