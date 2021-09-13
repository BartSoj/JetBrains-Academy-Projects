from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from datetime import timedelta
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///todo.db?check_same_thread=False')
Base = declarative_base()


class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String)
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return f"{self.task}. {self.deadline.day} {self.deadline.strftime('%b')}"


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def print_today_tasks():
    tasks = session.query(Task).filter(datetime.today().date() == Task.deadline).all()
    print("Today", datetime.today().day, datetime.today().strftime("%b"))
    if tasks:
        for task in tasks:
            print(task)
    else:
        print("Nothing to do!")


def print_week_tasks():
    tasks = session.query(Task).filter(datetime.today() + timedelta(days=7) >= Task.deadline).all()
    for i in range(7):
        date = datetime.today().date() + timedelta(i)
        weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        print(weekdays[date.weekday()], date.day, date.strftime("%b"))
        printed = False
        for task in tasks:
            if task.deadline == date:
                print(task)
                printed = True
        if not printed:
            print("Nothing to do!")
        print()


def print_all_tasks():
    tasks = session.query(Task).order_by(Task.deadline).all()
    print("All tasks")
    if tasks:
        for task in tasks:
            print(task)
    else:
        print("Nothing to do!")


def print_missed_tasks():
    tasks = session.query(Task).filter(datetime.today().date() > Task.deadline).all()
    print("Missed tasks:")
    if tasks:
        for task in tasks:
            print(task)
    else:
        print("Nothing is missed!")


def add_task():
    task = input("Enter task\n")
    deadline = input("Enter deadline\n")
    print("The task has been added!")
    session.add(Task(task=task, deadline=datetime.strptime(deadline, "%Y-%m-%d").date()))
    session.commit()


def delete_task():
    print("Choose the number of the task you want to delete:")
    tasks = session.query(Task).order_by(Task.deadline).all()
    for task in tasks:
        print(task)
    num = int(input())
    print("The task has been deleted!")
    session.delete(tasks[num - 1])
    session.commit()


def main():
    while True:
        print("1) Today's tasks")
        print("2) Week's tasks")
        print("3) All tasks")
        print("4) Missed tasks")
        print("5) Add task")
        print("6) Delete task")
        print("0) Exit")
        choice = input()
        print()
        if choice == "0":
            break
        elif choice == "1":
            print_today_tasks()
        elif choice == "2":
            print_week_tasks()
        elif choice == "3":
            print_all_tasks()
        elif choice == "4":
            print_missed_tasks()
        elif choice == "5":
            add_task()
        elif choice == "6":
            delete_task()
        print()
    print("Bye!")


main()
