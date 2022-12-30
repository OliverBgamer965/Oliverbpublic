import tkinter as tk
import random


# Create the main window
window = tk.Tk()

# Set the window title
window.title("Clicker Game By OBI")

# Create a counter variable
counter = 0

# Define a function to move the button and increment the counter
def move_button():
    global counter
    counter += 1
    label.config(text=str(counter))
    
    # Generate random x and y coordinates
    x = random.randint(0, window.winfo_width())
    y = random.randint(0, window.winfo_height())
    
    # Move the button to the new coordinates
    button.place(x=x, y=y)

# Define a function to update the timer label
def update_timer():
    global timer
    timer -= 1
    timer_label.config(text=str(timer))
    if timer > 0:
        # Schedule another update in 1000 milliseconds (1 second)
        window.after(1000, update_timer)
    else:
        # Disable the button and display a message
        button.config(state="disabled")
        timer_label.config(text="You clicked the button {} times!".format(counter))

# Create a button widget
button = tk.Button(text="Click Me!", command=move_button, font=("Helvetica", 10))

# Create a label widget to display the counter
label = tk.Label(text="0", font=("Helvetica", 25))

# Create a label widget to display the timer
timer_label = tk.Label(text="10", font=("Helvetica", 25))

# Pack the widgets into the window
button.pack()
label.pack()
timer_label.pack()

# Set the timer to 30 seconds
timer = 30

# Start the timer
update_timer()

# Set the background color to red
window.config(bg="black")

# Disable resizing of the window
window.resizable(False, False)

# Set the window to full screen
window.attributes("-fullscreen", True)

# Define a function to display the high scores
def show_high_scores():
    # Create a new window to display the high scores
    scores_window = tk.Tk()
    scores_window.title("High Scores")
    
    # Create a listbox widget to display the high scores
    scores_list = tk.Listbox(scores_window)
    
    # Insert the high scores into the listbox
    scores_list.insert(tk.END, "Player 1: 100")
    scores_list.insert(tk.END, "Player 2: 90")
    scores_list.insert(tk.END)

# Run the main loop
window.mainloop()