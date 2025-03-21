# Cafe Rating Web Application

A Flask-based web application for tracking and rating cafes based on various criteria.

## Features
- Add new cafe entries with detailed information
- View list of all cafes with their ratings
- Rate cafes based on coffee quality, WiFi strength, and power outlet availability
- Bootstrap 5 styling for responsive design
- Form validation for data consistency

## Prerequisites
- Python 3.x
- Required Python packages (listed in requirements.txt):
  - `Flask`
  - `Flask-Bootstrap5`
  - `Flask-WTF`
  - `WTForms`

## Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/cafe-rating-app.git
cd cafe-rating-app
```

2. Install dependencies:
```bash
# On Windows
python -m pip install -r requirements.txt

# On MacOS/Linux
pip3 install -r requirements.txt
```

## Usage
1. Run the application:
```bash
python app.py
```

2. Access the web application at:
```
http://localhost:5000
```

## Application Routes
- `/`: Home page
- `/add`: Form to add a new cafe
- `/cafes`: List of all cafes

## Form Fields
- Cafe Name (required)
- Location (Google Maps URL, required)
- Opening Time (required)
- Closing Time (required)
- Coffee Rating (1-5 ☕️ symbols, required)
- WiFi Rating (1-5 💪 symbols or ✘, required)
- Power Outlet Rating (1-5 🔌 symbols or ✘, required)

## File Structure
- `app.py`: Main application file
- `cafe-data.csv`: Stores cafe data
- `static/css/styles.css`: Custom CSS styling
- `templates/`: HTML templates
  - `index.html`: Home page
  - `add.html`: Add cafe form
  - `cafes.html`: Cafe list

## How It Works
1. Uses Flask as the web framework
2. Implements WTForms for form handling and validation
3. Stores data in a CSV file
4. Uses Bootstrap 5 for styling
5. Custom CSS loaded from styles.css

## Configuration
- Secret key is set in the code (consider using environment variables for production)
- CSV file (`cafe-data.csv`) is used as the data store
- Debug mode is enabled by default

## Notes
- The `/add` route currently only prints "True" when form validates - needs implementation to write to CSV
- Uses UTF-8 encoding for CSV handling
- Form validation ensures all fields are completed with valid data
- URL field requires a valid URL format

## License
[MIT License](LICENSE)

## Requirements.txt
```
Flask
Flask-Bootstrap5
Flask-WTF
WTForms
```

To complete the project, you'll need to:
1. Create the template files (index.html, add.html, cafes.html)
2. Implement the CSV writing functionality in the /add route
3. Create a basic cafe-data.csv file
```

