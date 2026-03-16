Bug ID: BUG_LOGIN_001
Title: Login page allows submission with empty username and password

Environment:
Browser: Google Chrome
Application: https://the-internet.herokuapp.com/login
OS: Windows

Steps to Reproduce:
1. Open the login page
2. Leave username field empty
3. Leave password field empty
4. Click the Login button

Expected Result:
The system should prevent login and display validation error for empty fields.

Actual Result:
The system attempts login and shows an invalid credentials message.

Severity:
Medium

Priority:
Medium

Status:
Open