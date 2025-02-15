#importing libraries.

import cv2
from mtcnn import MTCNN

#reading the image
image_path = "face.jpeg"
image = cv2.imread(image_path)

#converting image rgb.

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#initializing MTCNN detector
detector = MTCNN()
faces = detector.detect_faces(image_rgb)

print("detected faces", faces)

#drawing bounding box
for face in faces:
    x,y,width,height = face['box']
    cv2.rectangle(image, (x,y), (x+width, y+height), (0, 255, 0), 2)
    
#save the output image file.
output_path = "output.jpeg"
cv2.imwrite(output_path, image)
print('output is saved')