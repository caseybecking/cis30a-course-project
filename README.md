# CIS-30A Course Project
## Description

Keylogging is, as the name suggests, the action of recording the keys entered on the keyboard on a computer. Keyloggers can be used for both legitimate and malicious purposes. Write a keylogger program that records the user input. You can use the Pynput library to control and monitor input devices such as mouse and keyboard. Additionally, you can use Listener API and Pythoncan to read data buffer and create log files of data that has been input by the users.

- The program should entice the user to enter information.
- The program should record keyboard input and save input information to a text file.
- The program should output a text file that contains input information from the user.
- The program should contain the following components:
	- Include comments throughout the program (10 points)
	- Use variables and list to store and access data. You can use tuple or dictionary in place of a list (20 points)
	- Use string object to display and control text output. (10 points)
	- Define 2 or more functions and use function calls to execute tasks in the program. (20 points)
	- Implement loop (for or while or both) (10 points)
	- Include conditional statement (if or if-else or if-elif-else) (10 points)
	- Use a non-built-in module, custom module. (20 points)
	- Contains at least 2 classes and 1 sub-class (20 points)
	- Includes 1 or more objects and 1 or more methods in each class. (20 points)
	- Implement error detection using Python built-in exceptions. (10 points)
	- Implement file operations and file output. (20 points)
	- Integrate UI (optional): Bonus 30 points


## Goals
The goal of this program is to create a user-interactive application that captures user inputs in a secure and user-consented manner. It will log these inputs for analysis, returning the results in a structured format.
  

## Functionality
1. **Key Logging with Consent**  
   - The program will collect key presses from the user **only when explicit consent is given**.
   - Key presses will be logged to a uniquely named file following the format:  
     `keys_logged_<username>_<timestamp>.txt`.
   - Logging will stop once the user completes the interaction.
2. **Interactive Question System**  
   - Users will be prompted with a set of questions designed to gather specific information.
   - The first question will always prompt the user for their name.  
   - Subsequent questions will be selected **randomly** from a predefined list stored in a file named `questions.txt`.  
   - This ensures a dynamic experience while maintaining structure.
3. **Output and Data Retrieval**  
   - Once the user completes their session, the program will compile the logged data and return the full contents of the log file for review or further use.
   - This output will be user-friendly and timestamped for traceability.
  

## Target Audience
As a cybersecurity professional, I developed this tool to help teams understand keylogging risks. It's meant to show how monitoring can work—and why it's crucial to get clear consent from users. Think of it like a live demonstration that teaches security teams about potential system vulnerabilities and ethical boundaries. By walking through real-world scenarios, we can better understand how information tracking works and why user privacy matters.

  

## Strengths/Weaknesses
### Strengths
Gets clear user permission before logging
Shows exactly what data is being collected
Helps security teams understand monitoring risks
Lets users see what's happening in real-time
### Weaknesses
Keylogging can still feel invasive
Could accidentally grab sensitive info
Might be misused by someone with bad intentions
  

## Future Improvements
- Add encryption to log files for additional security.
- Implement a user authentication mechanism for accessing logs.
- Provide an optional real-time visualization of user responses during the session.
- Introduce a configuration file to adjust program behavior (e.g., enabling/disabling logging or modifying the question structure).
  

## Installation

  

## Usage



