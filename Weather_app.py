from configparser import ConfigParser
import requests
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

# Read API key from the configuration file
config_file = "config.ini"
config = ConfigParser()
config.read(config_file)
api_key = config['sofian']['api']
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

# Function to retrieve weather details
def get_weather(city):
    try:
        result = requests.get(url.format(city, api_key))
        if result.ok:
            data = result.json()
            # city_name = data['name']
            # country = data['sys']
            temp_kelvin = data['main']['temp']
            temp_celsius = temp_kelvin - 273.15
            weather_description = data['weather'][0]['main']
            return temp_celsius, weather_description
        else:
            print("Error: Failed to retrieve weather data.")
    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))
    return None

# Function to search for a city's weather
def search():
    city = city_text.get()
    weather = get_weather(city)
    if weather:
        temperature_label['text'] = '{:.2f} Degree Celsius'.format(weather[0])
        weather_l['text'] = weather[1]
    else:
        messagebox.showerror('Error', "Cannot find {}".format(city))

# Create the GUI application window
app = Tk()
app.title("Weather App")
app.geometry("300x400")

# Set background image
background_image = Image.open("c:/Users/radeb/Pictures/background.jpg")
background_image = background_image.resize((300, 400), Image.LANCZOS)
background_photo = ImageTk.PhotoImage(background_image)
background_label = Label(app, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Add labels, buttons, and text entry field
city_text = StringVar()
city_entry = Entry(app, textvariable=city_text, font=("Arial", 12), width=20)
city_entry.place(relx=0.5, rely=0.2, anchor=CENTER)

search_btn = Button(app, text="Search Weather", width=15, command=search, bg="lightblue", font=("Arial", 12, "bold"))
search_btn.place(relx=0.5, rely=0.3, anchor=CENTER)

# location_lbl = Label(app, text="Location", font=("Arial", 14, "bold"), fg="white", bg="black")
# location_lbl.place(relx=0.5, rely=0.42, anchor=CENTER)

temperature_label = Label(app, text="", font=("Arial", 12), fg="white", bg="black")
temperature_label.place(relx=0.5, rely=0.5, anchor=CENTER)

weather_l = Label(app, text="", font=("Arial", 12), fg="white", bg="black")
weather_l.place(relx=0.5, rely=0.6, anchor=CENTER)

# Run the GUI application
app.mainloop()
