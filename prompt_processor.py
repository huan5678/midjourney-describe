import os
import sys
import re
import pyperclip
import tkinter as tk
from reportlab.graphics import renderPM
from svglib.svglib import svg2rlg
from tkinter import PhotoImage, END, INSERT
from tkinter.ttk import Style, Button, Label, Entry
from PIL import Image as PImage


def process_string(input_string, prefix, ar):
    input_string = re.sub(r'\d️⃣', None, input_string)
    input_string = re.sub(r',', r'\,', input_string)  # 替換逗號
    input_string = re.sub(r'--ar \d+:\d+', ',', input_string)
    input_string = re.sub(r'\n+', '\n', input_string).strip()
    lines = input_string.split('\n')
    joined_lines = ','.join(lines).rstrip(',')
    final_string = f'{{{joined_lines}}} --ar {ar} --{{{prefix}}}'
    return final_string

def process_and_display(input_textbox, prefix_entry, result_textbox, last_ar_entry):
    input_text = input_textbox.get("1.0", END)
    prefix = prefix_entry.get()
    last_ar = last_ar_entry.get()
    result = process_string(input_text, prefix, last_ar)
    result_textbox.configure(state="normal")  # 臨時啟用以更新內容
    result_textbox.delete("1.0", END)
    result_textbox.insert(INSERT, result)
    result_textbox.configure(state="disabled")  # 更新後禁用

def resource_path(relative_path):
    """獲取應用程序資源的絕對路徑"""
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.dirname(os.path.abspath(__file__))

    return os.path.join(base_path, relative_path)

def clear_textbox(input_textbox, result_textbox):
    input_textbox.delete("1.0", END)
    result_textbox.configure(state="normal")  # 臨時啟用以更新內容
    result_textbox.delete("1.0", END)
    result_textbox.configure(state="disabled")  # 更新後禁用


def svg_to_photoimage(svg_file_path, size=None):
    drawing = svg2rlg(svg_file_path)
    output_path = os.path.splitext(svg_file_path)[0] + ".png"
    renderPM.drawToFile(drawing, output_path, fmt="PNG")

    if size is not None:
        img = PImage.open(output_path)
        img = img.resize(size, PImage.ANTIALIAS)
        img.save(output_path, "PNG")

    img = PhotoImage(file=output_path)
    os.remove(output_path)
    return img

def copy_result(result_textbox):
    result_text = result_textbox.get("1.0", END)
    pyperclip.copy(result_text.strip())
    
def paste_scoured_text(input_textbox):
    input_text = pyperclip.paste()
    input_textbox.insert(INSERT, input_text)

def create_gui():
    window = tk.Tk()
    window.title("Text Processor")

    window_width = 640
    window_height = 560
    window.geometry(f"{window_width}x{window_height}")

    if sys.platform == 'win32':
      window.iconbitmap(resource_path('assets/icon.ico'))

    else:
        img = PhotoImage(file=resource_path('assets/icon.icns'))
        window.tk.call('wm', 'iconphoto', window._w, img)

    content_frame = tk.Frame(window)
    content_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    style = Style()
    style.configure('TButton', font=('Arial', 10))

    input_label = Label(content_frame, text="Prompt:")
    input_label.grid(row=0, column=0, sticky=tk.W, pady=5)

    input_textbox = tk.Text(content_frame, height=10, width=80, wrap="word")
    input_textbox.grid(row=1, column=0, columnspan=2, pady=5)

    # input_scrollbar_y = tk.Scrollbar(content_frame, orient="vertical", command=input_textbox.yview)
    # input_scrollbar_y.grid(row=1, column=2, sticky=tk.NSEW)
    # input_textbox.config(yscrollcommand=input_scrollbar_y.set)

    paste_icon = svg_to_photoimage(resource_path('assets/paste.svg'), size=(24, 24))
    paste_button = Button(content_frame, image=paste_icon, style='TButton', command=lambda: paste_scoured_text(input_textbox))
    paste_button.grid(row=0, column=1, sticky=tk.E, padx=10, pady=10)

    prefix_label = Label(content_frame, text="Prefix:")
    prefix_label.grid(row=3, column=0, sticky=tk.W, padx=10, pady=10)

    prefix_entry = Entry(content_frame)
    prefix_entry.insert(0, "5,n5,ex,sc")
    prefix_entry.grid(row=3, column=0, padx=10, pady=10)

    process_button = Button(content_frame, text="Generate", style='TButton',
    command=lambda: process_and_display(
    input_textbox, prefix_entry, result_textbox, ar_entry))
    process_button.grid(row=3, column=1, sticky=tk.E, padx=10, pady=10)

    ar_label = Label(content_frame, text="AR:")
    ar_label.grid(row=4, column=0, sticky=tk.W, padx=10, pady=10)

    ar_entry = Entry(content_frame)
    ar_entry.insert(0, "5:7")
    ar_entry.grid(row=4, column=0, padx=10, pady=10)

    clear_button = Button(content_frame, text="Clear", style='TButton', command=lambda: clear_textbox(input_textbox, result_textbox))
    clear_button.grid(row=4, column=1, sticky=tk.E, padx=10, pady=10)

    result_label = Label(content_frame, text="Result:")
    result_label.grid(row=5, column=0, sticky=tk.W, padx=10, pady=10)

    result_textbox = tk.Text(content_frame, height=10, width=80, state="disabled")  # 初始化為禁用
    result_textbox.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    copy_icon = svg_to_photoimage("assets/copy.svg", size=(24,24))

    copy_button = Button(content_frame, image=copy_icon, style='TButton', command=lambda: copy_result(result_textbox))
    copy_button.grid(row=7, column=1, sticky=tk.E, padx=10, pady=10)

    window.mainloop()


if __name__ == "__main__":
    create_gui()


