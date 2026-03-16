# Login Test Cases

## TC_LOGIN_001
**Test Scenario:** Verify successful login with valid credentials

**Steps:**
1. Open https://the-internet.herokuapp.com/login
2. Enter username: tomsmith
3. Enter password: SuperSecretPassword!
4. Click Login

**Expected Result:**  
User should be redirected to the secure area and see a success message.


---

## TC_LOGIN_002
**Test Scenario:** Verify login with invalid password

**Steps:**
1. Open login page
2. Enter username: tomsmith
3. Enter password: wrongpassword
4. Click Login

**Expected Result:**  
System should display "Your password is invalid!"


---

## TC_LOGIN_003
**Test Scenario:** Verify login with invalid username

**Steps:**
1. Open login page
2. Enter username: wronguser
3. Enter password: SuperSecretPassword!
4. Click Login

**Expected Result:**  
System should display "Your username is invalid!"


---

## TC_LOGIN_004
**Test Scenario:** Verify login with empty fields

**Steps:**
1. Open login page
2. Leave username empty
3. Leave password empty
4. Click Login

**Expected Result:**  
System should display an error message and prevent login.