from tkinter import *
from PIL import Image,ImageTk
import requests
from io import BytesIO # позволяет работать с байтами, картинка прилетает в виде байтов


def loade_image():
    try:
        response = requests.get(url)
        response.raise_for_status() # для обработки исключений
        image_data = BytesIO(response.content) # кортинка будет преобразована с помощью BytesIO
        img = Image.open(image_data)
        return Image Tk.PhotoImage(img)
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None


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