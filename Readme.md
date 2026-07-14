# 🩺 Skin Disease Classification using Deep Learning

> **An end-to-end AI-powered skin disease classification system built with PyTorch, EfficientNet-B0, Flask, and FastAPI.**

This project leverages **transfer learning** with **EfficientNet-B0** to automatically classify skin diseases from clinical images. Alongside the trained deep learning model, the project provides both a **Flask web application** for end users and a **FastAPI REST API** for integration into other applications.

To improve prediction reliability, the system also supports **Multi-Image Voting**, allowing multiple photos of the same lesion to be analyzed together before producing a final prediction.

---

# 🚀 Features

* 🧠 EfficientNet-B0 based image classifier
* 📷 Single-image prediction
* 🖼️ Multi-image voting for improved robustness
* 🌐 Flask web interface
* ⚡ FastAPI REST API
* 📊 Confidence score prediction
* 🔄 Automated image preprocessing
* 🧩 Modular training pipeline
* 📁 Config-driven project structure

---

# 🏗️ System Architecture

```text
Input Skin Image(s)
        │
        ▼
Image Preprocessing
(Resize • Normalize)
        │
        ▼
EfficientNet-B0
(Transfer Learning)
        │
        ▼
Softmax Probabilities
        │
        ▼
Multi-Image Voting
(Optional)
        │
        ▼
Final Disease Prediction
        │
        ▼
Flask UI / FastAPI API
```

---

# 📂 Project Structure

```text
skin-disease-project/

├── app/
│   ├── main.py
│   ├── routes.py
│   └── schemas.py
│
├── configs/
│   └── config.yaml
│
├── models/
│   └── trained_model.pt
│
├── src/
│   ├── config/
│   ├── data/
│   ├── interface/
│   ├── models/
│   └── utils/
│
├── templates/
├── static/
├── flask_app.py
├── requirements.txt
└── README.md
```

---

# 🧠 Model

The classifier is built using **EfficientNet-B0**, a lightweight convolutional neural network that provides an excellent balance between accuracy and computational efficiency.

The model is fine-tuned using transfer learning on a curated skin disease dataset.

---

# 📊 Supported Classes

Current implementation predicts:

* Lichen
* Lupus
* Moles (Benign)
* Psoriasis
* Rosacea
* Seborrheic Keratosis

The architecture can easily be extended to additional disease categories by retraining the model.

---

# 🛠️ Tech Stack

### Machine Learning

* PyTorch
* Torchvision
* EfficientNet-B0

### Backend

* FastAPI
* Flask

### Image Processing

* Pillow
* OpenCV
* NumPy

### Utilities

* Pandas
* YAML

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/shivansh-arch/skin-disease-project.git
cd skin-disease-project
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Flask Application

```bash
python flask_app.py
```

Open

```text
http://127.0.0.1:5000
```

---

# ⚡ Run FastAPI

```bash
uvicorn app.main:app --reload
```

Swagger documentation

```text
http://127.0.0.1:8000/docs
```

---

# 🔄 Multi-Image Voting

Instead of predicting from only one image, the system can process multiple images of the same lesion.

Workflow:

1. Upload multiple images
2. Predict each image individually
3. Average confidence scores
4. Return the highest-confidence disease

This approach improves robustness when images suffer from poor lighting, blur, or different viewing angles.

---

# 📸 Screenshots

Add screenshots here.

* Home Page
* Upload Screen
* Prediction Result
* Multi-image Upload
* API Swagger

---

# 📈 Future Improvements

* Mobile application
* Docker deployment
* ONNX model export
* Model quantization
* Grad-CAM visualization
* Explainable AI (XAI)
* Additional disease categories
* Cloud deployment
* User authentication
* Patient history management

---

# ⚠️ Limitations

* Educational project
* Predicts only supported disease classes
* Does not replace professional medical diagnosis
* Performance depends on image quality

---

# 🎯 Learning Outcomes

This project demonstrates:

* Deep Learning for Medical Imaging
* Transfer Learning
* CNN-based Image Classification
* REST API Development
* Flask Web Development
* FastAPI Integration
* Image Preprocessing
* Model Deployment

---

# 👨‍💻 Author

**Shivansh Gupta**

Computer Science Student | Machine Learning & AI Enthusiast

GitHub: https://github.com/shivansh-arch

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
