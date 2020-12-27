from django.db import models

# Create your models here.

class Notice:
    def __init__(self, contents, date, title, file, image):
        self.contents = contents
        self.date = date
        self.title = title
        self.file = file
        self.image = image
        self.notice_id = None


    def to_dict(self):
        # 딕셔너리 생성
        data = {
            'contents': self.contents,
            'date': self.date,
            'title': self.title,
            'file': self.file,
            'image': self.image,
        }

        # 생성된 딕셔너리 반환
        return data

    def from_dict(data, notice_id):
        # 객체 생성
        notice = Notice(data['contents'], data['date'], data['title'], data['file'], data['image'],)
        notice.notice_id = notice_id

        # 생성된 객체 반환
        return notice

