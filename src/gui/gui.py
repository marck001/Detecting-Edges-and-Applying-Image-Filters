import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.colorchooser import askcolor
from PIL import ImageTk, Image
#from ..image_filtering.contrast import apply_contrast

def create_gui():
 
    window = tk.Tk()
    window.title("GUI")
    window.configure(bg='white')
    
    frame = tk.Frame(window, padx=30, pady=40, bg="white")
    frame.grid(row=0, column=0)

    tk.Label(frame, text="Detecting Edges and Applying Image Filters",
             font=('Helvetica', 24), bg='white', fg='blue').grid(row=0, column=0, columnspan=4, pady=20)


    global canvas
    canvas = Canvas(frame, width=900, height=350, bg="azure", highlightthickness=0)
    canvas.grid(row=1, column=0, columnspan=4, pady=10)

    global input_img_label, output_img_label, input_img_tk, output_img_tk
    input_img_label = canvas.create_image(150, 50, anchor='nw') 
    output_img_label = canvas.create_image(500, 50, anchor='nw')  

    
    contrast_btn = Button(frame, text='Contrast', width=12, height=2, bg='yellow',
                          activebackground='light sea green', font=('Times', 18, 'bold'))
    vignette_btn = Button(frame, text='Vignette', width=12, height=2, bg='yellow',
                          activebackground='light sea green', font=('Times', 18, 'bold'))
    choose_color_btn = Button(frame, text="Choose color", command=show)
    load_input_image_btn = Button(frame, text="Load Input Image", command=load_input_image)

    load_input_image_btn.grid(row=2, column=0, padx=10, pady=10)
    contrast_btn.grid(row=2, column=1, padx=10, pady=10)
    vignette_btn.grid(row=2, column=2, padx=10, pady=10)
    choose_color_btn.grid(row=2, column=3, padx=10, pady=10)
    
    return window

def show():
   color = askcolor()
   print(color)
   


def load_input_image():
    global input_img, output_img, input_img_tk, output_img_tk
  
    file_path = filedialog.askopenfilename()
    print(file_path)
    if file_path:
        input_img = Image.open(file_path).resize((300, 300))
        output_img = input_img.copy()  
        input_img_tk = ImageTk.PhotoImage(input_img)

       
        canvas.itemconfig(input_img_label, image=input_img_tk)
        canvas.input_image_ref = input_img_tk 

       
        update_output_image(output_img)

def update_output_image(image):
    global output_img_tk
    output_img_tk = ImageTk.PhotoImage(image.resize((300, 300)))
    canvas.itemconfig(output_img_label, image=output_img_tk)
    canvas.output_image_ref = output_img_tk  