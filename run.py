from ultralytics import YOLO

# 加载一个预训练的 YOLO11n 模型
yolo = YOLO(model="yolov8n.pt",task="detect")

result = yolo(source="ultralytics/assets/bus.jpg")

# result = yolo(source=0) # 通过摄像头检测