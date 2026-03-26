#!/bin/bash

# This script starts the development server for the Processing & Preservation web project.

# Navigate to the project directory
cd "$(dirname "$0")/.."

# Install dependencies
npm install

# Start the development server
npm start

echo "Development server is running. Visit http://localhost:3000 to view the project."