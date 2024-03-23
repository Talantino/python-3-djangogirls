# 👯‍♀️ DjangoGirls - Blog Post Manager Project

This Django-based Blog-News Post Manager is designed to facilitate the addition and viewing of news posts. Each post can contain a title, the main text, and a publication date.

## Features

- **Adding News Posts**: Users can add news posts with a title, text, and a publication date.
- **Viewing All Posts**: All news posts can be viewed on the homepage, allowing users to easily access the content.

## Technologies and Libraries  
![Alt text for Logo1](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![Alt text for Logo1](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
![Alt text for Logo1](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![Alt text for Logo1](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
- **Django Forms**: Utilized for creating forms for task addition and editing.
- **Jinja**: The template engine for rendering the HTML pages with dynamic data.
- **CRUD Operations**: Create, Read, Update, Delete operations are fundamental for managing news posts.

## Getting Started

Follow these instructions to get the project up and running on your local machine.

### Prerequisites

- Python (3.x)
- Django
### Installation

1. Clone this repository to your local machine:
```bash
git clone git@github.com:Talantino/python-3-djangogirls.git
```
2. Navigate to the project directory:
```bash
cd python-3-djangogirls
```
4. Install the required dependencies:
```bash
pip install -r requirements.txt
```

6. Run the migrations to create the database schema:
```bash
python manage.py migrate
```

7. Start the development server:
```bash
python manage.py runserver
```
### Usage

After the server is running, open your web browser and go to `http://127.0.0.1:8000/` to view the homepage displaying all news posts. Use the provided form to add new posts and see them appear on the homepage.

## Contributing

🤗 Contributions to improve the project are welcome. Feel free to fork the repository and submit pull requests.
