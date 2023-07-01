import tkinter as tk 
from tkinter import Tk
from tkinter import messagebox as msgbox
from tkinter import filedialog
from PIL import ImageTk, Image
from photo_watermark import add_date_to_photo


def add_date_exec(photo_path):  
    
    output_code = add_date_to_photo(
        photo_path,
        date_tf.get(),
        output_path_tf.get()
    )

    if output_code == 0:
        msgbox.showinfo('Состояние', 'Готово!')
        window_add_date.destroy()

def get_file_path():
    window_select_photos = Tk()
    window_select_photos.title("Выбор фото")
    window_select_photos.geometry("780x600")
    photo_pathes = filedialog.askopenfilenames()
    window_select_photos.destroy()

    return photo_pathes

photo_pathes = get_file_path()

for photo_path in photo_pathes:

    window_add_date = Tk()
    window_add_date.title("Добавляем дату на фото")
    window_add_date.geometry("700x400")

    frame = tk.Frame(
        window_add_date,
        padx=10,
        pady=10
    )

    frame.pack(expand=True)

    date_lb = tk.Label(
        frame,
        text="Введите дату, которую надо добавить на фото"
    )

    date_lb.grid(row=2, column=1)

    date_tf = tk.Entry(frame)
    date_tf.grid(row=2, column=3, pady=5)


    output_path_lb = tk.Label(
        frame,
        text="Введите папку, куда положить фото"
    )


    output_path_lb.grid(row=3, column=1)

    output_path_tf = tk.Entry(frame)
    output_path_tf.grid(row=3, column=3, pady=5)

    image = Image.open(photo_path)

    x, y = image.size
    times = x // 400

    resize_val = (int(x / times), int(y / times))

    img_tk = ImageTk.PhotoImage(image.resize(resize_val), master=frame)

    img_lb = tk.Label(
        frame,
        image=img_tk
    )

    img_lb.grid(row=5, column=1, padx=30, pady=5)
    
    ##
    add_button = tk.Button(
        frame,
        text='Добавить дату на фото',
        command=lambda: add_date_exec(photo_path)
    )

    add_button.grid(row=4, column=3, pady=5)
    
    # select_button = tk.Button(
    #     frame,
    #     text='Выбрать другие фото',
    #     command=get_file_path
    # )

    # select_button.grid(row=5, column=3, pady=5)

    window_add_date.mainloop()
