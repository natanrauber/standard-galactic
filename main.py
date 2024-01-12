import tkinter as tk
from ctypes import byref, c_int, sizeof, windll
import clipboard

# Initialize Tkinter
root = tk.Tk()
root.title("Standard Galactic")
root.iconbitmap("icon.ico")
root.configure(bg='black')

HWND = windll.user32.GetParent(root.winfo_id())
windll.dwmapi.DwmSetWindowAttribute(HWND, 35, byref(c_int(0x00800080)), sizeof(c_int))
windll.dwmapi.DwmSetWindowAttribute(HWND, 36, byref(c_int(0x00FFFFFF)), sizeof(c_int))
windll.dwmapi.DwmSetWindowAttribute(HWND, 34, byref(c_int(0x00FF00FF)), sizeof(c_int))

class GalacticAlphabetConverter:
    def __init__(self, master):
        self.master = master

        # output frame
        output_frame = tk.Frame(master)
        output_frame.configure(bg='black')
        output_frame.pack(padx=10, pady=10)

        # output text
        self.text_output = tk.Text(output_frame, wrap=tk.WORD, width=40, height=5)
        self.text_output.configure(
            bg='black',
            fg='white',
            insertbackground='#F0F',
            highlightbackground="#F0F",
            highlightcolor="#F0F",
            highlightthickness=1,
            bd=0,
            state=tk.DISABLED,  # Set the state to DISABLED to prevent direct editing
        )
        self.text_output.pack(side=tk.TOP)

        # output buttons frame
        output_buttons_frame = tk.Frame(output_frame)
        output_buttons_frame.configure(bg='black')
        output_buttons_frame.pack(side=tk.BOTTOM, pady=10)

        # clear button
        clear_button_frame = tk.Frame(output_buttons_frame)
        clear_button_frame.configure(bg='#F0F')
        clear_button_frame.pack(side=tk.LEFT, padx=5)
        self.clear_button = tk.Button(clear_button_frame, text="Clear", width=10, command=self.clear_output)
        self.clear_button.configure(
            bg='#800080',
            fg='white',
            activebackground='black',
            activeforeground='white',
            highlightbackground="#F0F",
            highlightcolor="#F0F",
            highlightthickness=1,
            bd=0,
        )
        self.clear_button.pack(padx=1, pady=1)

        # copy button
        copy_button_frame = tk.Frame(output_buttons_frame)
        copy_button_frame.configure(bg='#F0F')
        copy_button_frame.pack(side=tk.RIGHT, padx=5)
        self.copy_button = tk.Button(copy_button_frame, text="Copy", width=10, command=self.copy_to_clipboard)
        self.copy_button.configure(
            bg='#800080',
            fg='white',
            activebackground='black',
            activeforeground='white',
            highlightbackground="#F0F",
            highlightcolor="#F0F",
            highlightthickness=1,
            bd=0,
        )
        self.copy_button.pack(padx=1, pady=1)

        # input frame
        input_frame = tk.Frame(master)
        input_frame.configure(bg='black')
        input_frame.pack(padx=10, pady=10)

        # input text entry label
        self.text_entry_label = tk.Label(input_frame, text="Enter the text:")
        self.text_entry_label.configure(bg='black', fg='white')
        self.text_entry_label.pack()

        # input text entry
        self.text_entry = tk.Entry(input_frame, width=40)
        self.text_entry.configure(
            bg='black',
            fg='white',
            insertbackground='#F0F',
            highlightbackground = "#F0F",
            highlightcolor= "#F0F",
            highlightthickness=1,
            bd=0,
        )
        self.text_entry.pack()

        # input buttons frame
        input_buttons_frame = tk.Frame(input_frame)
        input_buttons_frame.configure(bg='black')
        input_buttons_frame.pack(pady=10)

        # encode button
        encode_button_frame = tk.Frame(input_buttons_frame)
        encode_button_frame.configure(bg='#F0F')
        encode_button_frame.pack(side=tk.LEFT, padx=5)
        self.encode_button = tk.Button(encode_button_frame, text="Encode", width=10, command=self.encode)
        self.encode_button.configure(
            bg='#800080',
            fg='white',
            activebackground='black',
            activeforeground='white',
            highlightbackground = "#F0F",
            highlightcolor= "#F0F",
            highlightthickness=1,
            bd=0,
        )
        self.encode_button.pack(padx=1, pady=1)

        # decode button
        decode_button_frame = tk.Frame(input_buttons_frame)
        decode_button_frame.configure(bg='#F0F')
        decode_button_frame.pack(side=tk.RIGHT, padx=5)
        self.decode_button = tk.Button(decode_button_frame, text="Decode", width=10, command=self.decode)
        self.decode_button.configure(
            bg='#800080',
            fg='white',
            activebackground='black',
            activeforeground='white',
            highlightbackground = "#F0F",
            highlightcolor= "#F0F",
            highlightthickness=1,
            bd=0,
        )
        self.decode_button.pack(padx=1, pady=1)

    def encode(self):
        english_text = self.text_entry.get().lower().replace('\n', ' ')
        galactic_text = self.convert_to_galactic(english_text)
        self.add_line(galactic_text)

    def decode(self):
        galactic_text = self.text_entry.get().replace('\n', ' ')
        english_text = self.convert_to_english(galactic_text)
        self.add_line(english_text)

    def convert_to_galactic(self, english_text):
        # Create a dictionary mapping English letters to Galactic letters
        mapping = {
            'a': 'ᔑ',
            'b': 'ʖ',
            'c': 'ᓵ',
            'd': '↸',
            'e': 'ᒷ',
            'f': '⎓',
            'g': '⊣',
            'h': '⍑',
            'i': '╎',
            'j': '⋮',
            'k': 'ꖌ',
            'l': 'ꖎ',
            'm': 'ᒲ',
            'n': 'リ',
            'o': '𝙹',
            'p': '!¡',
            'q': 'ᑑ',
            'r': '∷',
            's': 'ᓭ',
            't': 'ℸ ̣',
            'u': '⚍',
            'v': '⍊',
            'w': '∴',
            'x':' ̇/',
            'y': '‖',
            'z': '⨅',
        }
        galactic_text = english_text
        for key, value in mapping.items():
            galactic_text = galactic_text.replace(key, value)
        return galactic_text

    def convert_to_english(self, galactic_text):
        # Create a dictionary mapping Galactic letters to English letters
        reverse_mapping = {
            'ᔑ': 'a',
            'ᖋ': 'a',
            'ʖ': 'b',
            'ᓵ': 'c',
            'ᔮ': 'c',
            '↸': 'd',
            'ᒷ': 'e',
            '⎓': 'f',
            '⊣': 'g',
            '˧': 'g',
            '⍑': 'h',
            '₸': 'h',
            '╎': 'i',
            '¦': 'i',
            '⋮': 'j',
            'ꖌ': 'k',
            'ꖎ': 'l',
            'ᒲ': 'm',
            'リ': 'n',
            '𝙹': 'o',
            'ᒍ': 'o',
            '!¡': 'p',
            'ᑑ': 'q',
            '∷': 'r',
            '∷': 'r',
            'ᓭ': 's',
            'ℸ ̣': 't',
            'ℸ': 't',
            'ᒣ': 't',
            '⚍': 'u',
            '⍊': 'v',
            '∴': 'w',
            '̇/̇': 'x',
            ' ̇/': 'x',
            '̇/': 'x',
            '||': 'y',
            'ǁ': 'y',
            '‖': 'y',
            '⨅': 'z',
        }

        english_text = galactic_text
        for key, value in reverse_mapping.items():
            english_text = english_text.replace(key, value)
        return english_text

    def add_line(self, line):
        # Add a line to the text output and remove the oldest line if there are more than 5 lines
        current_content = self.text_output.get("1.0", tk.END)
        lines = current_content.split("\n")[:-1]  # Remove the last empty line
        if len(lines) >= 2:
            # Remove the oldest line
            self.text_output.config(state=tk.NORMAL)  # Enable editing temporarily
            self.text_output.delete("1.0", f"{len(lines[0]) + 1}.{len(lines[1])}")
            self.text_output.config(state=tk.DISABLED)  # Disable editing again
        # Add the new line
        self.text_output.config(state=tk.NORMAL)  # Enable editing temporarily
        self.text_output.insert(tk.END, f"{line}\n")
        self.text_output.config(state=tk.DISABLED)  # Disable editing again

    def clear_output(self):
        # Clear the content of the Text widget
        self.text_output.config(state=tk.NORMAL)  # Enable editing temporarily
        self.text_output.delete("1.0", tk.END)
        self.text_output.config(state=tk.DISABLED)  # Disable editing again

    def copy_to_clipboard(self):
        # Get the content of the Text widget
        output_text = self.text_output.get("1.0", tk.END).strip()

        # Copy the content to the clipboard
        clipboard.copy(output_text)


if __name__ == "__main__":
    app = GalacticAlphabetConverter(root)
    root.mainloop()
