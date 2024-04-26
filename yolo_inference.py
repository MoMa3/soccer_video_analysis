from ultralytics import YOLO

model = YOLO("yolov8m")

model.predict("input_videos/08fd33_4.mp4", save=True)