# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to design and implement RESTful APIs using the FastAPI framework. You'll build a complete API with multiple endpoints, request validation, and proper HTTP status codes to understand modern web service development.

## 📝 Tasks

### 🛠️ Create a Basic FastAPI Application

#### Description
Set up a FastAPI application with basic endpoints. Create a simple API that serves as the foundation for the rest of the assignment.

#### Requirements
Completed program should:

- Import and initialize a FastAPI application instance
- Create at least one GET endpoint that returns a welcome message or status information
- Run the application using Uvicorn on localhost:8000
- Include proper HTTP status codes in responses


### 🛠️ Implement CRUD Operations for a Resource

#### Description
Build endpoints to Create, Read, Update, and Delete (CRUD) items from a simple data model. This could be a todo list, product catalog, user database, or similar resource.

#### Requirements
Completed program should:

- Define a data model using Pydantic for request/response validation
- Implement POST endpoint to create new items
- Implement GET endpoint to retrieve all items
- Implement GET endpoint with path parameter to retrieve a specific item by ID
- Implement PUT endpoint to update an existing item
- Implement DELETE endpoint to remove an item
- Return appropriate HTTP status codes (200, 201, 404, etc.)


### 🛠️ Add Request Validation and Error Handling

#### Description
Enhance the API with proper input validation and meaningful error responses. Ensure the API handles edge cases and provides clear feedback when something goes wrong.

#### Requirements
Completed program should:

- Use Pydantic models for automatic request validation
- Return HTTP 400 for invalid request data with error details
- Return HTTP 404 when requested resource is not found
- Implement try-except blocks or FastAPI exception handlers
- Provide clear, meaningful error messages to API clients
- Validate required fields and data types
