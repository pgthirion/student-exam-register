# Student Exam Register

A Python utility designed for exam administrators to quickly generate an attendance registration form.

## Features

* **Interactive Input:** Prompts the user for the number of students and their specific ID numbers.
* **Automated Formatting:** Generates a clean, structured text file ready for printing.
* **Signature Lines:** Automatically adds a signature space for each student entry.

## Prerequisites

* Python 3.x

## Installation

1.  **Download the Script:**
    * Click the green **<> Code** button at the top of this page.
    * Select **Download ZIP**.
    * Extract the ZIP file to a folder on your computer.

2.  **Open Terminal:**
    * Navigate to the extracted folder.

        cd path/to/student-exam-register

## Usage

Run the script using Python:

    python student_register.py

**Process:**
1.  Enter the total number of students writing the exam.
2.  Enter the ID number for each student when prompted.

**Output:**
The script creates a file named `reg_form.txt` in the same directory:

    ID List:

    Student 1:  22 sign here: _____________________
    Student 2:  1 sign here: _____________________
