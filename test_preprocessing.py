from src.data.loader import get_dataloaders
import matplotlib.pyplot as plt

# Load data
train_loader, val_loader = get_dataloaders()

# Get one batch
images, labels = next(iter(train_loader))

# Print basic info
print("Batch shape:", images.shape)
print("Labels:", labels)

# Print class names
print("Classes:", train_loader.dataset.classes)

# Convert image for display (CHW → HWC)
img = images[0].permute(1, 2, 0)

# OPTIONAL: Undo normalization for correct visualization
img = img * 0.229 + 0.485   # approximate reverse normalization

# Convert to numpy
img = img.numpy()

# Show image
plt.imshow(img)
plt.title(f"Label index: {labels[0].item()}")
plt.axis("off")
plt.show()