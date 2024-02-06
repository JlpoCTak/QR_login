import segno
import cv2
import sqlite3
import json


class Worker:
    def __init__(self, id_worker, tg_id, first_name, patronymic, last_name, age, profession):
        self.id_worker = id_worker
        self.tg_id = tg_id
        self.first_name = first_name
        self.patronymic = patronymic
        self.last_name = last_name
        self.age = age
        self.profession = profession


    def generate_qr(self):
        data_worker = (f'{self.id_worker};{self.first_name};'
                       f'{self.patronymic};{self.last_name};'
                       f'{self.age};{self.profession}')

        qrcode = segno.make_qr(data_worker)
        qrcode.save('test.png', scale=7)


def read_qr():
    img = cv2.imread('test.png')
    detector = cv2.QRCodeDetector()
    data, bbox, straight_qrcode = detector.detectAndDecode(img)
    return data


worker1 = Worker(1, '657529187', 'Igor', 'Kopylov', 'Igorevich',
                 18, 'programmer')

worker1.generate_qr()


print(read_qr())
