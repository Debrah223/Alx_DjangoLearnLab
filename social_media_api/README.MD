This is a Django REST Framework-based API for user authentication, including registration, login, and profile management.

Features: 
    User Registration
    Token-based Authentication
    User Login
    Profile Management

Technologies Used:
    Python 3
    Django
    Django REST Framework (DRF)
    Django REST Framework Authtoken

API Endpoints
1. User Registration
Endpoint: POST /api/accounts/register/
2. User Login
Endpoint: POST /api/accounts/login/
3. User Profile
Get Profile: GET /api/accounts/profile/
Update Profile: PUT /api/accounts/profile/

 The project uses a custom CustomUser model extending Django’s AbstractUser,