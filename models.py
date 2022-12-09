from config import SQLALCHEMY_DATABASE_URI

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from cloudinary_util import cloudinaryUtils
import json

cloud = cloudinaryUtils()
db = SQLAlchemy()


def setup_db(app, database_path=SQLALCHEMY_DATABASE_URI):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.app_context().push()
    db.app = app
    db.init_app(app)
    db.create_all()


class FilesData(db.Model):

    file_name = db.Column(db.String(), primary_key=True, nullable=False)
    public_id = db.Column(db.String(), nullable=False)
    file_url = db.Column(db.String(), nullable=False)
    upload_date = db.Column(db.String(), nullable=False)

    def __init__(self, data):
        print("inserting fileds in their respective attributes...")
        try:
            self.file_name = data.get("name")
            self.public_id = data.get("publicId")
            self.url = data.get("url")
            self.upload_date = data.get("uploadDate")
        except:
            raise Exception("Missing fields")
        print("done.")

    @classmethod
    def create_new_file(cls, file):
        print("checking if file exists in data...")
        file_in_database = FilesData.query.filter(
            FilesData.file_name == file.filename).one_or_none()

        if file_in_database:
            print("file exists in database")
            raise Exception("File already exists in database")

        print("done: file does not exist in database.")

        # upload file
        print("uploading file...")
        upload_data = cloud.uploadFile(file)
        print("done.")

        data = {
            "name": file.filename,
            "publicId": upload_data.get("public_id"),
            "uploadDate": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        }
        print("creating object...")
        return cls(data)

    def insert(self):
        print("preparing to insert data into database")
        db.session.add(self)
        db.session.commit()
        print("Finished inserting the data")
        print("Fetching newly inserted data from database...")
        new_entry = FilesData.query.filter(
            FilesData.file_name == self.file_name).one_or_none()
        if new_entry == None:
            raise Exception("File already exists in database")
        return new_entry.format()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def format(self):
        return {
            "fileName": self.file_name,
            "publicId": self.public_id,
            "url": self.url,
            "uploadDate": self.upload_date
        }

    def __repr__(self):
        return json.dumps(self.format())
