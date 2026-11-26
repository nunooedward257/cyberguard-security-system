# Welcome Message
print("=" * 55)
print("           CYBERGUARD v1.0")
print("   PERSONAL SECURITY MONITORING SYSTEM")
print("=" *55)

print("\nWelcome, Security Analyst!")
print("\nYour mission is to monitor account")
print("information and identify potential threats.")

print("\nStarting security assessment...")

# USER INFORMATION COLLECTION
print("\n--- USER INFORMATION COLLECTION ---")

username = input("Enter Username: ")
email = input("Enter Email Address: ")
password = input("Enter password: ")
age = int(input("Enter age: "))
ip_address = input("Enter IP address: ")
failed_attempts =int(input("Enter failed login attempts: "))

status = input("Is the account Active or Inactive? ").lower()

if status == "active":
    account_status = True
elif status == "inactive":
    account_status = False
else:
    account_status = False
    print("Invalid account status entered!")

print("\nUser information collected successfully!")

print("\n--- ACCOUNT DETAILS ---")
# Display Account Details
print("Username: ", username)
print("Email: ", email)
print("Age: ", age)
print("IP Address: ", ip_address)
print("Failed Login Attempts: ", failed_attempts)
print("Account Status: ", account_status)


print("\n--- SECURITY THREAT DETECTION ---")
# Check account status
if account_status == False:
    print("Account access is currently disabled.")

if failed_attempts == 0:
    print("No failed login attempts detected.")

# Check failed login attempts
elif failed_attempts >= 1 and failed_attempts <= 4:
    print("Low security alert.")
elif failed_attempts >= 5:
    print("CRITICAL WARNING: Possible brute force attack.")

# Check active account security
if account_status == True and failed_attempts < 5:
    print("No critical login threat detected.")


print("\n--- PASSWORD STRENGTH CHECKER ---")
# Check password length
password_length = len(password)

if password_length < 8:
    print("Weak Password.")

elif password_length >= 8 and password_length <= 11:
    print("Moderate Password.")

else:
    print("Strong Password.")


# Report Code
print("\n" + "=" * 45)
print("       CYBERGUARD SECURITY REPORT")
print("=" * 45)

# Determine Password Strength
if password_length < 8:
    password_strength = "WEAK"

elif password_length <= 11:
    password_strength = "MODERATE"

else:
    password_strength = "STRONG"

# Determine Threat Level
if failed_attempts >= 5:
    threat_level = "HIGH"
elif failed_attempts >= 1:
    threat_level = "MODERATE"
else:
    threat_level = "LOW"

# User Information
print("\nUSER INFORMATION")
print("-" * 45)
print("Username  :", username)
print("Email     :", email)
print("Age       :", age)
print("IP Address:", ip_address)
print("Account Status:", status.upper())

# Security Analysis
print("\nSECURITY ANALYSIS")
print("-" * 45)
print("Password Assessment:", password_strength)
print("Failed Login Attempts:", failed_attempts)

# Threat Detection
print("\nTHREAT DETECTION")
print("-" * 45)

if failed_attempts >= 5:
    print("[CRITICAL] Multiple failed attempts!")
    print("[WARNING] Possible brute-force attack detected.")

elif failed_attempts >=1:
    print("[WARNING] Low Security Alert.")

else:
    print("No failed login attempts detected\n"
    "and no critical threat.")

if account_status == False:
    print("[WARNING] Account access is currently disabled.")

# Final Security Status
print("\nFINAL SECURITY STATUS")
print("-" * 45)
print("THREAT LEVEL:", threat_level)

# Recommendation
print("\nRECOMMENDATION:")

if failed_attempts >= 5:
    print("Investigate the login activity and\n" \
    "secure the account immediately.")

elif failed_attempts >= 1:
    print("Review the login activity and monitor\n" \
    "the account for suspicious behaviour.")

else:
    print("Continue monitoring the account regularly.")

print("\n" + "=" * 45)
print("       END OF SECURITY REPORT")
print("=" * 45)

