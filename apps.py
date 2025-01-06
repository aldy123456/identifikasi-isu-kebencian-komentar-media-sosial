import tkinter as tk
import pandas as pd
import customtkinter
import re
import nltk
import string
import pickle
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import filedialog
from customtkinter import CTkEntry
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from PIL import Image as PILImage
stemmer = nltk.SnowballStemmer("english")
stopword = set(stopwords.words('english'))

class project:
    def __init__(self, root, text):
        self.root = root
        self.root.title("Halaman Depan")
        self.root.geometry("1920x1080")
        self.root.state('zoomed')
        self.root.resizable(0, 0)
        # self.login_success = False
        self.create_widgets()

    def create_widgets(self):
        self.create_background()
        self.create_entry()
        self.create_reset_button()
        self.button_function()
        self.create_table()

    def create_background(self):
        self.gambar_image = PILImage.open("C://Users/wawut/OneDrive/Documents/pemrosesan teks/ku/gambar7.png")

        # Resize the image to fit the window size
        self.resized_image = self.gambar_image.resize((1240, 650), PILImage.ANTIALIAS)

        # Convert the resized image to ImageTk format
        self.gambar_image = ImageTk.PhotoImage(self.resized_image)

        # Create a label with the resized image
        self.gambar_image_label = tk.Label(self.root, image=self.gambar_image)
        self.gambar_image_label.place(x=0, y=0, relwidth=1, relheight=1)

    def create_entry(self):
        self.entry = CTkEntry(
            master=self.root,
            placeholder_text="Type your text here...",
            width=880,
            height=80,
            bg_color="white",
            border_width=2,
            corner_radius=10
        )
        self.entry.place(x=250, y=180)

    def button_function(self):
        self.login_button = tk.Button(self.root, text="enter",bg= "#00c6ba", command=self.prediksi, font=("Helvetica", 12, "bold"), borderwidth=0)
        self.login_button.place(x=610, y=278, width=150, height=55)
        # Set the font for the entry
        self.entry.configure(font=("Helvetica", 16, "bold"))

    def create_table(self):
    # Create Treeview widget
        columns = ("Input Text", "Prediction Result")
        self.tree = ttk.Treeview(self.root, columns=columns, show='headings', height=13)
        self.tree.heading("Input Text", text="Input Text")
        self.tree.heading("Prediction Result", text="Prediction Result")
        self.tree.column("Input Text", width=600)
        self.tree.column("Prediction Result", width=250)
        self.tree.place(x=270, y=400)

        # Define tag configurations for row colors
        self.tree.tag_configure("header", background="lightblue")

        # Set up styles for custom appearance
        self.tree_style = ttk.Style()
        self.tree_style.configure("Treeview.Heading", font=('Helvetica', 12, 'bold'), foreground='black')  # Header style
        self.tree_style.configure("Treeview", font=('Helvetica', 10), background='#f0f0f0')  # Body style


    def cleaning(self, text):
        text = str(text).lower()
        text = re.sub('\[.*?\]', '', text)
        text = re.sub('https?://\S+|www\.\S+', '', text)
        text = re.sub('<.*?>+', '', text)
        text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
        text = re.sub('\n', '', text)
        text = re.sub('\w*\d\w*', '', text)
        text_tokens = word_tokenize(text)
        text = [word for word in text_tokens if not word in stopword]
        text = " ".join(text)
        text = [stemmer.stem(word) for word in text.split(' ')]
        text = " ".join(text) 
        return text

    def prediksi(self):
        loaded_vectorizer = pickle.load(open('tfidf_vectorizer5.pkl', 'rb'))
        teks_baru = self.entry.get()
        teks_baru1 = self.cleaning(teks_baru)

        loaded_model = pickle.load(open('svm_model.sav', 'rb'))
        self.Prediction = loaded_model.predict(loaded_vectorizer.transform([teks_baru1]))

        explanation_text = self.explain_prediction(self.Prediction[0])
        self.tree.insert("", "end", values=(teks_baru, explanation_text))
    
    def explain_prediction(self, Prediction):
        if self.Prediction == 1:
            return "Hate Speech"
        elif self.Prediction == 2:
            return "Offensive Language"
        elif self.Prediction == 0:
            return "Neutral"
        
    def create_reset_button(self):
        self.reset_button = tk.Button(self.root, text="Reset", bg="white", command=self.reset_table, font=("Helvetica", 12, "bold"), borderwidth=0)
        self.reset_button.place(x=1180, y=630, width=130, height=40)

    def reset_table(self):
    # Delete all items in the Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)
        
if __name__ == "__main__":
    root = tk.Tk()
    project = project(root, text="")
    root.mainloop()
