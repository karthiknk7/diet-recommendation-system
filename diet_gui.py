import tkinter as tk
from tkinter import ttk, messagebox
from diet_plans import weight_loss_diet, weight_gain_diet, maintain_diet

def calculate_bmi(weight, height):
    return round(weight / ((height / 100) ** 2), 2)

def calculate_bmr(weight, height, age, gender, activity_level):
    if gender.lower() == "male":
        bmr = 88.36 + (13.4 * weight) + (4.8 * height) - (5.7 * age)
    else:
        bmr = 447.6 + (9.2 * weight) + (3.1 * height) - (4.3 * age)

    activity_multiplier = {"Low": 1.2, "Moderate": 1.55, "High": 1.9}
    return round(bmr * activity_multiplier.get(activity_level, 1.2), 2)

def recommend_diet(goal):
    if goal == "Weight Loss":
        return weight_loss_diet()
    elif goal == "Weight Gain":
        return weight_gain_diet()
    else:
        return maintain_diet()

def generate_diet():
    try:
        age = int(age_entry.get())
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        gender = gender_var.get()
        activity = activity_var.get()
        goal = goal_var.get()

        bmi = calculate_bmi(weight, height)
        calories = calculate_bmr(weight, height, age, gender, activity)
        diet = recommend_diet(goal)

        result_text = f"Your BMI: {bmi}\nCalories Needed: {calories} kcal\n\nDIET PLAN:\n"
        for meal, food in diet.items():
            result_text += f"{meal}: {food}\n"

        result_label.config(text=result_text)

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")

root = tk.Tk()
root.title("Diet Recommendation System")
root.geometry("500x600")

tk.Label(root, text="Diet Recommendation System", font=("Arial", 16, "bold")).pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=10)

for label in ["Age", "Weight (kg)", "Height (cm)"]:
    tk.Label(frame, text=label).pack()
    entry = tk.Entry(frame)
    entry.pack()
    if label == "Age":
        age_entry = entry
    elif label == "Weight (kg)":
        weight_entry = entry
    else:
        height_entry = entry

gender_var = tk.StringVar(value="Male")
tk.Label(frame, text="Gender").pack()
ttk.Combobox(frame, textvariable=gender_var, values=["Male", "Female"]).pack()

activity_var = tk.StringVar(value="Moderate")
tk.Label(frame, text="Activity Level").pack()
ttk.Combobox(frame, textvariable=activity_var, values=["Low", "Moderate", "High"]).pack()

goal_var = tk.StringVar(value="Maintain")
tk.Label(frame, text="Fitness Goal").pack()
ttk.Combobox(frame, textvariable=goal_var, values=["Weight Loss", "Weight Gain", "Maintain"]).pack()

tk.Button(root, text="Generate Diet Plan", command=generate_diet, bg="green", fg="white").pack(pady=15)

result_label = tk.Label(root, text="", justify="left")
result_label.pack()

root.mainloop()
