import cv2

def generate_dataset():
    face_classifier = cv2.CascadeClassifier("lbpcascade_frontalface_opencv.xml")
    
    def face_cropped(img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)
        
        if len(faces) == 0:
            return None
        else:
            # Get the largest face (assuming it's the closest to the camera)
            max_area = 0
            for (x, y, w, h) in faces:
                area = w * h
                if area > max_area:
                    max_area = area
                    largest_face = (x, y, w, h)
            x, y, w, h = largest_face
            cropped_face = img[y:y+h, x:x+w]
            return cropped_face
    
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)  # Set width to 1920 pixels
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)  # Set height to 1080 pixels
    
    id = 1
    img_id = 0

    while True:
        ret, frame = cap.read()
        if ret:
            cropped_face = face_cropped(frame)
            if cropped_face is not None:
                img_id += 1
                face = cv2.resize(cropped_face, (200, 200))
                face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                file_name_path = f"data/user.{id}.{img_id}.jpg"
                cv2.imwrite(file_name_path, face)
                cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                cv2.imshow("Cropped face", face)
                if cv2.waitKey(4) == 13 or img_id == 10:
                    break
            else:
                cv2.imshow("Cropped face", frame)  # Show full frame if no face is detected
                if cv2.waitKey(4) == 13:
                    break
        else:
            print("Error: Failed to capture frame")
            break

    cap.release()
    cv2.destroyAllWindows()
    print("Collecting Samples is completed..............")

generate_dataset()


