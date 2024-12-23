from tkinter import *
from PIL import Image,ImageTk
import requests
from io import BytesIO # позволяет работать с байтами, картинка прилетает в виде байтов

window = Tk()
window.title("Cats!")
window.geometry("600x480")

label = Label()
label.pack()

url = "https://cataas.com/cat" # url адрес в интернете
img = load_image(url) # функция загрузки изображения в который будем передавать url и будет возвращаться картинка
#делаем проверку

if img:
    label.config(image=img) # установим картинку на метку
    label.image = img # нужно чтобы сборщик мусора не убрал картинку

window.mainloop()