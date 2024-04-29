# zartek-assignment

### Basic Ride Sharing API with Class-Based Viewsets.
- User registration
- Login
- Create ride request
- List all available rides
- View ride details
- Update ride status
- Test case included for all apis and models

## Getting Started

### Prerequisites
- Python
- Django

### Installation

1. Clone the repository:
   ```bash
   https://github.com/Aswanym/zartek-assignment.git
   
2. Create virtual environment
   ```bash
      virtualenv venv
   
3. activate virtualenv (windows)
   ```bash
      venv/Scripts/activate
   
4. Install dependencies
   ```bash
      pip install -r requirements.txt
      
   
5. Configuration
- Create a .env file in the project root. 
- Add the following environment variables to the .env file:

   ```bash
  SECRET_KEY=your_secret_key
  
- Replace the placeholder values with your actual values.

7. Database Migration
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   

8. Running the Server - Start the development server:
   ```bash
   python manage.py runserver


9. Visit http://localhost:8000/ in your browser to view project.


10. To run test cases 
```bash
    python manage.py test <app_name\test>
