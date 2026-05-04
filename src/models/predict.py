import torch
from PIL import Image
from torchvision import transforms
import torch.nn.functional as F

from src.models.model import get_model
from src.config.config import Config
from src.data.loader import get_dataloaders   # ✅ ADD HERE

config = Config()

# transforms
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])


# ✅ ADD THIS FUNCTION HERE
def get_classes():
    train_loader, _ = get_dataloaders()
    return train_loader.dataset.classes


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def load_model():
    model = get_model()
    model.load_state_dict(torch.load(config.get("paths", "model_path"), map_location=device))
    model.to(device)
    model.eval()
    return model


def predict(image_path):
    model = load_model()
    classes = get_classes()   # ✅ USE HERE

    image = Image.open(image_path).convert("RGB")
    image = transform(image).unsqueeze(0).to(device)

    with torch.no_grad():
        

        outputs = model(image)
        probs = F.softmax(outputs, dim=1)

        confidence, predicted = torch.max(probs, 1)
        return classes[predicted.item()], confidence.item()  # ✅ RETURN NAME
def predict_multiple(image_paths):
    model = load_model()
    classes = get_classes()

    results = {}

    import torch.nn.functional as F

    for path in image_paths:
        image = Image.open(path).convert("RGB")
        image = transform(image).unsqueeze(0).to(device)

        with torch.no_grad():
            outputs = model(image)
            probs = F.softmax(outputs, dim=1)

            confidence, predicted = torch.max(probs, 1)

        label = classes[predicted.item()]
        conf = confidence.item()

        if label not in results:
            results[label] = []

        results[label].append(conf)

    # Voting logic
    final_label = None
    max_score = 0

    for label, confs in results.items():
        avg_conf = sum(confs) / len(confs)

        if avg_conf > max_score:
            max_score = avg_conf
            final_label = label

    return final_label, max_score