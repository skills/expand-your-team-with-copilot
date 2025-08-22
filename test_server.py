#!/usr/bin/env python3
"""
Simple test server without MongoDB dependency to understand the routing issue
"""
from fastapi import FastAPI, APIRouter, HTTPException, Query
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from typing import Dict, Any, Optional, List
import os
from pathlib import Path

# Mock data
activities_data = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Mondays and Fridays, 3:15 PM - 4:45 PM",
        "schedule_details": {
            "days": ["Monday", "Friday"],
            "start_time": "15:15",
            "end_time": "16:45"
        },
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 7:00 AM - 8:00 AM",
        "schedule_details": {
            "days": ["Tuesday", "Thursday"],
            "start_time": "07:00",
            "end_time": "08:00"
        },
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    }
}

# Initialize FastAPI app
app = FastAPI(
    title="Mergington High School API",
    description="API for viewing and signing up for extracurricular activities"
)

# Create router for activities
activities_router = APIRouter(
    prefix="/activities",
    tags=["activities"]
)

@activities_router.get("/", response_model=Dict[str, Any])
def get_activities(
    day: Optional[str] = None,
    start_time: Optional[str] = None,
    end_time: Optional[str] = None
) -> Dict[str, Any]:
    """
    Get all activities with their details, with optional filtering by day and time
    """
    print(f"Received request for activities with params: day={day}, start_time={start_time}, end_time={end_time}")
    
    # For simplicity, just return all activities for now
    result = {}
    for name, details in activities_data.items():
        result[name] = {
            **details,
            "current_participants": len(details["participants"])
        }
    
    print(f"Returning {len(result)} activities")
    return result

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(current_dir, "src", "static")), name="static")

# Root endpoint to redirect to static index.html
@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")

# Include the activities router
app.include_router(activities_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)