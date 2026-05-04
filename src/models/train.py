import torch
import torch.nn as nn
import torch.optim as optim

from src.models.model import get_model
from src.data.loader import get_dataloaders
from src.config.config import Config
from src.utils.logger import get_logger

# Init
config = Config()
logger = get_logger("train")


def train():
    logger.info("Starting training...")

    # Device
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    logger.info(f"Using device: {device}")

    # Load data
    train_loader, val_loader = get_dataloaders()

    # Load model
    model = get_model()
    model.to(device)

    # Loss + Optimizer
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=config.get("training", "lr"))

    epochs = config.get("training", "epochs")

    best_val_acc = 0.0

    for epoch in range(epochs):
        logger.info(f"Epoch [{epoch+1}/{epochs}] started")

        # -------- TRAIN --------
        model.train()
        train_loss = 0
        correct = 0
        total = 0

        for images, labels in train_loader:
            images, labels = images.to(device), labels.to(device)

            optimizer.zero_grad()

            outputs = model(images)
            loss = criterion(outputs, labels)

            loss.backward()
            optimizer.step()

            train_loss += loss.item()

            _, predicted = torch.max(outputs, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

        train_acc = 100 * correct / total

        # -------- VALIDATION --------
        model.eval()
        val_loss = 0
        correct = 0
        total = 0

        with torch.no_grad():
            for images, labels in val_loader:
                images, labels = images.to(device), labels.to(device)

                outputs = model(images)
                loss = criterion(outputs, labels)

                val_loss += loss.item()

                _, predicted = torch.max(outputs, 1)
                total += labels.size(0)
                correct += (predicted == labels).sum().item()

        val_acc = 100 * correct / total

        logger.info(
            f"Epoch [{epoch+1}] "
            f"Train Loss: {train_loss:.4f}, Train Acc: {train_acc:.2f}% | "
            f"Val Loss: {val_loss:.4f}, Val Acc: {val_acc:.2f}%"
        )

        # -------- SAVE BEST MODEL --------
        if val_acc > best_val_acc:
            best_val_acc = val_acc
            torch.save(model.state_dict(), config.get("paths", "model_path"))
            logger.info(f"Best model saved with val acc: {val_acc:.2f}%")

    logger.info("Training completed!")


if __name__ == "__main__":
    train()