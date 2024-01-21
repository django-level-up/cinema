# Cinema Project

Cinema is a movie viewing project that aggregates films from various sources such as Kinopoisk, IMDb, TMD, and allows downloading. The application automatically synchronizes and updates data from sources and checks link availability 24/7.

## Installation

1. Clone the repository:

    ```bash
    git clone <URL_of_the_repository>
    ```

2. Run Docker Compose:

    ```bash
    docker-compose -f infrastructure/dev/docker-compose.yml up
    ```

    Then:

    ```bash
    docker-compose -f infrastructure/dev/docker-compose.yml up
    ```

3. Stop the server and load initial data:

    ```bash
    docker-compose -f infrastructure/dev/docker-compose.yml run --rm cinema_app_dev sh -c "python3 manage.py import_movies && python3 manage.py import_shows"
    ```

    Then start again:

    ```bash
    docker-compose -f infrastructure/dev/docker-compose.yml up
    ```

4. Go to [localhost:8000/admin/](http://localhost:8000/admin/) and log in with the following credentials:
   - Email: super@gmail.com
   - Password: super

5. Browse movies and test the API using Swagger.

## ER Diagram

![ER Diagram](image.png)

## Note

- To download movies from other sources, ensure the presence of necessary API keys and configurations in the `.env` file.
- Additional information about available APIs and configurations can be found in the documentation.

For any installation issues or questions, refer to the documentation or contact the [developers](mailto:developer@example.com).
