import customtkinter as ctk
import subprocess
import threading
import tkinter.messagebox as messagebox
from tkinter import Toplevel
from text import translate_text

# Configure appearance
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

# translate text
def translate():
    input_text = text_input.get("1.0", "end-1c").strip()
    language = language_input.get()

    if input_text and language:
        try:
            translated_text = translate_text(input_text, language)
            result_output.delete("1.0", "end")
            result_output.insert(ctk.END, translated_text)
        except Exception as e:
            messagebox.showerror("Error", f"Translation failed: {e}")
    else:
        messagebox.showwarning("Warning", "Please enter both text and target language.")

# function to handle AI chat in a separate thread
def run_ai_chat_threaded():
    threading.Thread(target=run_ai_chat).start()

# Function to run the AI chat program
def run_ai_chat():
    try:
        # Start the assistant.py process with explicit UTF-8 encoding, make sure the path to the assistant.py is correct
        process = subprocess.Popen([r"python3", "assistant.py"],
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding='utf-8')

        # Read the output line by line
        for line in process.stdout:
            ai_output_textbox.insert(ctk.END, line)
            ai_output_textbox.see(ctk.END)  # Auto-scroll to the end

        # Check for any errors
        stderr = process.stderr.read()
        if stderr:
            messagebox.showerror("Error", f"AI Chat Error: {stderr}")

    except Exception as e:
        messagebox.showerror("Error", f"Failed to start AI Chat: {e}")

#load history from the file and display it in a new window
def load_history():
    try:
        with open("history.txt", "r", encoding="utf-8") as file:
            history_content = file.read()

        # Create a new top-level window for displaying the history
        history_window = Toplevel(app)
        history_window.title("Chat History")
        history_window.geometry("600x400")

        # Set the frame background color
        history_window.configure(bg="black")

        # Create a textbox to display the history with black background and white text
        history_textbox = ctk.CTkTextbox(history_window, height=300, width=580)
        history_textbox.pack(pady=10, padx=10)
        history_textbox.insert("1.0", history_content)
        history_textbox.configure(state="disabled")  # Make the textbox read-only

        # Set the appearance to black background and white text
        history_textbox.configure(bg="black", fg="white")

    except FileNotFoundError:
        messagebox.showerror("Error", "No history found.")

# Function to show about information
def show_about():
    messagebox.showinfo("About", "This is a human-like translator \nVersion 1.0")

# Create the main window
app = ctk.CTk()
app.title("Text Translator and AI Chat")
app.geometry("900x700")

# add a main frame
main_frame = ctk.CTkFrame(app)
main_frame.pack(pady=20, padx=20, fill="both", expand=True)

# Translator Section
translator_frame = ctk.CTkFrame(main_frame)
translator_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

translator_label = ctk.CTkLabel(translator_frame, text="Text Translator", font=ctk.CTkFont(size=18, weight="bold"))
translator_label.pack(pady=10)

language_label = ctk.CTkLabel(translator_frame, text="Enter Target Language:")
language_label.pack(pady=5)

language_input = ctk.CTkEntry(translator_frame, width=300)
language_input.pack(pady=5)

text_input_label = ctk.CTkLabel(translator_frame, text="Enter Text to Translate:")
text_input_label.pack(pady=5)

text_input = ctk.CTkTextbox(translator_frame, height=100, width=600)
text_input.pack(pady=5)

translate_button = ctk.CTkButton(translator_frame, text="Translate", command=translate)
translate_button.pack(pady=10)

result_label = ctk.CTkLabel(translator_frame, text="Translated Text:")
result_label.pack(pady=5)

result_output = ctk.CTkTextbox(translator_frame, height=250, width=600)
result_output.pack(pady=5)

# AI Chat Section
ai_chat_frame = ctk.CTkFrame(main_frame)
ai_chat_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

ai_chat_label = ctk.CTkLabel(ai_chat_frame, text="AI Chat", font=ctk.CTkFont(size=18, weight="bold"))
ai_chat_label.pack(pady=10)

ai_chat_button = ctk.CTkButton(ai_chat_frame, text="Chat to AI", command=run_ai_chat_threaded)
ai_chat_button.pack(pady=10)

ai_output_label = ctk.CTkLabel(ai_chat_frame, text="AI Output:")
ai_output_label.pack(pady=5)

ai_output_textbox = ctk.CTkTextbox(ai_chat_frame, height=300, width=600)
ai_output_textbox.pack(pady=5)

# Dropdown and Additional Buttons Section
additional_options_frame = ctk.CTkFrame(app)
additional_options_frame.pack(pady=20)

load_history_button = ctk.CTkButton(additional_options_frame, text="Load History", command=load_history)
load_history_button.pack(side="left", padx=10)

about_button = ctk.CTkButton(additional_options_frame, text="About", command=show_about)
about_button.pack(side="left", padx=10)

# Make the columns and rows in the main frame expandable
main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_columnconfigure(1, weight=1)
main_frame.grid_rowconfigure(0, weight=1)

# Run the main loop
app.mainloop()
