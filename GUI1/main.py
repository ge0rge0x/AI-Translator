from tkinter import *
from tkinter import ttk
from tkinter import messagebox, filedialog
import subprocess

class TranslatorWindow:
    def __init__(self, root):
        self.root = root
        self.translations_history = []  # To store past translations

        # Change the title and size of the window
        self.root.title("AI Translator")
        self.root.geometry("710x400")
        self.root.resizable(False, False)
        self.root.configure(bg="lightgray")
        
        # Widget dimensions and styles
        self.widget_width = 20
        self.widget_font = ('verdana', 11)
        self.textbox_width = 40
        self.textbox_height = 15
        self.textbox_font = ('verdana', 10)
        self.button_font = ('verdana', 12, 'bold')

        # Setting up comboboxes
        self.cb_autoDetect = ttk.Combobox(
            self.root, width=self.widget_width, font=self.widget_font, state='readonly'
        )
        self.cb_autoDetect['values'] = ('Auto Detect',)
        self.cb_autoDetect.place(x=30, y=30)
        self.cb_autoDetect.current(0)

        self.cb_choose_language = ttk.Combobox(
            self.root, width=self.widget_width, font=self.widget_font, state='readonly'
        )
        # List of languages
        languages = [ '📌 English', '📌 Spanish', 'Abkhaz', 'Acehnese','Acholi', 'Afar', 'Afrikaans', 'Albanian', 'Alur', 'Amharic', 'Arabic', 'Armenian',
'Assamese',
'Avar',
'Awadhi',
'Aymara',
'Azerbaijani',
'Balinese',
'Baluchi',
'Bambara',
'Baoulé',
'Bashkir',
'Basque',
'Batak Karo',
'Batak Simalungun',
'Batak Toba',
'Belarusian',
'Bemba',
'Bengali',
'Betawi',
'Bhojpuri',
'Bikol',
'Bosnian',
'Breton',
'Bulgarian',
'Buryat',
'Cantonese',
'Catalan',
'Cebuano',
'Chamorro',
'Chechen',
'Chichewa',
'Chinese (Simplified)',
'Chinese (Traditional)',
'Chuukese',
'Chuvash',
'Corsican',
'Crimean Tatar',
'Croatian',
'Czech',
'Danish',
'Dari',
'Dhivehi',
'Dinka',
'Dogri',
'Dombe',
'Dutch',
'Dyula',
'Dzongkha',
'English',
'Esperanto',
'Estonian',
'Ewe',
'Faroese',
'Fijian',
'Filipino',
'Finnish',
'Fon',
'French',
'Frisian',
'Friulian',
'Fulani',
'Ga',
'Galician',
'Georgian',
'German',
'Greek',
'Guarani',
'Gujarati',
'Haitian Creole',
'Hakha Chin',
'Hausa',
'Hawaiian',
'Hebrew',
'Hiligaynon',
'Hindi',
'Hmong',
'Hungarian',
'Hunsrik',
'Iban',
'Icelandic',
'Igbo',
'Ilocano',
'Indonesian',
'Irish',
'Italian',
'Jamaican Patois',
'Japanese',
'Javanese',
'Jingpo',
'Kalaallisut',
'Kannada',
'Kanuri',
'Kapampangan',
'Kazakh',
'Khasi',
'Khmer',
'Kiga',
'Kikongo',
'Kinyarwanda',
'Kituba',
'Kokborok',
'Komi',
'Konkani',
'Korean',
'Krio',
'Kurdish (Kurmanji)',
'Kurdish (Sorani)',
'Kyrgyz',
'Lao',
'Latgalian',
'Latin',
'Latvian',
'Ligurian',
'Limburgish',
'Lingala',
'Lithuanian',
'Lombard',
'Luganda',
'Luo',
'Luxembourgish',
'Macedonian',
'Madurese',
'Maithili',
'Makassar',
'Malagasy',
'Malay',
'Malay (Jawi)',
'Malayalam',
'Maltese',
'Mam',
'Manx',
'Maori',
'Marathi',
'Marshallese',
'Marwadi',
'Mauritian Creole',
'Meadow Mari',
'Meiteilon (Manipuri)',
'Minang',
'Mizo',
'Mongolian',
'Myanmar (Burmese)',
'Nahuatl (Eastern Huasteca)',
'Ndau',
'Ndebele (South)',
'Nepalbhasa (Newari)',
'Nepali',
'NKo',
'Norwegian',
'Nuer',
'Occitan',
'Odia (Oriya)',
'Oromo',
'Ossetian',
'Pangasinan',
'Papiamento',
'Pashto',
'Persian',
'Polish',
'Portuguese (Brazil)',
'Portuguese (Portugal)',
'Punjabi (Gurmukhi)',
'Punjabi (Shahmukhi)',
'Quechua',
'Qʼeqchiʼ',
'Romani',
'Romanian',
'Rundi',
'Russian',
'Sami (North)',
'Samoan',
'Sango',
'Sanskrit',
'Santali',
'Scots Gaelic',
'Sepedi',
'Serbian',
'Sesotho',
'Seychellois Creole',
'Shan',
'Shona',
'Sicilian',
'Silesian',
'Sindhi',
'Sinhala',
'Slovak',
'Slovenian',
'Somali',
'Spanish',
'Sundanese',
'Susu',
'Swahili',
'Swati',
'Swedish',
'Tahitian',
'Tajik',
'Tamazight',
'Tamazight (Tifinagh)',
'Tamil',
'Tatar',
'Telugu',
'Tetum',
'Thai',
'Tibetan',
'Tigrinya',
'Tiv',
'Tok Pisin',
'Tongan',
'Tsonga',
'Tswana',
'Tulu',
'Tumbuka',
'Turkish',
'Turkmen',
'Tuvan',
'Twi',
'Udmurt',
'Ukrainian',
'Urdu',
'Uyghur',
'Uzbek',
'Venda',
'Venetian',
'Vietnamese',
'Waray',
'Welsh',
'Wolof',
'Xhosa',
'Yakut',
'Yiddish',
'Yoruba',
'Yucatec Maya',
'Zapotec',
'Zulu'
]
        self.cb_choose_language['values'] = languages
        self.cb_choose_language.place(x=457, y=30)
        self.cb_choose_language.current(0)

        # Textboxes with scrollbars
        self.textbox1 = Text(self.root, width=self.textbox_width, height=self.textbox_height,
                             borderwidth=4, font=self.textbox_font, pady=5, relief=RIDGE)
        self.textbox1.place(x=20, y=70)
        self.textbox1_scroll = Scrollbar(self.root, command=self.textbox1.yview)
        self.textbox1_scroll.place(x=350, y=75, height=300, anchor='ne')
        self.textbox1.config(yscrollcommand=self.textbox1_scroll.set)

        self.textbox2 = Text(self.root, width=self.textbox_width, height=self.textbox_height,
                             borderwidth=4, font=self.textbox_font, pady=5, relief=RIDGE)
        self.textbox2.place(x=360, y=70)
        self.textbox2_scroll = Scrollbar(self.root, command=self.textbox2.yview)
        self.textbox2_scroll.place(x=700, y=75, height=300, anchor='ne')
        self.textbox2.config(yscrollcommand=self.textbox2_scroll.set)

        # Buttons
        btn_translate = Button(self.root, text="Translate", relief=RIDGE, borderwidth=2,
                               font=self.button_font, cursor="hand2", command=self.translate, width=8)
        btn_translate.place(x=240, y=345)
        
        btn_clear = Button(self.root, text="Clear", relief=RIDGE, borderwidth=2,
                           font=self.button_font, cursor="hand2", command=self.clear, width=8)
        btn_clear.place(x=370, y=345)

        # Swap Button
        btn_swap = Button(self.root, text="↹", relief=RIDGE, borderwidth=2,
                          font=self.button_font, cursor="hand2", command=self.swap_texts, width=8)
        btn_swap.place(x=308, y=20)

        # History Button
        btn_history = Button(self.root, text="⟲", relief=RIDGE, borderwidth=2,
                             font=self.button_font, cursor="hand2", command=self.show_history, width=8)
        btn_history.place(x=304, y=300)

        # Upload Document Button
        btn_upload = Button(self.root, text="Upload Document", relief=RIDGE, borderwidth=2,
                            font=self.button_font, cursor="hand2", command=self.upload_document, width=15)
        btn_upload.place(x=20, y=340)

    def translate(self):
        '''Takes input from textbox1, runs the command, and shows output in textbox2.'''
        txt_input = self.textbox1.get("1.0", "end-1c")
        language = self.cb_choose_language.get()

        if not txt_input.strip():
            messagebox.showerror('Translator - Error', 'Please type something to translate.')
            return

        command = f"tgpt -q --provider openai --temperature 0 --key 'translate and output translated text only DO NOT CONTAIN ANY ADDITIONAL TEXT, NO CONTEXT Required to {language} this message {txt_input}'"
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            if result.returncode == 0:
                translated_text = result.stdout.strip()
                self.textbox2.delete(1.0, 'end')
                self.textbox2.insert('end', translated_text)
                self.translations_history.append((language, txt_input, translated_text))
            else:
                messagebox.showerror('Translator - Error', f'Command failed with error: {result.stderr.strip()}')
        except Exception as e:
            messagebox.showerror('Translator - Error', f'An error occurred: {str(e)}')

    def clear(self):
        '''Clears textboxes data.'''
        self.textbox1.delete(1.0, 'end')
        self.textbox2.delete(1.0, 'end')

    def swap_texts(self):
        '''Swaps the content of textbox1 and textbox2.'''
        text1 = self.textbox1.get("1.0", "end-1c")
        text2 = self.textbox2.get("1.0", "end-1c")
        
        self.textbox1.delete(1.0, 'end')
        self.textbox2.delete(1.0, 'end')
        
        self.textbox1.insert('end', text2)
        self.textbox2.insert('end', text1)

    def show_history(self):
        '''Displays the history of translations.'''
        history_window = Toplevel(self.root)
        history_window.title("Translation History")
        history_window.geometry("600x300")
        history_window.resizable(False, False)
        
        # Create a text widget for displaying history with scrollbar
        history_text = Text(history_window, width=80, height=15, borderwidth=4, font=('verdana', 10), pady=5, relief=RIDGE)
        history_text.pack(padx=10, pady=10, side=LEFT, fill=Y, expand=True)
        history_scroll = Scrollbar(history_window, command=history_text.yview)
        history_scroll.pack(side=RIGHT, fill=Y)
        history_text.config(yscrollcommand=history_scroll.set)
        
        # Append history to the text widget
        if self.translations_history:
            for entry in self.translations_history:
                language, original, translated = entry
                history_text.insert('end', f"Language: {language}\n")
                history_text.insert('end', f"Original Text: {original}\n")
                history_text.insert('end', f"Translated Text: {translated}\n")
                history_text.insert('end', "-" * 40 + "\n")
        else:
            history_text.insert('end', "No translations yet.\n")

    def upload_document(self):
        '''Opens a file dialog to select a document and inserts its text into textbox1.'''
        file_path = filedialog.askopenfilename(
            title="Select Document",
            filetypes=(("Text files", "*.txt"), ("All files", "*.*"))
        )
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    self.textbox1.delete(1.0, 'end')
                    self.textbox1.insert('end', content)
            except Exception as e:
                messagebox.showerror('Error', f'Failed to read the file: {str(e)}')

# Driver code
if __name__ == "__main__":
    root = Tk()
    app = TranslatorWindow(root)
    root.mainloop()

