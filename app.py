from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def home():
    subjects = ['Python', 'Maths', 'Agile Methodology', 'Java', 'Database Admin']
    return render_template('index.html', subjects=subjects)
from flask import Flask, render_template
@app.route('/')
def home():
    subjects = ['Python', 'Maths', 'Agile Methodology', 'Java', 'Database Admin','platform and dev tool', 'UML', 'Merise', 'Web Programming','DB Implementation']
    return render_template('index.html', subjects=subjects)
import tkinter as tk

def handle_subject_selection(subject):
    print(f"Selected subject: {subject}")

root = tk.Tk()

# Create the navbar frame
navbar_frame = tk.Frame(root)
navbar_frame.pack()

# List of subjects
subjects = ['Python', 'Maths', 'Agile Methodology', 'Java', 'Database Admin']

# Create buttons for each subject
for subject in subjects:
    button = tk.Button(navbar_frame, text=subject, command=lambda s=subject: handle_subject_selection(s))
    button.pack(side=tk.LEFT)

root.mainloop()