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

def exit():
    window.destroy()




window = Tk()
window.title("Cats!")
window.geometry("600x520")

label = Label()
label.pack()

# update_button = Button(text= "Обновить", command=set_image)# обновление
# update_button.pack()

menu_bar Menu(window)
window.config(menu = menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Загрузить фото", command=set_image)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=exit)

url = "https://cataas.com/cat" # url адрес в интернете

set_image()

window.mainloop()