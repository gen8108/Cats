from tkinter import *
from PIL import Image,ImageTk
import requests
from io import BytesIO # позволяет работать с байтами, картинка прилетает в виде байтов


def load_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status() # для обработки исключений
        image_data = BytesIO(response.content) # картинка будет преобразована с помощью BytesIO
        img = Image.open(image_data)
        img.thumbnail((600, 480), Image.Resampling.LANCZOS)# картинку подогнать под размер
        #Image.Resampling.LANCZOS принцип по которому будет конвертироваться картинка(не страдает качество)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None

def set_image():
    img = load_image(url)

    if img:
        label.config(image=img)  # установим картинку на метку
        label.image = img  # нужно чтобы сборщик мусора не убрал картинку


window = Tk()
window.title("Cats!")
window.geometry("600x520")

label = Label()
label.pack()

update_button = Button(text= "Обновить", command=set_image)# обновление
update_button.pack()

url = "https://cataas.com/cat" # url адрес в интернете

set_image()

window.mainloop()