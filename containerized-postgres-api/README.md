Dockerized PostgreSQL & REST API Stack
Overview

This project demonstrates hands-on experience with Docker, Docker Images, Containers, Docker Compose, PostgreSQL, and REST API development.

The project consists of:

A PostgreSQL database running inside a Docker container
A custom REST API container exposing build-time Docker metadata
Docker image creation and container state persistence
Multi-container orchestration using Docker Compose
Database connectivity between containers

The goal was to build a complete containerized application stack while practicing image management, container networking, data persistence, and service orchestration.

Architecture
┌─────────────────┐
│   PostgreSQL    │
│   Container     │
│     ict-db      │
└────────┬────────┘
         │
         │ Docker Network
         │
┌────────▼────────┐
│    REST API     │
│    ict-api      │
└─────────────────┘
API Endpoints:

Endpoint	  Description
GET /build	Returns Docker build-time metadata
GET /entry	Returns latest student record from PostgreSQL

Technologies Used:

Docker
Docker Compose
PostgreSQL 16 Alpine
REST API
Linux (Ubuntu)
Git & GitHub
