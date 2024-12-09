# you have to first install with "pip install tinter" then "pip install Huggingface_hub" if huggingface_hub was incorrect , you have to visit Huggingface.co and check with lab should you install
import tkinter as tk
from tkinter import simpledialog, messagebox
from huggingface_hub import InferenceClient
from PIL import Image
import matplotlib.pyplot as plt
import time
import tkinter.font as tkFont
import time

print ("""
███--███---████---██--██---████---███--███--██████--██---██---████---██--██--███--██--██████--------██████--██████-
██-█-███--██------██--██--██--██--██-██-██--██--██---██-██---██--██--██--██--██-█-██----██------------██----██--██-
██--█-██---████---██████--██--██--██--█-██--██████----███----██--██--██--██--██--███----██----████----██----█████--
██----██------██--██--██--██--██--██----██--██--██----██-----██--██--██--██--██---██----██----████----██----██--██-
██----██--█████---██--██---████---██----██--██--██----██------████----████---██---██--██████--------██████--██---██
mshomayouni.ir ! 
""")
time.sleep(5)
# to run Hugging face
client = InferenceClient("black-forest-labs/FLUX.1-schnell", token="Your token")

# UI
def generate_image():
    user_input = simpledialog.askstring("prompt", "what do you want to draw with Flux?")
    
    if not user_input:
        messagebox.showwarning("info!", "please type a thing")
        return
    
    try:
        # waiting
        waiting_label.config(text="AI generating")
        root.update()

        # AI settings
        image = client.text_to_image(user_input)
        
        
        waiting_label.config(text="")
        
        # picture 
        plt.imshow(image)
        plt.axis('off')  # picture Show
        plt.show()
    except Exception as e:
        messagebox.showerror("ERR", f"an error detected {e}")
        waiting_label.config(text="")
        



# UI
root = tk.Tk()
root.title("AI image generator")
root.geometry("1000x600")
root.configure(bg='#FFB84D')  # orange UI

# Cairo font (or any other fonts)
font_cairo = tkFont.Font(family="Cairo", size=16)

# Welcome 
welcome_label = tk.Label(root, text="**Mohammadsam Homayouni's new project**", font=("Cairo", 24, "bold"), bg="#FFB84D", fg="#FF6F00")
welcome_label.pack(pady=50)
# my website
welcome_label = tk.Label(root, text="mshomayouni.ir", font=("Cairo", 24, "bold"), bg="#FFB84D", fg="#FF6F00")
welcome_label.pack(pady=50)

# waiting
waiting_label = tk.Label(root, text="wait", font=("Cairo", 14), bg="#FFB84D", fg="#FF6F00")
waiting_label.pack(pady=20)

# button to Start
generate_button = tk.Button(root, text="use AI", command=generate_image, height=2, width=20, font=font_cairo, bg="#FF6F00", fg="white", relief="raised")
generate_button.pack(pady=20)

# waiting code
def show_animation():
    waiting_label.config(text="wait.....")

# Start
show_animation()
root.mainloop()
