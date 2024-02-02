from db.database import BaseOrm, project_engine
import db.models    #This is an important import, it is necessary for metadata to know about the existence of classes that inherit from BaseOrm


def create_tables():
    project_engine.echo = True
    BaseOrm.metadata.drop_all(project_engine)
    BaseOrm.metadata.create_all(project_engine)


if __name__ == "__main__":
    create_tables()
