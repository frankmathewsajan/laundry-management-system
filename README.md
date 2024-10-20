## Requirements

- Python 3.x
- Django
- HTML/CSS for frontend
- SQLite (or another database) for storing data

## Installation Steps

1. **Clone the Repository and Navigate to `laundry` folder**
    
    ```bash
    git clone https://github.com/frankmathewsajan/laundry-management-system.git
    cd laundry
    ```
    
2. **Set Up Virtual Environment**
    
    ```bash
    python -m venv venv
    venv\Scripts\activate # On Linux use `source venv/bin/activate`
    ```
    
3. **Install Dependencies**
    
    ```bash
    pip install -r requirements.txt
    ```
    
4. **Set Up Database**
    
    ```bash
    python manage.py migrate
    ```
    
5. **Run the Application**
    
    ```python
    python manage.py runserver
    ```
    
    Access the application at `http://localhost:8000`
    

## Usage

The website UI/UX is pretty basic, but this is a quick guide for my dear dummies.

### Login

- Navigate to the `http://localhost:8000` page.
- The only user available is probably `vitap_mh3`
- I trust you, so the password is `1593`.

### How it works?

- Enter your college registration number (will be redirected to the user page)
- Followed by the cloth count. Make sure it is b/w 0 to 25.
- The entry will be recorded in the DB. Click the title to go back home.
- there are some limitations tho...

### So Sky is Not the Limit? Nah uh...

- For cloth count it's 0 to 25.
- A student can only give laundry 4 times a month.
- The username should in `^\d{2}[a-zA-Z]{3}\d{4,5}$` format.

Start -> **Two Digits** -> **Space** -> **Three Letters** -> **Space** -> **Four or Five Digits** -> End

1. **Start**
   - Beginning of the string `^`
2. **Two Digits**
   - `\d{2}`
3. **Space**
   - Single space ` `
4. **Three Letters**
   - `[a-zA-Z]{3}`
5. **Space**
   - Single space ` `
6. **Four or Five Digits**
   - `\d{4,5}`
7. **End**
   - End of the string `$`

### Conclusion

- Mess around with the website (it's very small), all the minute details are self-explanatory... 

## Code Structure (just the main files)

- **`manage.py`**: Django's command-line utility for administrative tasks.
- **`LaundryMS/`**: Directory containing Django project settings and configuration.
    - **`settings.py`**: Configuration settings for the Django project.
    - **`urls.py`**: URL declarations for the project.
    - **`wsgi.py`**: WSGI configuration for the project.
- **`laundry/`**: Django app containing the core functionality.
    - **`models.py`**: Contains the data models for the application.
    - **`views.py`**: Contains the view functions that handle requests and responses.
    - **`forms.py`**: Defines forms used in the application.
    - **`templates/`**: Directory containing HTML templates for the frontend.
    - **`static/`**: Directory containing static files like CSS and JavaScript.

## Troubleshooting

- **Issue: Application not running**
    - Ensure that all dependencies are installed.
    - Check if the virtual environment is activated.
    - Verify that the Django development server is running without errors.
- **Issue: Database errors**
    - Ensure that the database is properly set up and migrated.
    - Check the configuration settings for database connection in `settings.py`.
