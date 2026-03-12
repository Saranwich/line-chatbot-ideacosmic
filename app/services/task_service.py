from sqlmodel import Session, select
from app.models.task import Task

class TaskService :
    def __init__(self, session : Session):
        self.session = session
        
    def create_task (self, user_id : int, title : str) -> Task:
        """create and return new class

        Args:
            user_id (int): The primary key (id) of the user who owns the task.
            title (str): The name or description of the task.

        Returns:
            Task:  The newly created task object.
        """
        task = Task(user_id=user_id, title=title, status="OPEN")
        self.session.add(task)
        self.session.commit()
        self.session.refresh(task)
        return task
    
    def get_all_task_by_user_id (self, user_id : int) -> list[Task]:
        """Find and return all tasks belonging to a specific user by user id

        Args:
            user_id (int): the primary key (id) of the user

        Returns:
            list[Task]: A list of task objects.
        """
        statement = select(Task).where(Task.user_id == user_id)
        tasks = self.session.exec(statement).all()
        return tasks 
        
    def update_task_status (self, task_id: int, new_status: str) -> Task:
        """Updates task status of a specific task

        Args:
            task_id (int): The primary key (id) of the task.
            new_status (str): The new status (e.g., 'CLOSED').
            
        Returns:
            Task: The updated task object.
        """
        task = self.session.get(Task, task_id)
        if task :
            task.status = new_status
            self.session.commit()
            self.session.refresh(task)
        return task
        
    def delete_task(self, task_id: int) -> bool:
        """Deletes a specific task from the database.

        Args:
            task_id (int): The primary key (id) of the task.

        Returns:
            bool: True if deletion was successful, False if task not found.
        """
        task = self.session.get(Task, task_id)
        if task :
            self.session.delete(task)
            self.session.commit()
            return True
        return False