import tkinter as tk
from tkinter import messagebox
import random


all_questions = [
  {"question": "What is the capital of Gujarat?", "options": ["Surat", "Vadodara", "Ahmedabad", "Gandhinagar"], "answer": "Gandhinagar"},
  {"question": "Which river flows through Ahmedabad?", "options": ["Ganga", "Sabarmati", "Narmada", "Tapi"], "answer": "Sabarmati"},
  {"question": "Who is known as the Iron Man of India?", "options": ["Mahatma Gandhi", "Jawaharlal Nehru", "Sardar Vallabhbhai Patel", "Subhas Chandra Bose"], "answer": "Sardar Vallabhbhai Patel"},
  {"question": "Where was Mahatma Gandhi born?", "options": ["Nadiad", "Surat", "Porbandar", "Ahmedabad"], "answer": "Porbandar"},
  {"question": "Gir National Park is famous for which animal?", "options": ["Tiger", "Lion", "Elephant", "Leopard"], "answer": "Lion"},
  {"question": "Ahmedabad is located on which bank of the Sabarmati river?", "options": ["East", "West", "North", "South"], "answer": "West"},
  {"question": "What is the official language of Gujarat?", "options": ["Hindi", "English", "Gujarati", "Marathi"], "answer": "Gujarati"},
  {"question": "Which is the largest city in Gujarat by population?", "options": ["Surat", "Vadodara", "Ahmedabad", "Rajkot"], "answer": "Ahmedabad"},
  {"question": "What is the famous dance form of Gujarat?", "options": ["Kathak", "Bharatnatyam", "Garba", "Kuchipudi"], "answer": "Garba"},
  {"question": "Statue of Unity is located near which river?", "options": ["Narmada", "Tapi", "Sabarmati", "Mahi"], "answer": "Narmada"},
  {"question": "Which industry is Ahmedabad famous for?", "options": ["Shipbuilding", "Textile", "IT", "Oil"], "answer": "Textile"},
  {"question": "Who was the first Chief Minister of Gujarat?", "options": ["Narendra Modi", "Madhavsinh Solanki", "Chimanbhai Patel", "Jivraj Mehta"], "answer": "Jivraj Mehta"},
  {"question": "Which institute in Ahmedabad was established by Vikram Sarabhai?", "options": ["Gujarat University", "IIM Ahmedabad", "CEPT University", "Physical Research Laboratory (PRL)"], "answer": "Physical Research Laboratory (PRL)"},
  {"question": "In which year was Gujarat formed as a separate state?", "options": ["1947", "1950", "1960", "1972"], "answer": "1960"},
  {"question": "Which city is known as the Diamond City of Gujarat?", "options": ["Ahmedabad", "Surat", "Vadodara", "Junagadh"], "answer": "Surat"},
  {"question": "Kankaria Lake is located in which city?", "options": ["Surat", "Rajkot", "Ahmedabad", "Bhavnagar"], "answer": "Ahmedabad"},
  {"question": "Traditional male attire during Navratri in Gujarat?", "options": ["Kurta-Pajama", "Dhoti-Kurta", "Kediyu and Chorno", "Sherwani"], "answer": "Kediyu and Chorno"},
  {"question": "Which temple is located in Dwarka?", "options": ["Somnath Temple", "Dwarkadhish Temple", "Akshardham Temple", "Ambaji Temple"], "answer": "Dwarkadhish Temple"},
  {"question": "Who established Sabarmati Ashram?", "options": ["Sardar Patel", "Jawaharlal Nehru", "Mahatma Gandhi", "Lokmanya Tilak"], "answer": "Mahatma Gandhi"},
  {"question": "Which city is known as Sanskari Nagari?", "options": ["Surat", "Vadodara", "Rajkot", "Jamnagar"], "answer": "Vadodara"},
  {"question": "Which fort is located in Junagadh?", "options": ["Raigad Fort", "Red Fort", "Uparkot Fort", "Chittorgarh Fort"], "answer": "Uparkot Fort"},
  {"question": "Which is the famous stepwell in Patan?", "options": ["Adalaj Vav", "Rani ki Vav", "Agrasen ki Baoli", "Dada Harir Vav"], "answer": "Rani ki Vav"},
  {"question": "Which major port is located in Gujarat?", "options": ["Mumbai Port", "Kandla Port", "Chennai Port", "Kochi Port"], "answer": "Kandla Port"},
  {"question": "What is the state animal of Gujarat?", "options": ["Asiatic Lion", "Tiger", "Leopard", "Nilgai"], "answer": "Asiatic Lion"},
  {"question": "Who built Akshardham Temple in Gandhinagar?", "options": ["ISKCON", "BAPS", "Art of Living", "RSS"], "answer": "BAPS"}
]

questions = random.sample(all_questions, 25)


class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Quiz App")
        self.root.geometry("650x500")
        self.root.config(bg="#B2EAF8")
        self.current_q = 0
        self.score = 0
        self.total_questions = len(questions)

        self.header_frame = None
        self.info_label = None

        self.title_label = tk.Label(root, text=" Welcome to the Quiz!", font=("Arial", 22, "bold"),
                                    bg="#ECF0F1", fg="#2C3E50")
        self.title_label.pack(pady=30)

        self.start_button = tk.Button(root, text="Start Quiz", font=("Arial", 16), command=self.start_quiz,
                                      bg="#28B463", fg="white", padx=10, pady=5)
        self.start_button.pack()

    def start_quiz(self):
        self.start_button.destroy()
        self.title_label.destroy()
        self.setup_header()
        self.display_question()

    def setup_header(self):
        self.header_frame = tk.Frame(self.root, bg="#D6EAF8")
        self.header_frame.pack(fill="x", pady=5)

        self.info_label = tk.Label(self.header_frame, text="", font=("Arial", 14), bg="#D6EAF8", fg="#154360")
        self.info_label.pack(side="left", padx=10)

        self.quit_button = tk.Button(self.header_frame, text="Quit Game", font=("Arial", 12), bg="#E74C3C",
                                     fg="white", command=self.quit_game)
        self.quit_button.pack(side="right", padx=10)

    def update_header(self):
        attempted = self.current_q
        self.info_label.config(
            text=f"Total: {self.total_questions} | Attempted: {attempted} | Score: {self.score}"
        )

    def display_question(self):
        self.clear_screen(keep_header=True)
        self.update_header()

        q = questions[self.current_q]

        self.question_label = tk.Label(self.root, text=f"Q{self.current_q + 1}: {q['question']}",
                                       font=("Arial", 16), bg="#ECF0F1", wraplength=600, justify="left")
        self.question_label.pack(pady=20)

        self.selected_option = tk.StringVar()
        self.selected_option.set(None)

        self.options = []
        for option in q['options']:
            btn = tk.Radiobutton(self.root, text=option, variable=self.selected_option, value=option,
                                 font=("Arial", 14), bg="#ECF0F1", anchor="w", width=35, padx=20)
            btn.pack(pady=4)
            self.options.append(btn)

        self.next_button = tk.Button(self.root, text="Next", font=("Arial", 14),
                                     bg="#3498DB", fg="white", command=self.next_question)
        self.next_button.pack(pady=25)

    def next_question(self):
        if not self.selected_option.get():
            messagebox.showwarning("Warning", "Please select an option!")
            return

        if self.selected_option.get() == questions[self.current_q]["answer"]:
            self.score += 1

        self.current_q += 1

        if self.current_q < len(questions):
            self.display_question()
        else:
            self.show_result()

    def quit_game(self):
        confirm = messagebox.askyesno("Quit Quiz", "Are you sure you want to quit?\nYour score will be shown.")
        if confirm:
            self.show_result()

    def show_result(self):
        self.clear_screen(keep_header=False)

        result_text = f" Quiz Finished!\nYour Score: {self.score} / {self.current_q}"
        result_label = tk.Label(self.root, text=result_text, font=("Arial", 20, "bold"),
                                bg="#ECF0F1", fg="#1E8449")
        result_label.pack(pady=50)

        quit_btn = tk.Button(self.root, text="Exit", font=("Arial", 14), command=self.root.quit,
                             bg="#E74C3C", fg="white", padx=10, pady=5)
        quit_btn.pack()

    def clear_screen(self, keep_header=False):
        for widget in self.root.winfo_children():
            if keep_header and widget == self.header_frame:
                continue
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()