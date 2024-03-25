import cv2
import numpy as np

# 비디오 파일 열기
cap = cv2.VideoCapture('bird.mp4')

# 비디오 파일이 열렸는지 확인
if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

# 비디오 프레임의 폭과 높이 가져오기
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 새로운 비디오 파일을 생성하기 위한 설정
out = cv2.VideoWriter('cartoon_bird.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, (frame_width, frame_height))

# 비디오 파일이 끝날 때까지 반복
while cap.isOpened():
    # 비디오에서 프레임 읽기
    ret, frame = cap.read()

    # 비디오 파일의 끝에 도달하면 종료
    if not ret:
        break

    # Convert the image to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Apply median blur to reduce noise
    gray = cv2.medianBlur(gray, 5)
    # Detect edges using adaptive thresholding
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    # Convert the image to color
    color = cv2.bilateralFilter(frame, 9, 300, 300)
    # Combine the color image with the edges mask
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    # 새로운 비디오 파일에 프레임 쓰기
    out.write(cartoon)

    # 프레임 표시
    cv2.imshow('Cartoon', cartoon)

    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 비디오 파일과 윈도우 창 닫기
cap.release()
out.release()
cv2.destroyAllWindows()
