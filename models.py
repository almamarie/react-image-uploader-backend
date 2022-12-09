from config import SQLALCHEMY_DATABASE_URI

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from cloudinary_util import cloudinaryUtils

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

    file_name = db.Column(db.String, primary_key=True, nullable=False)
    public_id = db.Column(db.String, nullable=False)
    upload_date = db.Column(db.Date(), nullable=False)

    def __init__(self, data):
        try:
            self.file_name = data.get("name")
            self.public_id = data.get("publicId")
            self.upload_date = data.get("uploadDate")
        except:
            raise Exception("Missing fields")

    @classmethod
    def create_new_file(cls, file):

        # file_in_database = FilesData.query.filter(
        #     FilesData.file_name == file.name).one_or_none()

        # if file_in_database:
        #     raise Exception("File already exists in database")

        # upload file
        upload_data = cloud.uploadFile(file)
        print("Upload data: ", upload_data)
        data = {
            "name": file.name,
            "publicId": upload_data.get("public_id"),
            "uploadDate": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        }
        print("Data: ", data)
