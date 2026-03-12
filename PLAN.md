# 📅 Task-Reminder Bot (IdeaCosmic) - Project Plan

## 🎯 1. Project Vision
A professional-grade LINE Chatbot designed to help users manage tasks and receive automated reminders. This project follows **MVC (Model-View-Controller)** architecture and separates **Core Business Logic** from **LINE-specific Logic** for maximum scalability and maintainability.

## 🗺️ 2. The Master Roadmap

### Phase 1: The Architect (Database & MVC Design)
- [x] Define PostgreSQL Schema (Users, Tasks, Reminders).
- [x] Design Data Storing Approaches (Handling repeating tasks).
- [x] Establish MVC folder structure.

### Phase 2: The Foundation (Postgres & Core Backend)
- [x] Set up PostgreSQL with SQLAlchemy/SQLModel. (Connection & Tables are LIVE! 🚀)
- [ ] Implement Database Migrations with Alembic.
- [x] Build `TaskService` (Full CRUD: Create, Read, Update, Delete). ✅
- [x] Build `UserService` (Core CRUD logic for Users). ✅
- [x] Set up Professional Testing Suite (Centralized `test_utils.py` and separate CRUD tests). ✅

### Phase 3: The Messenger (LINE Integration)
- [x] Implement FastAPI Webhook with Signature Validation. ✅
- [x] Implement `FollowEvent` (Add Friend) logic. ✅
- [ ] Build a **Smart Dispatcher** using a Dictionary/Map to route commands (Planned for Tomorrow! 🧠).
- [ ] Implement Text Handlers for "Add" and "List" commands.
- [ ] Design Flex Message UI for Task Dashboard.

### Phase 4: The "Hell" (Background Tasks & Geo-Logic)
- [ ] Implement Background Workers (APScheduler/Celery) for push notifications.
- [ ] Handle Timezones (`pytz`) for accurate reminders.
- [ ] Implement Geo-spatial logic for location-based tagging.

## 📍 3. Current Status (Updated: 2026-03-12)
**Where you are:**
- **The Brain is Strong:** `TaskService` and `UserService` are fully functional and tested independently.
- **The Laboratory is Clean:** You have a professional test environment (`tests/test_utils.py`) that resets the DB for every test.
- **The Bridge is Open:** `FollowEvent` and `MessageEvent` are correctly received from LINE.

**Next Learning Challenges (For Tomorrow):**
1. **The Smart Dispatcher:** Refactor `message_handler.py` to use a **Dictionary-based Command Map** (the "Pro" way you designed!).
2. **The Session Bridge:** Update `main.py` to correctly inject the database session into the handlers.
3. **Integration Test:** Perform the first "Real-World" test by adding a task through the LINE chat.

## 🗄️ 4. Database Schema (Live State)

### Tables
- **users**: Stores LINE IDs and display names.
- **tasks**: Stores user tasks with statuses (OPEN, CLOSED).
- **reminders**: (Schema defined, logic pending).

---
*Last Updated: 2026-03-12 (Night)*
