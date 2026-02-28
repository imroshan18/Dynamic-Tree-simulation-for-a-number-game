

### Interactive Dynamic Decision Tree Number Game

TreeLogic Arena is an interactive web-based number guessing game powered by a dynamic decision tree algorithm. The system adapts in real time based on user responses, demonstrating practical implementation of tree data structures in an applied game environment.

This project highlights algorithm design, backend logic implementation, and frontend interaction in a cohesive full-stack application.

---

## Author

**imroshan18**

---

## Project Overview

TreeLogic Arena is built around a dynamic decision tree that evolves based on user interactions. Instead of using static conditional logic, the application constructs and navigates a tree structure to determine outcomes.

The game demonstrates:

* Tree traversal logic
* Dynamic node creation
* State management
* Backend-to-frontend integration
* Interactive user feedback

---

## Core Concept

The application works as a structured number-based guessing system.

1. The system asks a series of questions.
2. Each response determines the next branch in the tree.
3. The decision tree narrows down possibilities.
4. The final leaf node represents the predicted number.

If the system fails to guess correctly, it can extend the tree structure dynamically to improve future predictions.

This mimics how adaptive decision systems operate.

---

## System Architecture

### 1. Backend Layer (Python)

The backend:

* Manages decision tree logic
* Handles node traversal
* Processes user responses
* Updates tree dynamically
* Controls game state

Core file:

```
decision_tree.py
```

---

### 2. Web Server Layer

The main application file:

```
main.py
```

Responsibilities:

* Serves HTML templates
* Routes requests
* Handles user input
* Returns updated game states

---

### 3. Frontend Layer

The frontend consists of:

* HTML templates (templates/)
* Static assets (static/)
* JavaScript for interaction
* CSS styling

It provides:

* Real-time question updates
* Dynamic response handling
* Interactive UI feedback

---

## Technology Stack

| Layer          | Technology                    |
| -------------- | ----------------------------- |
| Backend        | Python                        |
| Web Framework  | Lightweight Python Web Server |
| Frontend       | HTML, CSS, JavaScript         |
| Data Structure | Decision Tree                 |

---

## Installation Guide

### 1. Install Dependencies

```bash id="tr8wql"
pip install -r requirements.txt
```

---

### 2. Run the Application

```bash id="m2prlx"
python main.py
```

---

### 3. Access in Browser

Open:

```id="k91pxb"
http://127.0.0.1:5000
```

(Port may vary depending on configuration.)

---

## Project Structure

```id="y29qwe"
TreeLogic-Arena/
│
├── main.py               # Web server entry point
├── decision_tree.py      # Core tree logic
├── templates/            # HTML files
├── static/               # CSS & JavaScript
├── requirements.txt
└── README.md
```

---

## Algorithmic Design

The decision tree consists of:

* Internal Nodes → Questions
* Branches → User responses
* Leaf Nodes → Final guesses

Key operations:

* Tree traversal
* Conditional branching
* Dynamic node insertion
* State preservation

Time complexity for traversal:

* O(h), where h is tree height

---

## Design Goals

* Demonstrate tree data structure in real application
* Provide interactive UI experience
* Maintain clean separation between logic and presentation
* Showcase backend + frontend integration
* Build algorithm-driven web system

---

## Potential Enhancements

* Persistent tree storage (database or JSON)
* AI-based learning for smarter branching
* Multiplayer mode
* Leaderboard system
* Deployment to cloud platform
* Enhanced animations

---

## Professional Positioning

This project demonstrates:

* Data structure implementation
* Tree traversal logic
* Full-stack development
* Backend architecture design
* Interactive state management
* Algorithm-based system design

