# Python Regular Expressions (Regex) Project

## Project Overview

This project demonstrates the use of Python Regular Expressions (`re` module) to extract and identify different types of information from a sample text.

The program searches for five types of data:

1. **Email Addresses** – Identifies valid email address formats.
2. **Phone Numbers** – Extracts phone numbers in formats such as `(555) 123-4567` and `555-123-4567`.
3. **Credit Card Numbers** – Identifies 16-digit card number patterns separated by spaces or hyphens.
4. **Time** – Extracts valid times in both 12-hour and 24-hour formats.
5. **Currency** – Identifies monetary values that begin with a dollar sign.

The project uses Python's built-in `re` module and regular expression patterns to find matching information.

## Requirements

- Python 3.x
- No external libraries required.

## Setup Instructions

### 1. Install Python

Download and install Python 3 from:

https://www.python.org/downloads/

### 2. Clone or Download the Project

Download the project files or clone the repository:

```bash
git clone https://github.com/fimbuki-design/alu_regex-data-extraction-fimbuki-design-.git
```

### 3. Navigate to the Project Folder

```bash
cd 
```

### 4. Run the Program

Execute the Python file:

```bash
python extractor.py
```

## Expected Output

The program displays the extracted information in the terminal:

```text
Emails: [...]
Phone numbers: [...]
Credit cards: [...]
Times: [...]
Currency: [...]
```

The actual results depend on the regular expression patterns and the sample text provided.

## Technologies Used

- **Python 3** – Programming language.
- **re module** – Used for pattern matching and extracting information.

## Project Purpose

The purpose of this project is to understand how regular expressions work and how they can be used to identify specific patterns in text, including emails, phone numbers, credit card formats, times, and currency values.

## Author

Frank Imbuki
