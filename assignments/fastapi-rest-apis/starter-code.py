"""
FastAPI REST API Starter Code
Complete the assignment by implementing the tasks in the README.md file.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

# TODO: Initialize your FastAPI application
app = FastAPI(title="My REST API", version="1.0.0")

# TODO: Define your Pydantic models for data validation
# Example:
# class Item(BaseModel):
#     id: int
#     name: str
#     description: Optional[str] = None
#     price: float


# TODO: Create your in-memory data storage
# Example:
# items_db = []


# TODO: Implement your endpoints
# Task 1: Create a welcome GET endpoint
# @app.get("/")
# def read_root():
#     return {"message": "Welcome to my FASTApi!"}


# Task 2: Implement CRUD operations
# @app.post("/items/")
# def create_item(item: Item):
#     # TODO: Implement create logic
#     pass

# @app.get("/items/")
# def read_items():
#     # TODO: Implement read all logic
#     pass

# @app.get("/items/{item_id}")
# def read_item(item_id: int):
#     # TODO: Implement read by ID logic
#     pass

# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     # TODO: Implement update logic
#     pass

# @app.delete("/items/{item_id}")
# def delete_item(item_id: int):
#     # TODO: Implement delete logic
#     pass


# Task 3: Error handling is already partially set up above
# Make sure to return appropriate HTTP status codes and error messages

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
