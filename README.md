# CyberGuard Security System

## Project Description
CyberGuard is a Python-based personal account security monitoring system designed to collect account information, identify threats, assess password strength, and generate a security analyst report.

## Features
The system includes five main features:
1. **User Information Collection**
   - Collects username, email address, password, age, IP address, failed login attempts, and account status.
  
2. **Security Threat Detection**
   - Detects failed login attempts.
   - Identifies possible brute-force attacks.
   - Checks whether an account is active or inactive.
  
3. **Password Strength Checker**
   - Weak password: Fewer than 8 characters.
   - Moderate password: 8 to 11 characters.
   - Strong password: 12 or more characters.
  
4. **Security Analyst Report**
   - Generates a report containing user information, security analysis, threat detection, and recommendations.

5. **Threat Level Assessment**
   - Classifies account security as LOW, MODERATE, or HIGH.
  
## Technologies Used
- Python 3
- Visual Studio Code

## How to Run
1. Install Python 3.
2. Download or clone this repository.
3. Open the project folder in Visual Studio Code.
4. Open the terminal.
5. Run the following command:
   '''bash
   python cyberguard.py
   '''
6. Enter the requested account information to generate the security report.

## Project Purpose
This project demonstrates basic Python programming concepts, including:
- Variables and data types
- User input
- Conditional statements
- Comparison operators
- Boolean values
- String manipulation
- Password length assessment

## Disclaimer
CyberGuard is an educational project. It does not monitor real accounts or perform actual network security investigations. Its password assessment is based only on password length.

## Author
Edward Amissah Nunoo 
