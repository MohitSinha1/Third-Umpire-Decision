import tkinter #read about tkinter, cv2, PIL and canvas
import cv2
#python Imaging library
import PIL.Image, PIL.ImageTk
from functools import partial
import threading
import imutils
import time
#fixing width and height


set_width = 850
set_height = 600

path0 = r'D:\PYTHON-BOOTCAMP\Python_code\video.mp4'
stream = cv2.VideoCapture(path0)
flag = True
def play(speed):
    global flag
    print(f"You clicked on play. Speed is {speed}")

    # Play the video in reverse mode
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)

    grabbed, frame = stream.read()
    if not grabbed:
        exit()
    frame = imutils.resize(frame, width = set_width, height = set_height)
    frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)
    if flag:
        canvas.create_text(134, 26, fill="black", font="Times 26 bold", text="Decision Pending")
    flag = not flag



def pending(decision):
    # 1. Display decision pending image
    path1 = r'D:\PYTHON-BOOTCAMP\Python_code\pending.png'
    src1 = cv2.imread(path1)
    frame = cv2.cvtColor(src1, cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width= set_width , height= set_height)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)
    # 2. Wait for 1 second
    time.sleep(1.5)

    # 3. Display sponsor image
    path2 = r'D:\PYTHON-BOOTCAMP\Python_code\sponsor.png'
    src2 = cv2.imread(path2)
    frame = cv2.cvtColor(src2 , cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width = set_width, height = set_height)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)

    # 4. Wait for 1.5 second
    time.sleep(2.5)
    # 5. Display out/notout image
    if decision == 'out':
        path3 = r'D:\PYTHON-BOOTCAMP\Python_code\out.png'
        src3 = cv2.imread(path3)
    else:
        path3 = r'D:\PYTHON-BOOTCAMP\Python_code\not_out.png'
        src3 = cv2.imread(path3)
    frame = cv2.cvtColor(src3, cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width = set_width, height = set_height)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)


def out():
    thread = threading.Thread(target=pending, args=("out",))
    thread.daemon = 1
    thread.start()
    print("Player is out")


def not_out():
    thread = threading.Thread(target=pending, args=("not out",))
    thread.daemon = 1
    thread.start()
    print("Player is not out")





window = tkinter.Tk()
window.title("Mohit Third Umpire Decision")
path = r'D:\PYTHON-BOOTCAMP\Python_code\Homescreen.PNG'
src = cv2.imread(path)
cv_img = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window, width= set_width, height= set_height)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0, 0, ancho=tkinter.NW, image=photo)
canvas.pack()


# Buttons to control playback
btn = tkinter.Button(window, text="<< Previous (fast)", width=50, command=partial(play, -25))
btn.pack()

btn = tkinter.Button(window, text="<< Previous (slow)", width=50, command=partial(play, -2))
btn.pack()

btn = tkinter.Button(window, text="Next (slow) >>", width=50, command=partial(play, 0.5))
btn.pack()

btn = tkinter.Button(window, text="Next (fast) >>", width=50, command=partial(play, 25))
btn.pack()

btn = tkinter.Button(window, text="Give Out", width=50, command=out)
btn.pack()

btn = tkinter.Button(window, text="Give Not Out", width=50, command=not_out)
btn.pack()


window.mainloop()