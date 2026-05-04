# 🧴 Skin Disease Classification using Deep Learning

> A scalable, deep learning-based web application for automated skin disease classification.

## 📝 Project Overview

Early and accurate detection of skin diseases is critical for effective treatment and patient care. This project presents a comprehensive deep learning-based system designed to classify skin lesions from digital images.

Built using a **Convolutional Neural Network (EfficientNet-B0)** and a dual-backend architecture (Flask for the user interface, FastAPI for the REST API), the system offers robust, real-time predictions. To account for difficult lighting or blurry photos, the architecture includes a **Multi-Image Voting Logic** that processes multiple images of the same lesion simultaneously and aggregates the confidence scores to provide a highly accurate final prediction.

### 🎯 Key Features
* **Deep Feature Extraction:** Utilizes transfer learning with pre-trained ImageNet weights on EfficientNet-B0.
* **Dual Backend System:** Features a user-friendly web interface (Flask) and a high-performance REST API (FastAPI).
* **Multi-Image Voting Logic:** Upload multiple angles of the same skin lesion, and the system will average the confidence scores to provide the most reliable prediction.
* **Automated Data Preprocessing:** Real-time image resizing (224x224) and tensor normalization.

---

## 📂 Dataset Categorization

For this Minimum Viable Product (MVP), the model has been optimized and trained to classify **6 primary distinct classes** of skin conditions to ensure computational efficiency and high inference speed:

1. **Lichen**
2. **Lupus**
3. **Moles** (Benign Tumors)
4. **Psoriasis**
5. **Rosacea**
6. **Seborrheic Keratoses**

*(Note: The architecture is fully scalable and can be trained on up to 22+ classes if additional GPU resources and full datasets are provided).*

---

## ⚙️ Tech Stack

* **Language:** Python 3.10+
* **Deep Learning Framework:** PyTorch & Torchvision
* **Web Frameworks:** Flask (UI), FastAPI (REST API)
* **Image Processing:** PIL (Pillow), OpenCV
* **Data Manipulation:** NumPy, Pandas

---

## 🚀 How to Download and Run the Project

Follow these steps to run the web application locally on your machine.

### 1. Clone the Repository
Open your terminal and clone the repository:
```bash
git clone https://github.com/shivansh-arch/skin-disease-project.git
cd skin-disease-project
```

### 2. Set Up a Virtual Environment
It is highly recommended to use a virtual environment to manage dependencies.
```bash
# Create the virtual environment
python -m venv venv

# Activate it (Windows)
venv\Scripts\activate

# Activate it (Mac/Linux)
source venv/bin/activate
```

### 3. Install Dependencies
Install all required Python packages from the requirements file:
```bash
pip install -r requirements.txt
```

### 4. Run the Web Interface (Flask)
Start the user-friendly web application:
```bash
python flask_app.py
```
* Once the server starts, open your web browser and navigate to: **http://127.0.0.1:5000**
* Click "Upload" to select an image (or multiple images) and get a real-time prediction!

### 5. (Optional) Run the REST API (FastAPI)
If you want to test the developer API endpoints:
```bash
uvicorn app.main:app --reload
```
* Navigate to **http://127.0.0.1:8000/docs** to view the Swagger UI and test the API endpoints directly.

---

## 📁 Directory Structure

```plaintext
SkinDiseaseProject/
│
├── app/                  # FastAPI backend routes and logic
├── configs/              # Configuration files (e.g., config.yaml)
├── data/                 # Raw and processed image datasets
├── models/               # Saved PyTorch models (.pt files)
├── src/
│   ├── data/             # Data preprocessing scripts
│   ├── models/           # Model architecture, training, and evaluation scripts
│   └── utils/            # Helper functions and loggers
│
├── templates/            # HTML files for the Flask frontend
├── flask_app.py          # Main Flask web application
├── requirements.txt      # Python dependencies
└── Readme.md             # Project documentation
```
