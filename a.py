import tkinter as tk

def submit():
    selected_subjects = [subject.get() for subject in subject_checkbuttons if subject.get() == 1]
    print("Selected Subjects:", selected_subjects)

root = tk.Tk()
root.title("Subject Selection")

# Create subject selection checkboxes
subject_checkbuttons = []
subjects = ["Java", "Maths", "Agile Methodology", "UML", "Merise","prob and stats","web programming"]
for i, subject in enumerate(subjects):
    subject_var = tk.IntVar()
    subject_checkbutton = tk.Checkbutton(root, text=subject, variable=subject_var)
    subject_checkbutton.grid(row=i, column=0, sticky="w")
    subject_checkbuttons.append(subject_var)
# Submit button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.grid(row=len(subjects), column=0, pady=10)

root.mainloop()
