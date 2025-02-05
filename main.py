# pylint: disable=missing-docstring,line-too-long
# This will be my main file for my keylogger. I will import the other files here and run the program.
from datetime import datetime # timestamps
import random # shuffle questions
import utilities  # custom module

class KeyLogger:
    def __init__(self, username):
        # Sanitize username using custom module
        self.username = utilities.sanitize_input(username)
        # store keystrokes
        self.keystrokes = []
        # filename for logging
        self.filename = self.make_log_filename()

    def make_log_filename(self):
        # current time to make unique filename
        current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
        return f"keys_logged_{self.username}_{current_time}.txt"

    def record_key(self, key):
        # Sanitize the key input
        safe_key = utilities.sanitize_input(str(key))
        # adds each key press to our list
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{current_time}] Key: {safe_key}\n"
        self.keystrokes.append(log_entry)

    def save_log(self):
        # save
        try:
            with open(self.filename, 'w') as log_file:
                log_file.writelines(self.keystrokes)
            print(f"Saved log to {self.filename}")
        except Exception as e:
            print(f"Oops! Couldn't save log: {e}")

class QuestionManager:
    def __init__(self, questions_file='questions.txt'):
        # load questions from the text file
        self.questions = self.load_questions(questions_file)
        self.responses = []

    def load_questions(self, filename):
        try:
            with open(filename, 'r') as f:
                # Read each line, strip whitespace, remove empty lines
                return [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            print(f"Questions file {filename} not found. Using fallback questions.")
            return [
                "What is your current role in cybersecurity?",
                "How many years of experience do you have with security tools?",
                "What types of security monitoring have you implemented before?"
            ]

    def ask_questions(self, logger):
        # select and ask questions
        random.shuffle(self.questions)
        # ask up to 3 questions
        for question in self.questions[:3]:
            print(question)
            # Record character typed in
            response = input("Your response: ")
            for char in response:
                logger.record_key(char)
            # Save
            self.responses.append(f"Q: {question}\nA: {response}\n")

# get user consent
def get_user_consent():
    print("Key Logging Consent")
    print("This program will record your keystrokes.")
    while True:
        consent = input("Are you ok with this? (yes/no): ").lower()
        if consent in ['yes', 'y']:
            return True
        elif consent in ['no', 'n']:
            return False
        else:
            print("Type 'yes' or 'no'.")

# Main
def main():
    # Check if user gives consent, returns True or False from yes/no
    if not get_user_consent():
        print("Logging cancelled.")
        return
    # username
    username = input("Enter your username: ")
    # logger and question manager
    logger = KeyLogger(username)
    question_manager = QuestionManager()
    # questions and log keystrokes
    question_manager.ask_questions(logger)
    # save
    logger.save_log()
    # show the log contents
    try:
        with open(logger.filename, 'r') as log_file:
            print("\n--- Logged Keystrokes ---")
            print(log_file.read())
    except Exception as e:
        print(f"Couldn't read log file: {e}")


if __name__ == "__main__":
    main()
