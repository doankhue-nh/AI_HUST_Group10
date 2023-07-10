from ultralytics import YOLO
from PIL import Image
import cv2

model = YOLO("./weights/best.pt")

results = model.predict(source="./testset/1.jpg", show=True) # Display preds. Accepts all YOLO predict arguments