import pandas as pd
import random
import winsound  # Windows-specific library for playing audio
import pygame

# Replace "your_file.xlsx" with the actual name of your Excel file
file_path = "D:\\PATH TO\\CFA May 2024 Quiz Questions.xlsx"

correct_sound = "D:\\PATH TO\\two_tone_up_clicky.wav"
incorrect_sound = "D:\\PATH TO\\oof.mp3"

# Read the data from the Excel sheet
data = pd.read_excel(file_path)

# Separate questions and answers into lists
questions = data["Question"].tolist()
answers = data["Answer"].tolist()

# Shuffle the questions and answers together
combined = list(zip(questions, answers))
random.shuffle(combined)

# Separate shuffled questions and answers
questions, answers = zip(*combined)

# Initialize Pygame for MP3 playback
pygame.init()

# Replace non-breaking spaces with regular spaces
answers = [answer.replace(' ', ' ') for answer in answers]

# Loop through each question and answer
for i, question in enumerate(questions):
    user_answer = input(f"{question}: ")

    # Handle spacing and case-insensitivity
    stripped_user_answer = " ".join(user_answer.lower().split()).strip()
    stripped_correct_answer = " ".join(answers[i].lower().split()).strip()

    # Compare after handling spacing and case
    if stripped_user_answer == stripped_correct_answer:
        print("YOU'RE A WALKING BLOOMBER TERMINAL!")
        winsound.PlaySound(correct_sound, winsound.SND_FILENAME)
    else:
        print("oof.")
        # Reveal the correct answer
        print(f"The correct answer is: {answers[i]}.")
        # Play MP3 using Pygame
        incorrect_sound_obj = pygame.mixer.Sound(incorrect_sound)
        incorrect_sound_obj.play()
        # Wait for the sound to finish
        while pygame.mixer.get_busy():
            pygame.time.wait(100)

# End message
print("You've answered all questions!")

# Quit Pygame after use
pygame.quit()