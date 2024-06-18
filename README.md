# FinTrack

Welcome to FinTrack! This project is designed to help you manage your personal finances effectively. Below, you'll find detailed information on setting up the project, its purpose, features, and how to contribute.

## Introduction

FinTrack is a personal finance management application aimed at providing users with tools to track expenses, manage budgets, and analyze spending habits. Whether you're a budget-conscious individual or someone looking to gain better control over their finances, FinTrack aims to simplify the process with its intuitive interface and powerful features.

## Screenshots

![Screenshot 1](https://github.com/leaish613/FinTrack/assets/screenshot1.png)
![Screenshot 2](https://github.com/leaish613/FinTrack/assets/screenshot2.png)
![Screenshot 3](https://github.com/leaish613/FinTrack/assets/screenshot3.png)

## Project Purpose and Functionality

FinTrack integrates various technologies to deliver a comprehensive personal finance management solution:

- **Backend**: Built with Python and Flask, FinTrack manages user data and financial transactions securely.
- **Database**: SQLite is used to store and retrieve financial data efficiently.
- **Frontend**: Developed with React, the frontend provides an interactive dashboard for users to visualize their financial information.

Here’s how it works:
- The backend server uses SQLite as its database to store financial data.
- The React frontend communicates with the backend API to fetch and display financial information.
- Users can track expenses, set budgets, and analyze spending habits through intuitive interfaces.

## Features

- Track expenses and income with detailed categorization.
- Set budget goals and receive notifications for exceeding limits.
- Generate reports and graphs to analyze spending trends over time.
- Secure user authentication and data privacy controls.

## Getting Started

### Prerequisites

Before starting, ensure you have the following installed:

- Node.js
- Python 3.x
- SQLite
- npm (Node Package Manager)
- pip (Python Package Installer)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/leaish613/FinTrack.git
   cd FinTrack

2. Install dependencies for the frontend (React):

    ```bash 
    cd frontend 
    npm install
    
3. Install dependencies for the backend (Python):

    ```bash 
    cd ../backend 
    pip install -r requirements.txt

## Usage
To run FinTrack, follow these steps:

### Start the Backend Server (Flask)

1. Navigate to the backend directory:

    ```bash
    cd backend

2. Run the Flask server:

    ```bash     
    python app.py

The backend server should now be running at http://localhost:5000.

### Start the Frontend (React)
1. Navigate to the frontend directory:

    ```bash 
    cd frontend 

2. Start the React development server:

    ```bash 
    npm start

The React app should now be running and accessible at http://localhost:3000.

## Available Scripts
In the project directory, you can run:

- npm start: Runs the app in development mode for the React frontend. Open http://localhost:3000 to view it in your browser. The page will reload when you make changes, and you may see lint errors in the console.

## Database Integration
FinTrack uses SQLite as the database to store and manage financial data. The Python backend interacts with the SQLite database to provide seamless data management.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for review.
