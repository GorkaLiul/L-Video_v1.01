
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

import pytube
from pytube import YouTube

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/home/gorkaliul/Desktop/MyTkinterApp/build/assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

#~/Downloads
def click():
    global link
    global output
    output = entry_2.get()
    link = entry_1.get()

    yt = pytube.YouTube(link)
    video = yt.streams.get_highest_resolution()
    video.download(output)
    print('Video has been downloaded')

window = Tk()
window.title('L-VideoDownloader v1.0')
window.geometry("526x211")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 211,
    width = 526,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    189.0,
    96.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    263.0,
    20.0,
    image=image_image_2
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    209.5,
    96.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=72.0,
    y=79.0,
    width=275.0,
    height=33.0
)

canvas.create_text(
    9.0,
    8.0,
    anchor="nw",
    text="Video Downloader\n",
    fill="#000000",
    font=("Inter SemiBold", 12 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command = click,
    relief="flat"
)
button_1.place(
    x=378.0,
    y=79.0,
    width=99.0,
    height=101.0
)

canvas.create_text(
    24.0,
    89.0,
    anchor="nw",
    text="URL:",
    fill="#373737",
    font=("Inter SemiBold", 12 * -1)
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    189.0,
    146.0,
    image=image_image_3
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    219.0,
    146.5,
    image=entry_image_2
)
entry_2 = Entry(text = "~/Downloads",
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
    )
entry_2.place(
    x=91.0,
    y=129.0,
    width=256.0,
    height=33.0
)

canvas.create_text(
    24.0,
    137.0,
    anchor="nw",
    text="Output:",
    fill="#373737",
    font=("Inter SemiBold", 12 * -1)
)
window.resizable(False, False)
window.mainloop()
