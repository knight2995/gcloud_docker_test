import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage

import numpy as np
import cv2


cred = credentials.Certificate('serviceAccountKey.json')
firebase_admin.initialize_app(cred, {
    'storageBucket': 'fir-page-bb0d1.appspot.com'
})

bucket = storage.bucket()

blob = bucket.blob('up_octo.jpg')

contents = blob.download_as_string()

encoded_img = np.frombuffer(contents, dtype = np.uint8)
image = cv2.imdecode(encoded_img,  cv2.IMREAD_COLOR)

image = cv2.flip(image, 0)

upload_blob = bucket.blob('down_octo.jpg')

upload_blob.upload_from_string(cv2.imencode('.jpg', image)[1].tobytes(), content_type='image/jpeg')



