from sqlmodel import Session, select
from app.models.user import User

class UserService :
    def __init__(self, session : Session):
        self.session = session

    def get_user_by_line_id(self, line_user_id: str, auto_create: bool = False, display_name: str = "Unknown") -> User:
        """find and return User instance by user's line id

        Args:
            line_user_id (str): user's line id of target
            auto_create (bool, optional): create a new User if cannot found from given user's line id. Defaults to False.
            display_name (str): user's display name by auto create after not found user from line id. Defaults to "Unknow".

        Returns:
            User: target user
        """
        statement = select(User).where(User.line_user_id == line_user_id)
        user =  self.session.exec(statement).first()
        if not user :
            if auto_create :
                return self.create_user(line_user_id=line_user_id,display_name=display_name)
            return None
        return user

    def create_user(self, line_user_id : str, display_name : str, echo : bool = False) -> User:
        """create and return new user instance

        Args:
            line_user_id (str): user's line id
            display_name (str): user's display name
            echo (bool, optional): printing text on teminal. Defaults to False.

        Returns:
            User: user instance
        """
        user = User(line_user_id=line_user_id, display_name=display_name)
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        if echo : print(f"Create new user:{display_name}")
        return user
