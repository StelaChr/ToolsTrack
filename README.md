# ToolsTrack

ToolsTrack is a Django-based web application for managing, tracking, and maintaining tools. It allows users to categorize tools, track their usage and borrowing status, and log maintenance activities. The system is designed for individuals or organizations that need to keep an organized inventory of tools and their history.

## Features

- **User Authentication**: Register and log in with email-based accounts.
- **Tool Management**: Add, edit, view, and delete tools with details like name, brand, inventory number, room, section, and photo.
- **Borrowing System**: Track which tools are borrowed, by whom, and when they are returned.
- **Maintenance Tracking**: Log maintenance activities for each tool, including type, date, cost, and notes.
- **Categorization**: Organize tools into categories with descriptions.
- **Dashboard & Search**: View and search your tools and categories from a personalized dashboard.

## Installation

### Prerequisites
- Python 3.8+
- PostgreSQL database
- [pip](https://pip.pypa.io/en/stable/)

### Note about the `.env` file
For evaluation purposes, the `.env` file with the required environment variables will be provided separately.

### Clone the Repository
```bash
git clone <your-repo-url>
cd ToolsTrack
```

### Create a Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Configure Environment Variables
Create a `.env` file in the project root with the following:
```
SECRET_KEY=your_secret_key
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
```

### Apply Migrations
```bash
python manage.py migrate
```

### Create a Superuser (Admin)
```bash
python manage.py createsuperuser
```

### Run the Development Server
```bash
python manage.py runserver
```

## Usage

- Visit `http://127.0.0.1:8000/` to access the home page.
- Register a new account or log in.
- Use the dashboard to view, search, and manage your tools.
- Add new tools via `/tools/create/`.
- Edit, view details, or delete tools via `/tools/<tool_id>/edit/`, `/tools/<tool_id>/details/`, `/tools/<tool_id>/delete/`.
- Log maintenance for a tool via `/maintenance/<tool_id>/create/` and view records at `/maintenance/<tool_id>/records/`.
- Organize tools into categories and view them at `/category/<category_id>/`.
- Admin interface available at `/admin/` for advanced management.

## Project Structure

- `tools/` - Tool models, views, and management
- `maintenance/` - Maintenance records and views
- `category/` - Tool categories
- `accounts/` - Custom user model and authentication
- `common/` - Shared views (dashboard, home)
- `templates/` - HTML templates
- `static/` - Static files (CSS, JS, images)
- `media/` - Uploaded files/photos

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.
