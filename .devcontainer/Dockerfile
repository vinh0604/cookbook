FROM mcr.microsoft.com/devcontainers/python:0-3.11

# Install CLI utilities
RUN apt-get update && apt-get install -y jq sqlite3 httpie

# Install python dependencies
RUN pip install pre-commit poetry