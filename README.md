# The Gate Backend Server

This docker-compose file facilitates the deployment of a Django application with a PostgreSQL database for The Gate Education

## Prerequisites

- Docker Engine
- Docker Compose

## Usage

1. Clone the repository containing this `docker-compose.yml` file.
2. Ensure Docker Engine is running.
3. From the root of the repository, run the following command:

   ```
   docker-compose up --build
   ```

   This command will build and run the containers defined in this `docker-compose.yml` file.

4. The application will be available at `http://localhost:8000`.

## Services

### app

- **Build**: Builds the application image using the `Dockerfile` located in the current context.
- **Ports**: Maps port 8000 of the container to port 8000 of the host.
- **Volumes**: Mounts the local directories `./app` and `dev-static-data` into the container to allow real-time code changes and persistent storage of static files.
- **Command**: Executes a script that waits for the database to be available, performs database migrations, and runs the Django development server.
- **Environment Variables**:
  - `DB_HOST`: Database service name.
  - `DB_NAME`: Database name.
  - `DB_USER`: Database user.
  - `DB_PASS`: Database user password.
  - `DEBUG`: Django debug setting.

### db

- **Image**: Uses the official PostgreSQL 13 image with Alpine Linux.
- **Volumes**: Mounts a persistent volume to store PostgreSQL database data.
- **Environment Variables**:
  - `POSTGRES_DB`: Database name.
  - `POSTGRES_USER`: Database user.
  - `POSTGRES_PASSWORD`: Database user password.

## Volumes

- **dev-db-data**: Stores persistent data for the PostgreSQL database.
- **dev-static-data**: Mounted in the application for storing static files.

## URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    [Django URL documentation](https://github.com/TheGateEducation/api-backend-server/blob/development/app/app/urls.py)

Examples:
Function views
    1. Add an import:  `from my_app import views`
    2. Add a URL to `urlpatterns`:  `path('', views.home, name='home')`
Class-based views
    1. Add an import:  `from other_app.views import Home`
    2. Add a URL to `urlpatterns`:  `path('', Home.as_view(), name='home')`
Including another URLconf
    1. Import the `include()` function: `from django.urls import include, path`
    2. Add a URL to `urlpatterns`:  `path('blog/', include('blog.urls'))`

## Additional Notes

- This docker-compose.yml file is configured for a development environment. Make sure to adapt it according to the specific needs of your project and environment.
- Database credentials (`DB_PASS`, `POSTGRES_PASSWORD`) are set to default values. Make sure to change them in production environments and not include sensitive values in public repositories.

Enjoy your local development with Docker!
