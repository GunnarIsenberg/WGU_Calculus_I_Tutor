# WGU_Calculus_I_Tutor
A Calc I tutor tailored for WGUs material.

Project Overview

This project is a web application deployed on Google Cloud that provides Western Governors University (Western Governors University) students with a custom-tailored Calculus I chatbot.

The application delivers contextual explanations, guided problem-solving, and concept-level feedback aligned to the WGU Calculus I curriculum, with a focus on topics students historically struggle with (limits, derivatives, applications, and foundational intuition).

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
1. Web Interface (Presentation Layer)

Purpose:
Provide students with a clean, approachable, distraction-free interface for interacting with the Calculus I chatbot.

Responsibilities:

Render the chatbot interface in the browser

Accept user input (questions, partial work, conceptual confusion)

Display structured, readable responses

Maintain conversational continuity during a session

This layer is intentionally lightweight. It exists solely to support learning interactions, not to perform business logic.

2. Application Server (Orchestration Layer)

Purpose:
Act as the central coordinator between the user interface, authentication system, AI model, and data storage.

Responsibilities:

Serve web pages and API endpoints

Enforce authentication and session validation

Normalize and route user requests

Apply user-specific context (progress, prior questions)

Return structured responses to the frontend

This layer defines the application’s behavior and rules but remains stateless between requests.

3. Authentication & Identity Management

Purpose:
Ensure only authorized students can access the system, while minimizing friction and password management.

Responsibilities:

Authenticate users via institutional Microsoft accounts (Outlook)

Validate identity and session state

Derive a stable, unique user identifier

Gate access to all protected application features

Authentication is handled through Microsoft’s identity platform (Microsoft Entra ID), allowing students to sign in using credentials they already trust.

4. AI Reasoning Engine (Learning Core)

Purpose:
Provide intelligent, curriculum-aware Calculus I assistance tailored to each student.

Responsibilities:

Interpret student questions and misconceptions

Generate step-by-step explanations and conceptual clarifications

Adjust responses based on user history and prior misunderstandings

Maintain instructional tone aligned with academic learning (not answer-dumping)

This component transforms raw questions into pedagogically meaningful feedback.

5. Persistence Layer (User Data & Context)

Purpose:
Safely store and retrieve user-specific data required for personalization and continuity.

Responsibilities:

Store user profiles and metadata

Persist conversation history and learning context

Enable longitudinal tracking of topics and difficulties

Enforce strict per-user data ownership

Data storage is fully managed and serverless, optimized for document-based, user-keyed access patterns.

6. Cloud Infrastructure & Deployment

Purpose:
Provide a secure, scalable, low-maintenance runtime environment.

Responsibilities:

Host the application as a stateless service

Secure secrets and credentials

Enforce IAM-based access control

Scale automatically with demand

The infrastructure is intentionally minimal, favoring managed services to reduce operational complexity.

End-to-End User Experience (Conceptual)

A WGU student visits the application

They sign in using their institutional Outlook account

The system identifies them and loads their learning context

The student asks a Calculus I question

The system:

Interprets the question

Applies curriculum-aware reasoning

Responds with structured, instructional feedback

The interaction is saved for future continuity

The student iterates until understanding improves

Design Philosophy

Educational first – explanations over answers

Minimal surface area – fewer moving parts, fewer failures

Strong identity boundaries – user data is always isolated

Serverless where possible – low ops, high reliability

Leveraged Technologies
Application Framework

FastAPI
FastAPI serves as the core application framework, responsible for request handling, routing, and orchestration between authentication, AI services, persistence, and the user interface. It enables a clean separation between presentation logic and application behavior while supporting modern web standards and scalable cloud deployment.

Templating & Presentation

Jinja2
Jinja2 is used for server-side rendering of HTML pages. It enables dynamic content generation while keeping the frontend intentionally simple and tightly integrated with the backend.

Tailwind CSS with daisyUI
Tailwind provides a utility-first styling system that allows the interface to be visually polished without custom CSS complexity. daisyUI adds a higher-level component abstraction, enabling consistent, accessible UI elements with minimal design effort.

Authentication & Identity

Microsoft Entra ID (formerly Azure Active Directory)
Microsoft Entra ID is used as the identity provider, allowing students to authenticate using their institutional Outlook accounts. This removes the need for custom credential management while ensuring strong, standards-based identity validation.

AI Model Platform

Google Gemini
Gemini powers the conversational reasoning engine. It is leveraged to deliver context-aware, instructional responses tailored to Calculus I concepts, enabling guided explanations, conceptual reinforcement, and adaptive feedback.

Data Persistence

Google Firestore (Native Mode)
Firestore provides a fully managed, serverless document database used to store user profiles, conversation history, and learning context. Its document-oriented structure aligns naturally with per-user data isolation and simplifies authorization enforcement.

Cloud Platform & Infrastructure

Google Cloud Platform (GCP)
GCP provides the hosting and infrastructure foundation for the application, offering secure identity integration, managed runtime services, and seamless scaling.

Cloud Run
Cloud Run hosts the application as a stateless, containerized service. It enables automatic scaling, minimal operational overhead, and tight integration with other GCP services.

Google Cloud IAM & Secret Manager
IAM enforces least-privilege access between services, while Secret Manager securely stores sensitive configuration such as API credentials and authentication secrets.

Browser-Side Logic

Vanilla JavaScript (Minimal Use)
A small amount of client-side JavaScript handles user interaction and asynchronous communication with the backend. This avoids frontend framework complexity while still enabling a responsive, conversational experience.

Summary

Together, these technologies form a low-friction, secure, and extensible architecture that prioritizes instructional quality, operational simplicity, and user trust. The stack deliberately avoids unnecessary complexity while remaining robust enough to support future expansion beyond Calculus I.
