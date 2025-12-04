from PIL import Image
import torch
import io
from torchvision import transforms

# assume you have a simple classification model saved as models/disease_model.pt
MODEL_PATH = "models/disease_model.pt"
device = torch.device("cpu")
model = None

def load_model():
    global model
    if model is None:
        model = torch.load(MODEL_PATH, map_location=device)
        model.eval()

def predict_image_bytes(image_bytes: bytes):
    load_model()
    img = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    preprocess = transforms.Compose([
        transforms.Resize((224,224)),
        transforms.ToTensor(),
    ])
    tensor = preprocess(img).unsqueeze(0)
    with torch.no_grad():
        out = model(tensor)
        probs = torch.nn.functional.softmax(out, dim=1)
        conf, idx = torch.max(probs, dim=1)
    return {"label_index": int(idx.item()), "confidence": float(conf.item())}
