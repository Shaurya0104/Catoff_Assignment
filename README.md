# DOTA2 Player Stats and Match History with zkFetch Integration

This project is a Django-based web application that integrates the DOTA2 game API to fetch and display player statistics, match history, and professional player data. Additionally, it uses zkFetch (via Reclaim Protocol) as a middleware to generate zero-knowledge proofs (ZKP) of player data. The zkFetch middleware is implemented in Node.js.

## Features

- Fetch DOTA2 player statistics and match history using the DOTA2 API.
- Retrieve data for professional players.
- Generate zero-knowledge proofs of player data for privacy and verification.

## Prerequisites

Before starting, ensure you have the following installed:

- Python 3.x
- Django
- Node.js

## Installation and Setup

Follow the steps below to set up and run the project:

1. **Clone the Repository**

    ```bash
    git clone https://github.com/Shaurya0104/Catoff_Assignment.git
    cd Catoff_Assignment
    ```

2. **Install Django and Dependencies**

    Ensure Django is installed in your system. If not, you can install it using:

    ```bash
    pip install django
    ```

3. **Set Up the zkFetch Middleware**

    Navigate to the `zk-fetch-middleware` directory and install the required Node.js modules:

    ```bash
    cd zk-fetch-middleware
    npm install
    ```

    Start the zkFetch middleware server:

    ```bash
    node server.js
    ```

4. **Start the Django Backend**

    In a separate terminal, navigate to the project root directory and start the Django backend:

    ```bash
    python manage.py runserver
    ```

5. **Access the Application**

    Open your browser and go to:

    ```
    http://127.0.0.1:8000/game1/
    ```

## Project Structure

- `zk-fetch-middleware/`: Contains the Node.js middleware for zkFetch integration.
- `game1/`: Django app responsible for interacting with the DOTA2 API and handling requests.
- `manage.py`: Django’s command-line utility for administrative tasks.

## How It Works

### DOTA2 API Integration:
- Fetch player statistics and match history using their player ID.
- Access professional player data.

### Zero-Knowledge Proof with zkFetch:
- The application sends player data to the zkFetch middleware.
- zkFetch generates a zero-knowledge proof for the requested data.
- The proof is returned to the Django backend and displayed in the UI.

### Frontend:
- User-friendly interface to search for players and view their data.

## Example Workflow

1. Enter a player's ID or name in the search bar on the application interface.
2. The backend fetches data from the DOTA2 API and sends it to zkFetch.
3. zkFetch generates a zero-knowledge proof and sends it back.
4. The application displays the player's stats, match history, and proof data.

## API Reference

This project uses the following APIs:

- **DOTA2 API**: For fetching player statistics and match history.
- **zkFetch Middleware**: For generating zero-knowledge proofs.


## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- DOTA2 API Documentation
- zkFetch for providing a reliable ZKP middleware.
- Django and Node.js communities for their excellent frameworks and tools.

Enjoy exploring the world of DOTA2 with enhanced privacy using zkFetch!
