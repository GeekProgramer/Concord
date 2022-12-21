import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

from dotenv import load_dotenv

load_dotenv()

import cloudinary
import cloudinary.uploader
import cloudinary.api


class PfpManager:
    def __init__(self):
        self.config = cloudinary.config(secure=True)
        root = tk.Tk()
        root.withdraw()
        self.file_path = ""

    def getAndUpload(self):
        self.file_path = filedialog.askopenfilename()
        src = ""
        try:
            messagebox.showinfo("Uploading...", "Uploading image...")
            src = self.uploadImage(self.file_path)
            messagebox.showinfo("Success", "Avatar uploaded")
            
        except:
            print("User closed the context dialog")
        return src

    def uploadImage(self, path):
        cloudinary.uploader.upload(path, public_id="pfp", unique_filename=False, overwrite=True)

        cObj = cloudinary.CloudinaryImage("pfp")
        srcURL = cObj.build_url()

        print("****2. Upload an image****\nDelivery URL: ", srcURL, "\n")
        return srcURL