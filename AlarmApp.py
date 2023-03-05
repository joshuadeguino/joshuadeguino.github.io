import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import time
import winsound

class AlarmApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Alarm App")

    # Create main frame
    self.main_frame = ttk.Frame(master, padding=20)
    self.main_frame.grid()

    # Create label for alarm time input
    self.alarm_label = ttk.Label(self.main_frame, text="Alarm Time (HH:MM:SS):")
    self.alarm_label.grid(row=0, column=0, sticky="w")

    # Create entry widget for alarm time input
    self.alarm_entry = ttk.Entry(self.main_frame, width=10)
    self.alarm_entry.grid(row=0, column=1, padx=10, pady=10)

    # Create label for task input
    self.task_label = ttk.Label(self.main_frame, text="Task:")
    self.task_label.grid(row=1, column=0, sticky="w")

    # Create entry widget for task input
    self.task_entry = ttk.Entry(self.main_frame, width=30)
    self.task_entry.grid(row=1, column=1, padx=10, pady=10)

    # Create button to set the alarm
    self.set_button = ttk.Button(self.main_frame, text="Set Alarm", command=self.set_alarm)
    self.set_button.grid(row=2, column=1, pady=10)

    # Create listbox to display alarms
    self.alarm_listbox = tk.Listbox(self.main_frame, height=5)
    self.alarm_listbox.grid(row=3, column=1, padx=10, pady=10)

    # Create label for the alarm list
    self.list_label = ttk.Label(self.main_frame, text="List of Alarms:")
    self.list_label.grid(row=3, column=0, sticky="w")

def set_alarm(self):
    # Get the alarm time and task from the input fields
    alarm_time = self.alarm_entry.get()
    task = self.task_entry.get()

    # Add the alarm to the listbox
    self.alarm_listbox.insert(tk.END, f"{alarm_time} - {task}")

    # Get the current time
    current_time = time.strftime("%H:%M:%S")

    # Compute the number of seconds until the alarm time
    alarm_seconds = self.get_time_seconds(alarm_time)
    current_seconds = self.get_time_seconds(current_time)
    wait_time = alarm_seconds - current_seconds

    # Schedule the alarm to trigger at the specified time
    self.master.after(wait_time * 1000, lambda: self.trigger_alarm(task))

def get_time_seconds(self, time_str):
    # Convert a time string in HH:MM:SS format to the number of seconds since midnight
    hours, minutes, seconds = map(int, time_str.split(':'))
    return hours * 3600 + minutes * 60 + seconds

def trigger_alarm(self, task):
    # Display a message with the task name
    message = f"ALARM! Time to work on: {task}"
    messagebox.showinfo("Alarm", message)

    # Play a sound to alert the user
    winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)

    # Remove the alarm from the listbox
    self.alarm_listbox.delete(0)

# Create the main window
root = tk.Tk()

# Set window size and style
root.geometry("500x300")
root.configure(bg="#f0f0f0")
style = ttk.Style()
style.theme_use("clam")

# Create an instance of the AlarmApp class
app = AlarmApp(root)

# Start the application
root.mainloop()
