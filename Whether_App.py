import tkinter as tk
from tkinter import messagebox
import requests

API_KEY = "Your API Key "

def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&q="

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        city_name = data['name']
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description'].title()

        result_text = (
            f"Weather in {city_name}:\n"
            f"Temperature: {temp}°C\n"
            f"Feels Like: {feels_like}°C\n"
            f"Humidity: {humidity}%\n"
            f"Condition: {description}"
        )
        weather_result.config(text=result_text)

    except requests.exceptions.HTTPError as err:
        if response.status_code == 404:
            messagebox.showerror("Error", "City not found.")
        else:
            messagebox.showerror("Error", f"HTTP error: {err}")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")


app = tk.Tk()
app.title("Weather App")
app.geometry("400x300")
app.resizable(False, False)

tk.Label(app, text="Enter City:", font=("Arial", 14)).pack(pady=10)
city_entry = tk.Entry(app, font=("Arial", 14), justify="center")
city_entry.pack(pady=5)

tk.Button(app, text="Get Weather", font=("Arial", 14), command=get_weather).pack(pady=10)

weather_result = tk.Label(app, text="", font=("Arial", 12), justify="left")
weather_result.pack(pady=10)

app.mainloop()
