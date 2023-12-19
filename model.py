from db import Base, Session, engine
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from datetime import date

tables = {
    1: 'USER',
    2: 'Projects',
    3: 'Comments',
}

s = Session()

class USER(Base):
    __tablename__ = 'USER'
    user_ID = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)

    projects = relationship("Projects")
    comments = relationship("Comments")

    def init(self, user_ID, username, email):
        self.user_ID = user_ID
        self.username = username
        self.email = email

class Projects(Base):
    __tablename__ = 'Projects'
    project_ID = Column(Integer, primary_key=True)
    Date_of_publication = Column(Date)
    projectname = Column(String)

    user_ID = Column(Integer, ForeignKey('USER.user_ID'))

    comments = relationship("Comments")

    def init(self, project_ID, user_ID, Date_of_publication, projectname):
        self.project_ID = project_ID
        self.user_ID = user_ID
        self.Date_of_publication = Date_of_publication
        self.projectname = projectname

class Comments(Base):
    __tablename__ = 'Comments'
    comment_id = Column(Integer, primary_key=True)
    text = Column(String)
    date_of_publication = Column(Date)

    project_id = Column(Integer, ForeignKey('Projects.project_ID'))
    user_id = Column(Integer, ForeignKey('USER.user_ID'))

    def init(self, comment_id, project_id, user_id, text, date_of_publication):
        self.comment_id = comment_id
        self.project_id = project_id
        self.user_id = user_id
        self.text = text
        self.date_of_publication = date_of_publication


class Model:
    def __init__(self):
        self.session = Session()
        self.connection = engine.connect()

    @staticmethod
    def add_user(user_ID:int, username:str, email:str) -> None:
        user = USER(user_ID=user_ID, username=username, email=email)
        s.add(user)
        s.commit()

    @staticmethod
    def add_project(project_ID:int, user_ID:int, Date_of_publication:date, projectname:str) -> None:
        project = Projects(project_ID=project_ID, user_ID=user_ID, Date_of_publication=Date_of_publication, projectname=projectname)
        s.add(project)
        s.commit()

    @staticmethod
    def add_comment(comment_id:int, project_id:int, user_id:int, text:str, date_of_publication:date) -> None:
        comment = Comments(comment_id=comment_id, project_id=project_id, user_id=user_id, text=text, date_of_publication=date_of_publication)
        s.add(comment)
        s.commit()

    @staticmethod
    def view_user():
        return s.query(USER.user_ID, USER.username, USER.email).all()

    @staticmethod
    def view_project():
        return s.query(Projects.project_ID, Projects.user_ID, Projects.Date_of_publication, Projects.projectname).all()

    @staticmethod
    def view_comment():
        return s.query(Comments.comment_id, Comments.project_id, Comments.user_id, Comments.text, Comments.date_of_publication).all()

    @staticmethod
    def update_user(user_ID:int, username:str, email:str) -> None:
        s.query(USER).filter_by(user_ID=user_ID).update({USER.username:username, USER.email:email})
        s.commit()

    @staticmethod
    def update_project(project_ID:int, Date_of_publication:date, projectname:str) -> None:
        s.query(Projects).filter_by(project_ID=project_ID).update({Projects.Date_of_publication:Date_of_publication, Projects.projectname:projectname})
        s.commit()

    @staticmethod
    def update_comment(comment_id:int, text:str, date_of_publication:date) -> None:
        s.query(Comments).filter_by(comment_id=comment_id).update({Comments.text:text, Comments.date_of_publication:date_of_publication})
        s.commit()

    @staticmethod
    def delete_user(user_ID) -> None:
        user = s.query(USER).filter_by(user_ID=user_ID).one()
        s.delete(user)
        s.commit()

    @staticmethod
    def delete_project(project_ID) -> None:
        project = s.query(Projects).filter_by(project_ID=project_ID).one()
        s.delete(project)
        s.commit()

    @staticmethod
    def delete_comment(comment_id) -> None:
        comment = s.query(Comments).filter_by(comment_id=comment_id).one()
        s.delete(comment)
        s.commit()
