# Spam Detection Web App

A Machine Learning-based web application that detects whether a message is **Spam 🚨** or **Not Spam ✅** in real-time.



## Overview

This project combines **Machine Learning** and **Web Development** to build an interactive spam detection system.
Users can enter a message and instantly get predictions through a clean and dynamic web interface.



## Features

*  Detects Spam / Not Spam using ML
*  Interactive Popup UI
*  Report Spam Feature
*  Clean and Responsive Design
*  Real-time Prediction with Flask



## How It Works

1. User enters a message
2. Text is converted into numerical data using CountVectorizer
3. Model (**Multinomial Naive Bayes**) analyzes patterns
4. Result is displayed as Spam or Not Spam


## Tech Stack

* Backend: Python, Flask
* Machine Learning: Scikit-learn
* Frontend: HTML, CSS, JavaScript


## Project Structure

spam_project/
│
├── app.py
├── model.py
├── templates/
│     └── index.html
├── static/
│     └── style.css




## How to Run

1. Clone the repository:

git clone https://github.com/yourusername/spam-detection-app.git


2. Navigate to project folder:

cd spam-detection-app

3. Install dependencies:

pip install flask pandas scikit-learn


4. Run the app:

python app.py


5. Open in browser:


http://127.0.0.1:5000/




## What I Learned

* Text preprocessing using CountVectorizer
* Implementing Multinomial Naive Bayes
* Integrating ML models with Flask
* Building interactive UI with JavaScript



## Future Improvements

*  Use real-world large dataset
*  Store reported messages in database
*  Deploy application online
*  Enhance UI/UX design



## Acknowledgment

This project was built as part of my learning journey in "AI & Web Development".

