# 📅 Task-Reminder Bot (IdeaCosmic) - Project Plan

## 🎯 1. Project Vision
A professional-grade LINE Chatbot designed to help users manage tasks and receive automated reminders. This project follows **MVC (Model-View-Controller)** architecture and separates **Core Business Logic** from **LINE-specific Logic** for maximum scalability and maintainability.

## 🗺️ 2. The Master Roadmap

### Phase 1: The Architect (Database & MVC Design)
- [x] Define PostgreSQL Schema (Users, Tasks, Reminders, Locations).
- [x] Design Data Storing Approaches (Handling repeating tasks, image storage).
- [x] Establish MVC folder structure.

### Phase 2: The Foundation (Postgres & Core Backend)
- [x] Set up PostgreSQL with SQLAlchemy/SQLModel. (Connection & Tables are LIVE! 🚀)
- [ ] Implement Database Migrations with Alembic.
- [ ] Build `TaskService` (Core CRUD logic independent of LINE).

### Phase 3: The Messenger (LINE Integration)
- [x] Implement FastAPI Webhook with Signature Validation.
- [ ] Build the **Dispatcher** to route incoming events.
- [ ] Create Text, Image, and Location Handlers.
- [ ] Design Flex Message UI for Task Dashboard.

### Phase 4: The "Hell" (Background Tasks & Geo-Logic)
- [ ] Implement Background Workers (APScheduler/Celery) for push notifications.
- [ ] Handle Timezones (`pytz`) for accurate reminders.
- [ ] Implement Geo-spatial logic for location-based tagging.

## 📍 3. Current Status (Updated: 2026-03-10)
**Where you are:**
- **The Body is Ready:** Database tables (`users`, `tasks`, `reminders`) exist on your SSD.
- **The Bridge is Built:** Python can talk to Postgres via the `lifespan` manager.

**Next Learning Challenges (For Tomorrow):**
1. **The First Record:** ทดลองเขียนข้อมูลผู้ใช้คนแรก (User) ลงไปในตารางเมื่อมีคนทัก LINE มา
2. **The Logic (Service):** สร้าง `TaskService` เพื่อจัดการข้อมูลโดยไม่ต้องเขียน SQL เองบ่อยๆ


## 🗄️ 4. Database Schema (Draft)

### Tables (Conceptual)
```dbml
Table users {
  id integer [primary key]
  line_user_id varchar [unique]
  display_name varchar
  timezone varchar [default: 'Asia/Bangkok']
  created_at timestamp [default: `now()`]
}

Table tasks {
  id integer [primary key]
  user_id integer [ref: > users.id]
  title varchar
  status varchar [default: 'OPEN']
  image_url varchar [note: 'Link to storage bucket']
}

Table reminders {
  id integer [primary key]
  task_id integer [ref: > tasks.id]
  remind_time time
  is_active boolean [default: true]
  repeat_days varchar [note: 'e.g. 1,2,3 for Mon,Tue,Wed']
  last_sent_at timestamp
}
```

---
*Last Updated: 2025-03-09*
