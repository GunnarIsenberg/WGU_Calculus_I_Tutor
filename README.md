Calculus I Tutor for WGU

A custom-tailored Calculus I chatbot designed specifically for Western Governors University (WGU) students.

Project Overview

This project is a web application deployed on Google Cloud that provides Western Governors University students with a custom-tailored Calculus I chatbot.

The application delivers contextual explanations, guided problem-solving, and concept-level feedback aligned to the WGU Calculus I curriculum, with a focus on topics students historically struggle with:

Limits

Derivatives

Applications of derivatives

Foundational intuition

The system is designed to be:

Simple to use

Secure by default

Low-friction to operate

Easy to extend as curriculum depth grows

Core System Responsibilities

At a high level, the application is responsible for:

Authenticating users using their existing institutional email accounts

Serving a clean, modern web interface for interactive learning

Providing intelligent, context-aware Calculus I assistance

Persisting user-specific learning context and history

Enforcing per-user data isolation and validation

Major Components and Their Purpose
Web Interface (Presentation Layer)

Purpose
Provide students with a clean, approachable, distraction-free interface for interacting with the Calculus I chatbot.

Responsibilities

Render the chatbot interface in the browser

Accept user input (questions, partial work, conceptual confusion)

Display structured, readable responses

Maintain conversational continuity during a session

This layer is intentionally lightweight. It exists solely to support learning interactions, not to perform business logic.

Application Server (Orchestration Layer)

Purpose
Act as the central coordinator between the user interface, authentication system, AI model, and data storage.

Responsibilities

Serve web pages and API endpoints

Enforce authentication and session validation

Normalize and route user requests

Apply user-specific context (progress, prior questions)

Return structured responses to the frontend

This layer defines the application’s behavior and rules while remaining stateless between requests.

Authentication & Identity Management

Purpose
Ensure only authorized students can access the system while minimizing friction and password management.

Responsibilities

Authenticate users via institutional Microsoft accounts (Outlook)

Validate identity and session state

Derive a stable, unique user identifier

Gate access to all protected application features

Authentication is handled through Microsoft Entra ID, allowing students to sign in using credentials they already trust.

AI Reasoning Engine (Learning Core)

Purpose
Provide intelligent, curriculum-aware Calculus I assistance tailored to each student.

Responsibilities

Interpret student questions and misconceptions

Generate step-by-step explanations and conceptual clarifications

Adjust responses based on user history and prior misunderstandings

Maintain an instructional, academic tone (not answer-dumping)

This component transforms raw questions into pedagogically meaningful feedback.

Persistence Layer (User Data & Context)

Purpose
Safely store and retrieve user-specific data required for personalization and continuity.

Responsibilities

Store user profiles and metadata

Persist conversation history and learning context

Enable longitudinal tracking of topics and difficulties

Enforce strict per-user data ownership

Data storage is fully managed and serverless, optimized for document-based, user-keyed access patterns.

Cloud Infrastructure & Deployment

Purpose
Provide a secure, scalable, low-maintenance runtime environment.

Responsibilities

Host the application as a stateless service

Secure secrets and credentials

Enforce IAM-based access control

Scale automatically with demand

The infrastructure is intentionally minimal, favoring managed services to reduce operational complexity.

End-to-End User Experience (Conceptual)

A WGU student visits the application

The student signs in using their institutional Outlook account

The system identifies the student and loads their learning context

The student asks a Calculus I question

The system:

Interprets the question

Applies curriculum-aware reasoning

Responds with structured, instructional feedback

The interaction is saved for future continuity

The student iterates until understanding improves

Design Philosophy

Educational first — explanations over answers

Minimal surface area — fewer moving parts, fewer failures

Strong identity boundaries — user data is always isolated

Serverless where possible — low operational overhead and high reliability

Leveraged Technologies
Application Framework

FastAPI
Serves as the core application framework, responsible for request handling, routing, and orchestration between authentication, AI services, persistence, and the user interface.

Templating & Presentation

Jinja2
Used for server-side rendering of HTML pages, enabling dynamic content generation while keeping the frontend simple and tightly integrated with the backend.

Tailwind CSS with daisyUI
Tailwind provides a utility-first styling system that enables polished UI design without custom CSS complexity. daisyUI adds higher-level components for consistency and accessibility.

Authentication & Identity

Microsoft Entra ID (formerly Azure Active Directory)
Used as the identity provider to authenticate students via institutional Outlook accounts, eliminating the need for custom credential management.

AI Model Platform

Google Gemini
Powers the conversational reasoning engine, delivering context-aware, instructional responses aligned to Calculus I concepts.

Data Persistence

Google Firestore (Native Mode)
A fully managed, serverless document database used to store user profiles, conversation history, and learning context.

Cloud Platform & Infrastructure

Google Cloud Platform (GCP)
Provides the hosting and infrastructure foundation for the application.

Cloud Run
Hosts the application as a stateless, containerized service with automatic scaling.

Google Cloud IAM & Secret Manager
IAM enforces least-privilege access, while Secret Manager securely stores sensitive configuration and credentials.

Browser-Side Logic

Vanilla JavaScript (Minimal Use)
Handles user interaction and asynchronous communication with the backend while avoiding frontend framework complexity.

Summary

Together, these technologies form a low-friction, secure, and extensible architecture that prioritizes instructional quality, operational simplicity, and user trust. The stack deliberately avoids unnecessary complexity while remaining robust enough to support future expansion beyond Calculus I.
