pip install ultralytics

git clone https://github.com/ultralytics/yolov5
cd yolov5
pip install -r requirements.txt

Запуск обучения

yolo detect train data=data.yaml model=yolov8n.pt epochs=100 imgsz=640