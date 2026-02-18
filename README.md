# AI-AdBreak-Engagement-Extension
AI-powered OTT ad-break engagement extension

A Chrome extension that keeps fans engaged during live match ad breaks on OTT platforms and YouTube.
The Problem
A. Live cricket matches have frequent ads.
During ads:
 1. Viewers lose match context
 2. Emotional momentum breaks

B. New viewers don’t know what’s happening
 1. This reduces engagement.

Our Solution
Our extension:
 1. Detects when an ad starts
 2. Fetches a short AI-generated match recap
 3. Shows a minimal overlay during the ad
 4. Automatically hides it when live play resumes
 5. The live stream is never modified.

How It Works
 1. fetches live match data.
 2. AI generates a short contextual summary.
 3. Extension detects ad break.
 4. Extension displays the latest summary.
 5. Overlay disappears when the match resumes.

Tech Stack
A. Extension:
 1. JavaScript
 2. HTML & CSS
 3. Chrome Extension APIs

B. Backend:
 1. Python
 2. Flask
 3. REST API

Data:
 Live Sports Data API

How to Run
Backend
 cd backend
 pip install -r requirements.txt
 python app.py

Extension
 Open chrome://extensions
 Enable Developer Mode
 Click Load Unpacked

Select the extension folder

Impact
 a. Maintains engagement during ads
 b. Helps viewers quickly regain context

Works without interfering with streaming
