from sqlmodel import Session, create_engine, SQLModel
from app import config
from app.services.user_service import UserService
from app.models.user import User

# ใช้ TEST_DATABASE_URL จาก .env เพื่อความ Scalable และสมจริง
if not config.TEST_DATABASE_URL:
    raise ValueError("TEST_DATABASE_URL not found in .env. Please set it up for testing.")

test_engine = create_engine(config.TEST_DATABASE_URL, echo=True)

def setup_test_db():
    """เตรียมฐานข้อมูลสำหรับการทดสอบ (สร้าง Table)"""
    SQLModel.metadata.create_all(test_engine)

def test_user_service_flow():
    # 1. Setup
    setup_test_db()
    
    with Session(test_engine) as session:
        user_service = UserService(session)
        
        test_line_id = "U_PRO_TEST_99"
        test_name = "Scalable Tester"

        print("\n--- 🚀 Starting Professional Test Flow (PostgreSQL) ---")

        # 2. Test: Get (Should be None)
        print("1. Testing: Get non-existing user...")
        user = user_service.get_user_by_line_id(test_line_id)
        assert user is None
        print("✅ PASS: User not found as expected.")

        # 3. Test: Auto Create
        print(f"2. Testing: Auto-creating user: {test_name}...")
        user = user_service.get_user_by_line_id(test_line_id, auto_create=True, display_name=test_name)
        assert user is not None
        assert user.line_user_id == test_line_id
        assert user.display_name == test_name
        print(f"✅ PASS: User created successfully. (ID: {user.id})")

        # 4. Test: Get Existing
        print("3. Testing: Getting existing user (No duplicate creation)...")
        existing_user = user_service.get_user_by_line_id(test_line_id)
        assert existing_user.id == user.id
        print(f"✅ PASS: Found existing user. (ID: {existing_user.id})")

        print("--- 🎉 All Tests Passed! ---\n")

if __name__ == "__main__":
    try:
        test_user_service_flow()
    except Exception as e:
        print(f"\n❌ TEST FAILED: {str(e)}")
        print("Tip: Make sure you created 'ideacosmic_test' database in PostgreSQL.")
