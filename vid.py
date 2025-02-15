#importing libraries.

import cv2
from mtcnn import MTCNN

#initialize MTCNN detector.
detector = MTCNN()

#input video file
video_path = "video.mp4"
cap = cv2.VideoCapture(video_path)

#output video file
output_path = "output.mp4"
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

while cap.isOpened():
    ret, frame = cap.read()
    
    if not ret:
        break
    
    #convert frame to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    
    #detect faces
    faces = detector.detect_faces(rgb_frame)
    
    #drawing boxes
    for face in faces:
        x, y, width, height = face['box']
        cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 255, 0), 2)
        
        #frame in the output video
        out.write(frame)
        
        #displaying result in the video
        cv2.imshow('face detecttion', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
cap.release()
out.release()
cv2.destroyAllWindows()

print('output video is saved')        
