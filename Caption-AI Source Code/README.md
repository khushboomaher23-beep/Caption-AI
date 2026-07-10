# Caption-AI Source Code

## Overview

This folder contains the complete source code for CaptionAI – AI Powered Social Media Caption Generator, a web application developed as part of an internship project.

The application is designed to help users generate creative and platform-specific social media captions with the support of Generative AI. Users can enter a topic, choose a social media platform, select a preferred tone, and receive AI-generated captions along with relevant hashtags and call-to-action suggestions.

## Source Code Structure

The source code is organized into separate folders and files to keep the project modular, easy to understand, and simple to maintain.

### Main Files

*app.py* – Handles the backend logic, processes user requests, communicates with the AI model, and returns the generated results.
*requirements.txt* – Lists the Python packages required to run the application.
*.gitignore* – Excludes unnecessary and sensitive files from version control.
*README.md* – Provides an overview of the project source code.

### Project Folders

*templates/* – Contains the HTML template used to build the application's user interface.
*static/* – Stores the frontend resources, including CSS for styling and JavaScript for interactive functionality.

## Technologies Used

### Frontend

* HTML
* CSS
* JavaScript

### Backend

* Python
* Flask

### AI Integration

* Groq API
* LLaMA 3.3-70B Versatile Model

## Application Workflow

1. The user enters a topic or content idea.
2. A social media platform and preferred tone are selected.
3. The frontend sends the request to the Flask backend.
4. The backend communicates with the AI model through the Groq API.
5. The generated captions, hashtags, and call-to-action suggestions are returned and displayed on the application interface.

## Key Features

* AI-generated social media captions
* Platform-specific content generation
* Multiple caption suggestions
* Hashtag generation
* Call-to-action (CTA) suggestions
* Responsive and user-friendly interface

## Developer

Khushboo Meena

