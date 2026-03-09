# 📅 Task-Reminder Bot (IdeaCosmic) - Project Plan

## 🎯 1. Project Vision
A professional-grade LINE Chatbot designed to help users manage tasks and receive automated reminders. This project follows **MVC (Model-View-Controller)** architecture and separates **Core Business Logic** from **LINE-specific Logic** for maximum scalability and maintainability.

## 🗺️ 2. The Master Roadmap

### Phase 1: The Architect (Database & MVC Design)
- [ ] Define PostgreSQL Schema (Users, Tasks, Reminders, Locations).
- [ ] Design Data Storing Approaches (Handling repeating tasks, image storage).
- [ ] Establish MVC folder structure.

### Phase 2: The Foundation (Postgres & Core Backend)
- [ ] Set up PostgreSQL with SQLAlchemy/SQLModel.
- [ ] Implement Database Migrations with Alembic.
- [ ] Build `TaskService` (Core CRUD logic independent of LINE).

### Phase 3: The Messenger (LINE Integration)
- [ ] Implement FastAPI Webhook with Signature Validation.
- [ ] Build the **Dispatcher** to route incoming events.
- [ ] Create Text, Image, and Location Handlers.
- [ ] Design Flex Message UI for Task Dashboard.

### Phase 4: The "Hell" (Background Tasks & Geo-Logic)
- [ ] Implement Background Workers (APScheduler/Celery) for push notifications.
- [ ] Handle Timezones (`pytz`) for accurate reminders.
- [ ] Implement Geo-spatial logic for location-based tagging.

## 📍 3. Current Focus
**Step 1.1: Designing the Database Schema (ERD)**
- Defining tables for Users, Tasks, and Reminders.
- Deciding on the "Repeating Task" data structure.

## 🗄️ 4. Database Schema (Draft)

### Tables (Conceptual)
1. **`users`**
   - `id`: Internal Primary Key.
   - `line_user_id`: The unique ID from LINE.
   - `display_name`: User's name.
   - `timezone`: Crucial for "8:00 AM" to mean the *user's* 8:00 AM.
   - `created_at`: Metadata.

2. **`tasks`**
   - `id`: Internal Primary Key.
   - `user_id`: Foreign Key to `users`.
   - `title`: The "What" (e.g., "Buy Milk").
   - `status`: 'OPEN' (Active) or 'CLOSED' (Marked as done, no more reminders).
   - `image_url`: Link to an image (if attached).

3. **`reminders`**
   - `id`: Internal Primary Key.
   - `task_id`: Foreign Key to `tasks`.
   - `remind_time`: The specific time (e.g., 08:00).
   - `is_active`: Boolean (True = Bot keeps reminding, False = User sent "Stop").
   - `repeat_days`: String (e.g., "1,2,3,4,5,6,7" for daily).
   - `last_sent_at`: Timestamp (Used by the background worker to avoid double-sending).

---
*Last Updated: 2025-03-09*
