import tkinter as tk
from tkinter import messagebox
import csv

# ---------------- LOAD CSV ----------------
courses = []

try:
    with open("coursera_course_2024.csv", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        headers = reader.fieldnames

        # Auto detect columns
        title_col = None
        rating_col = None
        org_col = None

        for h in headers:
            hl = h.lower()
            if "title" in hl:
                title_col = h
            elif "rating" in hl:
                rating_col = h
            elif "org" in hl or "university" in hl or "partner" in hl:
                org_col = h

        for row in reader:
            courses.append(row)

except Exception as e:
    messagebox.showerror("Error", "CSV file not found!")
    exit()

# ---------------- GUI ----------------
root = tk.Tk()
root.title("High-Rated Course Recommendation System")
root.geometry("900x550")

tk.Label(
    root,
    text="High-Rated Skill-Based Course Recommendation",
    font=("Arial", 18, "bold")
).pack(pady=10)

tk.Label(root, text="Enter the skill you want to learn:").pack()
skill_entry = tk.Entry(root, width=40)
skill_entry.pack(pady=5)

info = tk.Label(
    root,
    text="Only top-rated courses are recommended to improve learner quality.",
    fg="gray"
)
info.pack(pady=5)

output = tk.Text(root, height=20, width=110)
output.pack(pady=10)

# ---------------- SEARCH FUNCTION ----------------
def search_courses():
    output.delete("1.0", tk.END)

    skill = skill_entry.get().strip().lower()

    if skill == "":
        messagebox.showerror("Input Error", "Please enter a skill")
        return

    results = []

    for course in courses:
        text = " ".join(str(v).lower() for v in course.values())

        if skill in text:
            try:
                rating = float(course.get(rating_col, 0))
            except:
                rating = 0.0

            results.append((course, rating))

    if not results:
        output.insert(tk.END, "No courses found for this skill.\n")
        return

    # Sort by rating (highest first)
    results.sort(key=lambda x: x[1], reverse=True)

    output.insert(
        tk.END,
        f"Top High-Rated Courses for '{skill.title()}':\n"
        + "-" * 50 + "\n\n"
    )

    # Show TOP 8 only (clean UI)
    for i, (course, rating) in enumerate(results[:8], start=1):
        output.insert(
            tk.END,
            f"{i}. {course.get(title_col)}\n"
            f"   Organization : {course.get(org_col, 'N/A')}\n"
            f"   Rating       : {course.get(rating_col, 'N/A')}\n\n"
        )

# ---------------- BUTTON ----------------
tk.Button(
    root,
    text="Search Courses",
    command=search_courses,
    bg="green",
    fg="white",
    font=("Arial", 11, "bold")
).pack(pady=5)

root.mainloop()
