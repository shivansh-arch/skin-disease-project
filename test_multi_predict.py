from src.models.predict import predict_multiple

images = [
    "your_image.jpg",
    "your_image.jpg",
    "your_image.jpg"
]

label, conf = predict_multiple(images)

print(f"Final Prediction: {label} ({conf*100:.2f}%)")