from ultralytics import YOLO
import cv2
model = YOLO("yolov8n.pt")  # 轻量模型
image = cv2.imread("")
model.predict("your_image.jpg", show=True)