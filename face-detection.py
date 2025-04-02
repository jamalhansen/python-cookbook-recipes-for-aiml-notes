import cv2

group_photo = cv2.imread('group-photo.webp')
grayscale_photo = cv2.cvtColor(group_photo, cv2.COLOR_BGR2GRAY)

# cv2.imwrite('group-photo-grayscale.jpg', grayscale_photo)

face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
faces = face_classifier.detectMultiScale(grayscale_photo, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

print(faces)
print(f"Found {len(faces)} faces in the photo.")

# Save faces to files
for i, (x, y, w, h) in enumerate(faces):
    face = group_photo[y:y+h, x:x+w]
    cv2.imwrite(f'face_{i}.jpg', face)

# Draw rectangles around faces
for (x, y, w, h) in faces:
    cv2.rectangle(group_photo, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow('Group Photo', group_photo)
cv2.waitKey(10000)
cv2.destroyAllWindows()

#cv2.imwrite('Group Photo', group_photo)
