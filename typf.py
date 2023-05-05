import tkinter as tk
import random
import time

# List of sentences for the game
sentences = ["The quick brown fox jumps over the lazy dog",
             "Python is an interpreted high-level programming language",
             "I'm learning to code with Python and it's fun",
             "A journey of a thousand miles begins with a single step",
             "Coding is not just about algorithms, it's about logic"]

# Initialize the game
score = 0
start_time = 0
sentence = random.choice(sentences)

# Function to start the game
def start_game():
    global start_time, sentence
    start_time = time.time()
    sentence_label.config(text=sentence)
    input_box.delete(0, tk.END)
    input_box.focus()

# Function to handle submission of score
def submit_score():
    global score, sentence
    end_time = time.time()
    time_taken = round(end_time - start_time, 2)
    if input_box.get() == sentence:
        score += 1
        result_label.config(text=f"Correct! Time taken: {time_taken} seconds")
    else:
        result_label.config(text=f"Incorrect. Time taken: {time_taken} seconds")
    wpm = calculate_wpm(time_taken, len(sentence))
    wpm_label.config(text=f"WPM: {wpm}")
    sentence = random.choice(sentences)
    start_game()

# Function to calculate WPM
def calculate_wpm(time_taken, sentence_length):
    minutes = time_taken / 60
    wpm = (sentence_length / 5) / minutes
    return round(wpm)

# Initialize the GUI
root = tk.Tk()
root.geometry("600x200")
root.iconbitmap('typeracer.ico')
root.configure(bg='ivory2')
root.title("TypeRacer")

# Create the widgets
sentence_label = tk.Label(root, text=sentence, font=("Arial", 16),bg='ivory2')
input_box = tk.Entry(root, font=("Arial", 16))
submit_button = tk.Button(root, text="Submit", font=("Arial", 16), command=submit_score,bg="olivedrab1")
exit_button = tk.Button(root, text="Exit", font=("Arial", 16), command=root.destroy,bg="indianred1")
result_label = tk.Label(root, font=("Arial", 16),bg='ivory2')
wpm_label = tk.Label(root, font=("Arial", 16),bg='ivory2')

# Add the widgets to the GUI
sentence_label.pack(pady=10)
input_box.pack(pady=10)
submit_button.pack(side=tk.LEFT, padx=10, pady=10)
exit_button.pack(side=tk.RIGHT, padx=10, pady=10)
result_label.pack(pady=10)
wpm_label.pack(pady=10)

# Start the game
start_game()

# Start the GUI event loop
root.mainloop()
