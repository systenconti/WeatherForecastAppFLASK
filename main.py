from flask import Flask, render_template, request
from backend import get_data

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def weather():
    if request.method == "POST":
        city = request.form["city"]
        day = request.form["day"]
        forecasttype = request.form["forecasttype"]
        print(city, day, forecasttype)

        filtered_data = get_data(place=city, forecast_days=int(day))
        dates = [item["dt_txt"] for item in filtered_data]
        temperatures = [item["main"]["temp"] for item in filtered_data]
        sky_conditions = [item["weather"][0]["main"] for item in filtered_data]
        print(dates, temperatures, sky_conditions)
    return render_template("weather.html")


if __name__ == "__main__":
    app.run(debug=True)
