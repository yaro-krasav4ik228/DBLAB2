from datetime import datetime
class View:

    @staticmethod
    def show_user(tasks):
        print("Tasks in tablet USER:")
        for task in tasks:
            print(f"user_ID: {task[0]}, username: {task[1]}, email: {task[2]}")

    @staticmethod
    def show_project(tasks):
        print("Tasks in tablet Projects:")
        for task in tasks:
            print(f"user_ID: {task[1]}, project_id: {task[0]}, Date of publication: {task[2]}, Project name: {task[3]}")

    @staticmethod
    def show_comment(tasks):
        print("Tasks in tablet Comments:")
        for task in tasks:
            print(f"user_ID: {task[2]}, project_id: {task[1]}, comment_id: {task[0]}, text: {task[3]}, Date of publication: {task[4]}")

    @staticmethod
    def get_task_input_full_tab1():
        userid = input("Enter user_id(only available): ")
        title = input("Enter username: ")
        description = input("Enter email: ")
        return userid, title, description

    @staticmethod
    def get_task_input_full_tab2():
        projectid = input("Enter project_id(only available): ")
        userid = input("Enter user_id(only available): ")
        title = input("Enter date: ")
        description = input("Enter projectname: ")
        return projectid, userid, title, description

    @staticmethod
    def get_task_input_full_tab3():
        commentid = input("Enter comment_id(only available): ")
        projectid = input("Enter project_id(only available): ")
        userid = input("Enter user_id(only available): ")
        title = input("Enter text: ")
        description = input("Enter date: ")
        return commentid, projectid, userid, title, description

    @staticmethod
    def get_task_input_tab1():
        title = input("Enter username: ")
        description = input("Enter email: ")
        return title, description

    @staticmethod
    def get_task_input_tab2():
        description = input("Enter project name: ")
        title = input("Enter date (YYYY-MM-DD): ")
        try:
            datetime.strptime(title, '%Y-%m-%d')
        except ValueError:
            print("Error: Date should be in YYYY-MM-DD format.(Will be returned default - 2000-01-01)")
            return description, '2000-01-01'
        return title, description

    @staticmethod
    def get_task_input_tab3():
        title = input("Enter text: ")
        description = input("Enter date (YYYY-MM-DD): ")
        try:
            datetime.strptime(description, '%Y-%m-%d')
        except ValueError:
            print("Error: Date should be in YYYY-MM-DD format.(Will be returned default - 2000-01-01)")
            return title, '2000-01-01'
        return title, description

    @staticmethod
    def get_task_id():
        while True:
            try:
                task_id = int(input("Enter ID: "))
                return task_id
            except ValueError:
                print("Error: Please enter a valid integer ID.")

    @staticmethod
    def show_message(message):
        print(message)
