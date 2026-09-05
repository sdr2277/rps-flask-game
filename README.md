### 🎮 Interactive Rock Paper Scissors (RPS) Web Engine

A full-stack, server-side web application built with Python and the Flask framework that handles responsive user sessions, algorithmic win-state evaluations, and smooth HTTP request/response routing. 

### 🚀 Live Deployment & Links

* **Live Application:** [Play Live Game on Render](https://rps-flask-game.onrender.com) *(Note: Hosted on a free instance; please allow 45–60 seconds for the web container to wake up on the first click)*
* **Central Portfolio Hub:** [Sudipta Debroy Portfolio](https://sdr2277.github.io)

### 🛠️ Architecture & Technical Features

* **State Preservation Architecture:** Leverages Flask client-side session cookies to track ongoing player win-loss streaks securely without local memory leakage.
* **Matrix Evaluation Engine:** Implements structural lookup validation matrices to execute instant score computations on the backend server.
* **RESTful Routing Framework:** Employs precise GET and POST request parameters to transition the UI seamlessly without requiring heavy frontend JavaScript engines.
* **Template Generation:** Engineered with Jinja2 parsing expressions to conditionally inject dynamic response layouts and styling blocks down to the viewport.

### 📁 Repository Directory Breakdown

text

├── app.py                 # Core Flask backend router & application gateway
├── requirements.txt       # Python deployment dependencies
├── static/
│   └── style.css          # Core layouts, game typography, and visual styling
└── templates/
    ├── base.html          # Standard HTML skeleton and global layouts
    ├── game.html          # Core gameplay component workspace
    └── index.html         # Start screen landing menu interface

Use code with caution.

### 🧰 Technology Stack

* **Backend Processing:** Python 3.10+ / Flask Framework
* **Interface Rendering:** HTML5 / Jinja2 Template Injections
* **Visual Layer:** Custom CSS3 Media Queries
* **Cloud Infrastructure:** Render Web Services Engine
