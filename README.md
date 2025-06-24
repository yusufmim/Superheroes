# Superheroes Flask API

## Description
This is a Flask-based RESTful API for managing superheroes, their powers, and the relationships between them through hero-powers. The API allows users to retrieve, update, and create records for heroes and powers, with full CRUD functionality for `HeroPower` associations. It includes validations, proper error handling, and an email notification feature when a new hero-power is created. This project was developed as part of the Phase 4 Code Challenge for the Superheroes assignment.

**Owner**: [Your Name]

## Features
- **Models and Relationships**:
  - `Hero`: Represents a superhero with `id`, `name`, and `super_name`.
  - `Power`: Represents a superpower with `id`, `name`, and `description`.
  - `HeroPower`: Associates heroes with powers, including a `strength` attribute ('Strong', 'Weak', 'Average').
  - Many-to-many relationship between `Hero` and `Power` through `HeroPower`, with cascade deletes.
- **Validations**:
  - `HeroPower.strength`: Must be 'Strong', 'Weak', or 'Average'.
  - `Power.description`: Must be present and at least 20 characters long.
- **Routes**:
  - `GET /heroes`: List all heroes.
  - `GET /heroes/:id`: Retrieve a hero with their associated powers.
  - `GET /powers`: List all powers.
  - `GET /powers/:id`: Retrieve a specific power.
  - `PATCH /powers/:id`: Update a power’s description.
  - `POST /hero_powers`: Create a new hero-power association with email notification.
- **Email Notification**: Sends an email when a new `HeroPower` is created (using Flask-Mail).
- **Error Handling**: Returns appropriate HTTP status codes (200, 201, 400, 404) with JSON error messages.
- **Serialization**: Uses `sqlalchemy_serializer` to control JSON output and prevent recursive loops.

## Setup Instructions
1. **Clone the Repository**:
   ```bash
   git clone <your-private-repo-url>
   cd superheroes-api