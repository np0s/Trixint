import tkinter as tk
from tkinter import messagebox
import threading
from modules.username_recon import check_username, open_profiles
from modules.phone_recon import parse_phone_number

PASTEL_BG = "#e9d6f7"
PASTEL_PANEL = "#f6e6fb"
PASTEL_ACCENT = "#b6baff"
PASTEL_BUTTON = "#f7c6e0"
PASTEL_BUTTON_ACTIVE = "#e0b3d6"
PASTEL_ENTRY = "#e3eaff"
PASTEL_TEXT = "#7a6fa1"
PASTEL_HEADER = "#d1c4e9"
PASTEL_ICON = "#a3e3e4"

class CuteButton(tk.Button):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.configure(
            font=("Comic Sans MS", 13, "bold"),
            bg=PASTEL_BUTTON,
            fg=PASTEL_TEXT,
            activebackground=PASTEL_BUTTON_ACTIVE,
            activeforeground=PASTEL_TEXT,
            relief="flat",
            bd=0,
            cursor="hand2",
            padx=18,
            pady=6,
            highlightthickness=0
        )
        self.bind("<Enter>", lambda e: self.config(bg=PASTEL_BUTTON_ACTIVE))
        self.bind("<Leave>", lambda e: self.config(bg=PASTEL_BUTTON))

class CuteEntry(tk.Entry):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.configure(
            font=("Comic Sans MS", 12),
            bg=PASTEL_ENTRY,
            fg=PASTEL_TEXT,
            relief="flat",
            bd=0,
            highlightthickness=2,
            highlightbackground=PASTEL_ACCENT,
            highlightcolor=PASTEL_ACCENT,
            insertbackground=PASTEL_TEXT
        )

class TrixintCuteGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Trixint")
        self.root.geometry("450x600")
        self.root.resizable(False, False)
        self.root.configure(bg=PASTEL_BG)

        # Main rounded panel
        self.panel = tk.Frame(root, bg=PASTEL_PANEL, bd=0, highlightthickness=0)
        self.panel.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=410, height=540)
        self.panel.pack_propagate(False)

        # Header
        self.header = tk.Frame(self.panel, bg=PASTEL_HEADER, bd=0, highlightthickness=0)
        self.header.pack(fill=tk.X, pady=(18, 10), padx=18)
        tk.Label(self.header, text="Trixint", font=("Comic Sans MS", 28, "bold"), fg=PASTEL_ACCENT, bg=PASTEL_HEADER).pack(side=tk.LEFT, padx=(0, 8))
        tk.Label(self.header, text="🔍", font=("Arial", 26), bg=PASTEL_HEADER).pack(side=tk.LEFT)

        # Username Scan
        self.section(self.panel, "😊 Username Scan", "Enter username", self.username_search, 0)
        # Phone Recon
        self.section(self.panel, "📞 Phone Recon", "Enter phone number", self.phone_search, 1)

        # Results area
        self.result_box = tk.Text(self.panel, height=8, font=("Comic Sans MS", 11), bg=PASTEL_ENTRY, fg=PASTEL_TEXT, relief="flat", bd=0, wrap=tk.WORD)
        self.result_box.pack(fill=tk.BOTH, expand=True, padx=24, pady=(10, 18))
        self.result_box.config(state=tk.DISABLED)

        # Store last username results for open_profiles
        self.last_username = None
        self.last_results = None

    def section(self, parent, label, placeholder, command, idx):
        # Section frame
        s = tk.Frame(parent, bg=PASTEL_PANEL)
        s.pack(fill=tk.X, padx=24, pady=(10 if idx==0 else 0, 0))
        # Label
        tk.Label(s, text=label, font=("Comic Sans MS", 15, "bold"), fg=PASTEL_TEXT, bg=PASTEL_PANEL).pack(anchor=tk.W, pady=(0, 4))
        # Entry + Button
        row = tk.Frame(s, bg=PASTEL_PANEL)
        row.pack(fill=tk.X)
        entry = CuteEntry(row, width=22)
        entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        entry.insert(0, placeholder)
        entry.bind("<FocusIn>", lambda e, ent=entry, ph=placeholder: self._clear_placeholder(ent, ph))
        entry.bind("<FocusOut>", lambda e, ent=entry, ph=placeholder: self._add_placeholder(ent, ph))
        btn = CuteButton(row, text="Search", command=lambda ent=entry: command(ent.get().strip()))
        btn.pack(side=tk.LEFT)
        # Save for later
        if idx == 0:
            self.username_entry = entry
        else:
            self.phone_entry = entry

    def _clear_placeholder(self, entry, placeholder):
        if entry.get() == placeholder:
            entry.delete(0, tk.END)
            entry.config(fg=PASTEL_TEXT)

    def _add_placeholder(self, entry, placeholder):
        if not entry.get():
            entry.insert(0, placeholder)
            entry.config(fg=PASTEL_TEXT)

    def username_search(self, username):
        if not username or username == "Enter username":
            messagebox.showwarning("Missing Username", "Please enter a username.")
            return
        self.result_box.config(state=tk.NORMAL)
        self.result_box.delete(1.0, tk.END)
        self.result_box.insert(tk.END, f"Searching for username: {username}...\n")
        self.result_box.config(state=tk.DISABLED)
        threading.Thread(target=self._username_thread, args=(username,), daemon=True).start()

    def _username_thread(self, username):
        try:
            results = check_username(username)
            self.last_username = username
            self.last_results = results
            found = [site for site, ok in results.items() if ok]
            notfound = [site for site, ok in results.items() if not ok]
            out = f"\nFound on {len(found)} sites:\n" + "\n".join(f"✅ {site}" for site in found)
            out += f"\n\nNot found on {len(notfound)} sites:\n" + "\n".join(f"❌ {site}" for site in notfound)
            self._update_result_box(out)
            # Add open button if found
            if found:
                self.result_box.config(state=tk.NORMAL)
                self.result_box.insert(tk.END, "\n\n")
                open_btn = CuteButton(self.panel, text="Open Found Profiles", command=self.open_found_profiles)
                self.result_box.window_create(tk.END, window=open_btn)
                self.result_box.config(state=tk.DISABLED)
        except Exception as e:
            self._update_result_box(f"Error: {e}")

    def open_found_profiles(self):
        if self.last_results and self.last_username:
            open_profiles(self.last_results, self.last_username)

    def phone_search(self, number):
        if not number or number == "Enter phone number":
            messagebox.showwarning("Missing Number", "Please enter a phone number.")
            return
        self.result_box.config(state=tk.NORMAL)
        self.result_box.delete(1.0, tk.END)
        self.result_box.insert(tk.END, f"Analyzing phone number: {number}...\n")
        self.result_box.config(state=tk.DISABLED)
        threading.Thread(target=self._phone_thread, args=(number,), daemon=True).start()

    def _phone_thread(self, number):
        try:
            info = parse_phone_number(number)
            if 'error' in info:
                out = f"❌ {info['error']}"
            else:
                out = (f"\nCountry: {info.get('country','?')}\nRegion: {info.get('region','?')}\nCarrier: {info.get('carrier','?')}\nType: {info.get('type','?')}\nValid: {'Yes' if info.get('valid') else 'No'}\nPossible: {'Yes' if info.get('possible') else 'No'}")
            self._update_result_box(out)
        except Exception as e:
            self._update_result_box(f"Error: {e}")

    def _update_result_box(self, text):
        self.result_box.config(state=tk.NORMAL)
        self.result_box.delete(1.0, tk.END)
        self.result_box.insert(tk.END, text)
        self.result_box.config(state=tk.DISABLED)

def run_gui():
    root = tk.Tk()
    app = TrixintCuteGUI(root)
    root.mainloop() 