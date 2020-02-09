from app import app
from flask import jsonify, request
import io
import os
import json
import torch
import torch.nn as nn
from torchvision import models
import torchvision.transforms as transforms
from PIL import Image

model = torch.hub.load('pytorch/vision:v0.4.2', 'googlenet', pretrained=True)
model.eval()
model.load_state_dict(torch.load(os.path.join(app.root_path, "model/", "aslPaper1Model.pth")))

img_indexer = json.load(open(os.path.join(app.root_path, "static/", "comparator.json")))

#The Following Code is Modeled Off: https://pytorch.org/tutorials/intermediate/flask_rest_api_tutorial.html
def transform(image_bytes):
    data_transform = transforms.Compose([
        transforms.Resize((256, 256)),
        transforms.RandomCrop((224,224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                             std=[0.229, 0.223, 0.225])
    ])
    image = Image.open(io.BytesIO(image_bytes))
    return data_transform(image).unsqueeze(0)

def get_prediction(image_bytes):
    tensor = transform(image_bytes=image_bytes)
    output = model(tensor)
    _, batch = output.max(1)
    predicted_idx = str(batch.item())
    return img_indexer[predicted_idx]


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        image = request.files['image']
        img_bytes = image.read()
        class_name = get_prediction(image_bytes=img_bytes)
        return jsonify({'class_name': class_name})

