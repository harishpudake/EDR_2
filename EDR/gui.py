
import customtkinter as ctk
from PIL import ImageTk,Image
import os



# To get the current working directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the full path to the  background image
bg_image_path = os.path.join(script_dir, "Resources", "bg_image.jpg")

# Construct the full path to the app icon (.ico) image
app_icon_path = os.path.join(script_dir, "Resources", "icons", "logo_icon.ico")



ctk.set_appearance_mode("Dark")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green


# --- Main Window Configuration ----
app = ctk.CTk() 
app.geometry("900x650")
app.title('Threat-Lock')
app.iconbitmap(app_icon_path) 
app.resizable(False, False)
# ----------------------------------





# ---------------------- adds the Background image ------------------------------------
img1=ImageTk.PhotoImage(Image.open(bg_image_path))
l1=ctk.CTkLabel(master=app,image=img1, text="")
l1.pack()
# -------------------------------------------------------------------------------------


# run the app/window
app.mainloop()
