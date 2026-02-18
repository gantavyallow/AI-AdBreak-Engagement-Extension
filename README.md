# AI-AdBreak-Engagement-Extension
AI-powered OTT ad-break engagement extension

A Chrome extension that keeps fans engaged during live match ad breaks on OTT platforms and YouTube.
The Problem

Live cricket matches have frequent ads.
During ads:

Viewers lose match context

Emotional momentum breaks

New viewers don’t know what’s happening

This reduces engagement.

Our Solution

Our extension:

Detects when an ad starts

Fetches a short AI-generated match recap

Shows a minimal overlay during the ad

Automatically hides it when live play resumes

The live stream is never modified.

How It Works

Backend fetches live match data.

AI generates a short contextual summary.

Extension detects ad break.

Extension displays the latest summary.

Overlay disappears when the match resumes.

Tech Stack

Extension:

JavaScript

HTML & CSS

Chrome Extension APIs

Backend:

Python

Flask

REST API

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

Maintains engagement during ads

Helps viewers quickly regain context

Works without interfering with streaming
