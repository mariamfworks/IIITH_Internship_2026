from ultralytics import YOLO

model = YOLO("yolo11n-seg.pt")
model.predict(source="../week 1/frames1_30fps", save=True)
