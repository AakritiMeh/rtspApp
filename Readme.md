# RTSPApp

RTSPApp is a Flask-based application designed to overlay custom logos and text on top of RTSP stream videos. The project provides a user-friendly interface for managing video overlays, with full control over the livestream, including options for play, pause, and volume adjustment. The backend is powered by Flask and MongoDB, while the frontend uses React and Vite.

# Features

- Stream video from an RTSP URL with real-time overlays.
- Add custom overlays such as logos and text.
- Full video control with play, pause, and volume adjustment.
- API endpoints for managing overlays with CRUD operations.
- Persistent overlay settings stored in MongoDB.

# Tech Stack

- Backend: Flask, Python
- Database: MongoDB
- Frontend: React, Vite
- Video Streaming: RTSP compatible
- Overlay management: Python video processing

# Requirements

Ensure you have the following installed:
<br />

- Python (>=3.7)
- Node.js (>=14.x)
- MongoDB (ensure MongoDB service is running)

# Installation

**1. Clone the repository:**

```bash
git clone https://github.com/AakritiMeh/rtspApp.git
cd rtspApp
```

**2.Backend Setup:**

Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate # Linux/Mac
venv\Scripts\activate # Windows
```

**3.Install required dependencies:**

```bash
pip install -r requirements.txt
```

Ensure MongoDB is running and accessible.

**4.Start the Flask backend server:**

```bash
python app.py
```

The backend will be running on http://localhost:5000.

**5.Frontend Setup:**

Navigate to the frontend folder:

```bash
cd frontend
```

**6.Install the required npm packages:**

```bash
npm install
```

**7.Run the frontend:**

```bash
npm run dev
```

The frontend will be running on http://localhost:3000.

# Usage

**Connect RTSP Stream:**

In the frontend interface, enter the RTSP URL of the stream you'd like to overlay.

- Add Overlay:

Use the controls in the frontend to add custom overlays such as logos or text on top of the livestream. You can upload an image file for logos or enter text directly.

- Control Video:

Use the play, pause, and volume buttons to control the stream.

- Save Overlay Settings:

The overlays and settings can be persisted via the backend API, which uses MongoDB to store and retrieve overlay configurations.

#

# API Documentation

The backend provides a set of API endpoints for managing the overlay settings:

- POST /api/overlays
  <br />
  Description: Add a new overlay configuration.

<br />
  Request Body:

```json
{
"type": "logo" | "text",
"content": "<URL or Text>",
"position": {"x": <int>, "y": <int>},
"size": {"width": <int>, "height": <int>}
}
```

Response: Returns the saved overlay object with its ID.

- GET /api/overlays
  <br />
  Description: Get all saved overlays.
  <br />
  Response:

```json
[
{
"id": "<overlay_id>",
"type": "logo" | "text",
"content": "<URL or Text>",
"position": {"x": <int>, "y": <int>},
"size": {"width": <int>, "height": <int>}
}
]
```

- PUT /api/overlays/:id

  Description: Update an existing overlay configuration by ID.
  <br />
  Request Body: Same as POST /api/overlays.

- DELETE /api/overlays/:id
  <br />
  Description: Delete an overlay by ID.
