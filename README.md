### 🎮 Interactive Rock Paper Scissors (RPS) Web Engine

A full-stack, server-side web application built with Python and the Flask framework that handles responsive user sessions, algorithmic win-state evaluations, and smooth HTTP request/response routing. 

### 🚀 Live Deployment & Links

* **Live Application:** [Play Live Game on Render](https://rps-flask-game.onrender.com) *(Note: Hosted on a free instance; please allow 45–60 seconds for the web container to wake up on the first click)*
* **Central Portfolio Hub:** [Sudipta Debroy Portfolio](https://sdr2277.github.io)

### 🛠️ Architecture & Technical Features

* **State Preservation Architecture:** Leverages Flask client-side session cookies to track ongoing player win-loss streaks securely without local memory leakage.
* **Matrix Evaluation Engine:** Implements structural lookup validation matrices to execute instant score computations on the backend server.
* **RESTful Routing Framework:** Employs precise GET and POST request parameters to transition the UI seamlessly without requiring heavy frontend JavaScript engines.
* **Unified Conditional Rendering:** Utilizes a single structural interface layout (index.html) driven by Jinja2 logic expressions to dynamically switch between the entry portal, active round processing, and win/loss result states without hard page refreshes

### 📁 Repository Directory Breakdown


├── app.py                 # Core Flask backend server and web route managers
├── logic.py               # Game mechanics engine handling win/loss scoring matrices
├── requirements.txt       # Production python engine dependency versions
├── render.yml             # Blueprint configuration file for Infrastructure-as-Code automation
├── templates/             # View layer containing Jinja2 template components
│   └── index.html         # Injected unified layout handling all game states and loops
└── README.md              # Technical engineering documentation


### 🧰 Technology Stack

* **Backend Processing:** Python 3.10+ / Flask Framework
* **Interface Rendering:** HTML5 / Jinja2 Template Injections
* **Visual Layer:** Custom CSS3 Media Queries
* **Cloud Infrastructure:** Render Web Services Engine
