# Tweet\_Model

A Django-based project for managing tweets, users, and media content.

## Features

- User authentication (login, logout, registration)
- Tweet creation, deletion, and editing
- Media uploads for tweets
- API integration using Django REST Framework (if applicable)

## Installation

1. **Clone the repository**

   ```sh
   git clone https://github.com/paras-bista/Tweet_Model.git
   cd Tweet_Model
   ```

2. **Create a virtual environment** (Recommended)

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**

   ```sh
   pip install -r requirements.txt
   ```

4. **Apply database migrations**

   ```sh
   python manage.py migrate
   ```

5. **Create a superuser (optional)**

   ```sh
   python manage.py createsuperuser
   ```

6. **Run the development server**

   ```sh
   python manage.py runserver
   ```

   Open your browser and visit: `http://127.0.0.1:8000/`

## Project Structure

```
Tweet_Model/
│── chaiheadq/        # Main Django app
│   ├── media/        # User-uploaded files
│   ├── static/       # Static files (CSS, JS, Images)
│   ├── templates/    # HTML Templates
│   ├── views.py      # Main application logic
│   ├── models.py     # Database models
│── db.sqlite3        # SQLite database (if used)
│── manage.py         # Django management script
│── requirements.txt  # Dependencies
└── README.md         # Project documentation
```

## API Endpoints (If using Django REST Framework)

- `GET /api/tweets/` - Fetch all tweets
- `POST /api/tweets/` - Create a new tweet
- `PUT /api/tweets/{id}/` - Update a tweet
- `DELETE /api/tweets/{id}/` - Delete a tweet

## Contributing

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`
3. Make changes and commit: `git commit -m 'Add new feature'`
4. Push changes: `git push origin feature-branch`
5. Open a Pull Request

## License

This project is licensed under the MIT License.


