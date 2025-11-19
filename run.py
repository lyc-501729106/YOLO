# 命令方式训练
# yolo task=detect mode=train model=yolov8n.pt  data=yolo.cattle.yml epochs=30  workers=1 batch=2


from ultralytics import YOLO

# # 加载一个预训练的 YOLO11n 模型
# yolo = YOLO(model="yolov8n.pt",task="detect")
#
# result = yolo(source="ultralytics/assets/bus.jpg")
# # result = yolo(source=0) # 通过摄像头检测


yolo = YOLO("yolov8n.pt")
yolo.train(data='yolo_cattle.yml',workers=0,epochs=1, batch=2)