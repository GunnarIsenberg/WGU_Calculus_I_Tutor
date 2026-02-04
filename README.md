================================================================================

CALCULUS I TUTOR FOR WGU

================================================================================

A custom-tailored Calculus I chatbot designed specifically for Western Governors
University (WGU) students.

--------------------------------------------------------------------------------
PROJECT OVERVIEW
--------------------------------------------------------------------------------
This project is a web application deployed on Google Cloud that provides WGU 
students with intelligent, context-aware Calculus I assistance.

The application delivers contextual explanations, guided problem-solving, and 
concept-level feedback aligned to the WGU Calculus I curriculum. It is 
specifically tuned to address topics students historically struggle with:
  * Limits
  * Derivatives
  * Applications of derivatives
  * Foundational intuition

The system is designed to be simple to use, secure by default, low-friction to 
operate, and easy to extend as curriculum depth grows.

--------------------------------------------------------------------------------
CORE SYSTEM RESPONSIBILITIES
--------------------------------------------------------------------------------
At a high level, the application is responsible for:
  1. Authenticating users using their existing institutional email accounts.
  2. Serving a clean, modern web interface for interactive learning.
  3. Providing intelligent, context-aware Calculus I assistance.
  4. Persisting user-specific learning context and history.
  5. Enforcing per-user data isolation and validation.

--------------------------------------------------------------------------------
ARCHITECTURE & COMPONENTS
--------------------------------------------------------------------------------

1. WEB INTERFACE (Presentation Layer)
   Purpose: Provide students with a clean, approachable, distraction-free 
   interface.
   Responsibilities:
   - Render the chatbot interface in the browser.
   - Accept user input (questions, partial work, conceptual confusion).
   - Display structured, readable responses.
   - Maintain conversational continuity during a session.
   Note: This layer is lightweight; it supports interactions but performs no 
   business logic.

2. APPLICATION SERVER (Orchestration Layer)
   Purpose: Act as the central coordinator between the UI, Auth, AI, and Data.
   Responsibilities:
   - Serve web pages and API endpoints.
   - Enforce authentication and session validation.
   - Normalize and route user requests.
   - Apply user-specific context (progress, prior questions).
   - Return structured responses to the frontend.

3. AUTHENTICATION & IDENTITY MANAGEMENT
   Purpose: Ensure secure access while minimizing friction.
   Responsibilities:
   - Authenticate users via institutional Microsoft accounts (Outlook).
   - Validate identity and session state.
   - Derive a stable, unique user identifier.
   - Gate access to protected features.

4. AI REASONING ENGINE (Learning Core)
   Purpose: Provide curriculum-aware assistance tailored to the student.
   Responsibilities:
   - Interpret student questions and misconceptions.
   - Generate step-by-step explanations and conceptual clarifications.
   - Adjust responses based on user history.
   - Maintain an instructional, academic tone (educational vs. answer-dumping).

5. PERSISTENCE LAYER (User Data & Context)
   Purpose: Store user-specific data for personalization and continuity.
   Responsibilities:
   - Store user profiles and metadata.
   - Persist conversation history and learning context.
   - Enable longitudinal tracking of topics and difficulties.
   - Enforce strict per-user data ownership.

6. CLOUD INFRASTRUCTURE & DEPLOYMENT
   Purpose: Provide a secure, scalable, low-maintenance runtime environment.
   Responsibilities:
   - Host the application as a stateless service.
   - Secure secrets and credentials.
   - Enforce IAM-based access control.
   - Scale automatically with demand.

--------------------------------------------------------------------------------
TECH STACK
--------------------------------------------------------------------------------

APPLICATION FRAMEWORK
* FastAPI: Core framework responsible for request handling, routing, and 
  orchestration.

AUTHENTICATION
* Microsoft Entra ID (Azure AD): Handles student authentication via 
  institutional Outlook accounts.

AI MODEL
* Google Gemini: Powers the conversational reasoning engine with context-aware, 
  instructional responses.

DATA PERSISTENCE
* Google Firestore (Native Mode): Fully managed, serverless document database 
  for user profiles and history.

CLOUD INFRASTRUCTURE (GCP)
* Cloud Run: Hosts the application as a stateless, containerized service.
* IAM & Secret Manager: Enforces access control and secures credentials.

BROWSER-SIDE LOGIC
* Vanilla JavaScript: Handles user interactions asynchronously without complex 
  frontend frameworks.

--------------------------------------------------------------------------------
USER WORKFLOW (END-TO-END)
--------------------------------------------------------------------------------
1. A WGU student visits the application.
2. The student signs in using their institutional Outlook account.
3. The system identifies the student and loads their learning context.
4. The student asks a Calculus I question.
5. The system interprets the question, applies curriculum reasoning, and 
   responds with instructional feedback.
6. The interaction is saved for future continuity.
7. The student iterates until understanding improves.

--------------------------------------------------------------------------------
DESIGN PHILOSOPHY
--------------------------------------------------------------------------------
* Educational first: Explanations over answers.
* Minimal surface area: Fewer moving parts, fewer failures.
* Strong identity boundaries: User data is always isolated.
* Serverless where possible: Low operational overhead and high reliability.
