from tkinter import Tk, ttk, Label, Entry, Button, Text, StringVar
from googletrans import Translator, LANGUAGES

translator = Translator()

def translate_text():
    source_language = source_lang_var.get()
    target_language = target_lang_var.get()
    text = text_entry.get()
    
    source_lang_code = get_language_code(source_language)
    target_lang_code = get_language_code(target_language)
    
    if source_lang_code and target_lang_code:
        try:
            translation = translator.translate(text, src=source_lang_code, dest=target_lang_code)
            result_text.delete(1.0, "end")
            result_text.insert("end", translation.text)
        except ValueError:
            result_text.delete(1.0, "end")
            result_text.insert("end", "Invalid languages")
    else:
        result_text.delete(1.0, "end")
        result_text.insert("end", "Languages not found")

def get_language_code(language):
    for code, lang in LANGUAGES.items():
        if lang.lower() == language.lower():
            return code
    return None

root = Tk()
root.title("Translator")
root.geometry("400x400")

source_lang_label = Label(root, text="Select source language:")
source_lang_label.pack(pady=10)

source_lang_var = StringVar(root)
source_lang_var.set("Select Language")
source_lang_dropdown = ttk.Combobox(root, textvariable=source_lang_var, values=list(LANGUAGES.values()), state="readonly")
source_lang_dropdown.pack(pady=5)

target_lang_label = Label(root, text="Select target language:")
target_lang_label.pack(pady=10)

target_lang_var = StringVar(root)
target_lang_var.set("Select Language")
target_lang_dropdown = ttk.Combobox(root, textvariable=target_lang_var, values=list(LANGUAGES.values()), state="readonly")
target_lang_dropdown.pack(pady=5)

text_label = Label(root, text="Enter text to translate:")
text_label.pack(pady=10)

text_entry = Entry(root, font=('Arial', 10))
text_entry.pack(pady=5)

translate_button = Button(root, text="Translate", command=translate_text, font=('Arial', 12), bg='green', fg='white')
translate_button.pack(pady=10)

result_label = Label(root, text="Translation:", font=('Arial', 12))
result_label.pack(pady=10)

result_text = Text(root, height=5, width=50, font=('Arial', 10))
result_text.pack(pady=5)

root.mainloop()
