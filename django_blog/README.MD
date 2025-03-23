The authentication system in this project allows users to:

Register a new account.
Log in to access protected areas.
Log out securely.
Manage their profile, including updating account details.

 How Authentication Works

Step 1: User Registration
A new user signs up by providing a username, email, and password.
The system uses Django’s UserCreationForm to handle validation.
Once the user registers, they are automatically logged in and redirected to their profile page.

Step 2: User Login
A registered user provides their username and password on the login page.
Django’s built-in authentication system checks the credentials.
If valid, Django creates a session and logs the user in.

Step 3: User Logout
A logged-in user clicks Logout.
Django clears the session and logs the user out.

Step 4: Profile Management
Authenticated users can view and edit their profile (e.g., change email).
Passwords are securely stored using Django’s hashing mechanism.

 User Interaction

1. Register
Visit /register/
Fill in username, email, password.
Click Submit → Redirects to /profile/.

2. Login
Visit /login/
Enter username and password.
Click Login → Redirects to /profile/.

3. Logout
Click Logout → Redirects to /login/.

4. Profile
Visit /profile/
View profile details.
Update details and save.

Security Measures

Passwords are securely hashed using Django’s PBKDF2 hashing algorithm.
CSRF protection is enabled in all forms using {% csrf_token %}.
Login is required for accessing the profile page using @login_required