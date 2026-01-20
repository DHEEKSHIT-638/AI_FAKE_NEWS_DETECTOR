# Fake News Detector

## Description
Fake News Detector is an AI-powered application designed to help students evaluate the credibility of news content in the digital age.  
The system allows users to submit either a full news article as text or upload an image containing news content such as screenshots, posters, or headlines.
Using a generative AI model, the application analyzes the provided content by examining language patterns, tone, contextual cues, and the presence of potential misinformation indicators.  
Based on this analysis, the system produces a credibility assessment that helps classify the content as likely reliable, needing verification, or potentially fake.
In addition to credibility evaluation, the application generates a neutral and unbiased summary of the news content and provides simple explanations aimed at improving media literacy among university students.  

## Features
- Text-based and image-based news analysis
- Fake or Real news prediction
- Simple and interactive user interface
- AI-powered contextual understanding

## Tech Stack
- Python
- Streamlit
- Google Generative AI API

## Setup Instructions
1. Clone the repository
2. Install dependencies using: pip install -r requirements.txt

## API Key Setup
This project requires a Google Generative AI API key.

Steps to get your API key from Google AI Studio:
- Visit https://aistudio.google.com/apikey
- Sign in with your Google account
- Click on Create API Key then click on create key.
- Copy the generated API key

Replace the following line in the code with your copied API key before running:

GOOGLE_API_KEY = "YOUR_API_KEY_HERE"

## How To Run
streamlit run AI_FAKE_NEWS_DETECTOR.py
## Sample News Image
A sample news article image (`news2.jpeg`) is included in the repository to demonstrate image upload and analysis.

