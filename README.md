# Library Management System
This project is an application for a library to store book and author data. It provides an HTTP REST API to fulfill the requirements specified below.

## Specifications
### 1. Import Authors from CSV
You can import authors' data from a CSV file into the database. The CSV file should have the following format:

```text
name
Luciano Ramalho
Osvaldo Santana Neto
David Beazley
Chetan Giridhar
Brian K. Jones
J.K Rowling
```

Each author record in the database will have the following fields:

- id (auto-generated)
- name

To import authors, you can use the following command:

```bash
python manage.py import_authors authors.csv
```

### 2. Authors Endpoint

This endpoint returns a paginated list of authors' data. Optionally, you can search authors by name.
- Endpoint: /authors
- Supported Methods: GET
- Query Parameters:
    - page (optional): Page number for pagination (default: 1)
    - limit (optional): Number of authors per page (default: 10)
    - search (optional): Search authors by name

### 3. Book CRUD Operations

This API supports the following CRUD operations for books:

- Create a book
- Read book's data
- Update book's data
- Delete book's data

Each book record has the following fields:

- id (auto-generated)
- name
- edition
- publication_year
- authors (multiple authors can write a book)

To retrieve books, you can filter by the following fields (or a combination of them):

- name
- publication_year
- edition
- author

However, these filters are optional, and you can navigate all the books' data without any filter.

To create a book, send a JSON payload with the following format:

```json
{
  "name": "Book Name",
  "edition": "1st Edition",
  "publication_year": 2023,
  "authors": [1, 2, 3]
}
```

## Technologies Used

- Python
- Django (optional)
- Django REST Framework (optional)
- PostgreSQL (optional)

## Getting Started

- Clone the repository.
- Install the required dependencies.
- Set up the database connection.
- Run the migrations.
- Start the development server.

## API Documentation
For detailed API documentation, please refer to the API Documentation file.

## Contributing
Contributions are welcome! If you have any suggestions, improvements, or bug fixes, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License.