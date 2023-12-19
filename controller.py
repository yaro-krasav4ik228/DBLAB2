from model import Model
from view import View


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()

    def run(self):
        while True:
            choice = self.show_menu()
            if choice == '1':
                self.run_tablets_add()
            elif choice == '2':
                self.run_tablets()
            elif choice == '3':
                self.run_tablets_update()
            elif choice == '4':
                self.run_tablets_delete()
            elif choice == '7':
                break

    def run_tablets(self):
        while True:
            choice = self.show_menu_tablets()
            if choice == '1':
                self.show_user()
            elif choice == '2':
                self.show_project()
            elif choice == '3':
                self.show_comment()
            elif choice == '4':
                break

    def run_tablets_update(self):
        while True:
            choice = self.show_menu_tablets()
            if choice == '1':
                self.update_task_tab1()
            elif choice == '2':
                self.update_task_tab2()
            elif choice == '3':
                self.update_task_tab3()
            elif choice == '4':
                break

    def run_tablets_add(self):
        while True:
            choice = self.show_menu_tablets()
            if choice == '1':
                self.add_task_tab1()
            elif choice == '2':
                self.add_task_tab2()
            elif choice == '3':
                self.add_task_tab3()
            elif choice == '4':
                break

    def run_tablets_delete(self):
        while True:
            choice = self.show_menu_tablets()
            if choice == '1':
                self.delete_task_tab1()
            elif choice == '2':
                self.delete_task_tab2()
            elif choice == '3':
                self.delete_task_tab3()
            elif choice == '4':
                break

    def show_menu(self):
        self.view.show_message("\nMenu:")
        self.view.show_message("1. Add Task")
        self.view.show_message("2. View Tasks")
        self.view.show_message("3. Update Task")
        self.view.show_message("4. Delete Task")
        self.view.show_message("7. Quit")
        return input("Enter your choice: ")

    def show_menu_tablets(self):
        self.view.show_message("\nTablets:")
        self.view.show_message("1. USER")
        self.view.show_message("2. Projects")
        self.view.show_message("3. Comments")
        self.view.show_message("4. Quit")
        return input("Enter your choice: ")

    def add_task_tab1(self):
        userid, title, description = self.view.get_task_input_full_tab1()
        self.model.add_user(userid, title, description)

    def add_task_tab2(self):
        projectid, userid, title, description = self.view.get_task_input_full_tab2()
        self.model.add_project(projectid, userid, title, description)

    def add_task_tab3(self):
        commentid, projectid, userid, title, description = self.view.get_task_input_full_tab3()
        self.model.add_comment(commentid, projectid, userid, title, description)

    def show_user(self):
        try:
            user = self.model.view_user()
            self.view.show_user(user)
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def show_project(self):
        try:
            project = self.model.view_project()
            self.view.show_project(project)
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def show_comment(self):
        try:
            comment = self.model.view_comment()
            self.view.show_comment(comment)
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def update_task_tab1(self):
        task_id = self.view.get_task_id()
        title, description = self.view.get_task_input_tab1()
        self.model.update_user(task_id, title, description)

    def update_task_tab2(self):
        task_id = self.view.get_task_id()
        title, description = self.view.get_task_input_tab2()
        self.model.update_project(task_id, title, description)

    def update_task_tab3(self):
        task_id = self.view.get_task_id()
        title, description = self.view.get_task_input_tab3()
        self.model.update_comment(task_id, title, description)

    def delete_task_tab1(self):
        task_id = self.view.get_task_id()
        self.model.delete_user(task_id)

    def delete_task_tab2(self):
        task_id = self.view.get_task_id()
        self.model.delete_project(task_id)

    def delete_task_tab3(self):
        task_id = self.view.get_task_id()
        self.model.delete_comment(task_id)
