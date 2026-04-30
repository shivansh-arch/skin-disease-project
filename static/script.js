document.addEventListener('DOMContentLoaded', () => {
    const uploadForm = document.getElementById('uploadForm');
    const fileInput = document.getElementById('fileInput');
    const dropZone = document.getElementById('dropZone');
    const previewContainer = document.getElementById('previewContainer');
    const analyzeBtn = document.getElementById('analyzeBtn');
    const loadingIndicator = document.getElementById('loadingIndicator');
    const resultContainer = document.getElementById('resultContainer');
    const predictionText = document.getElementById('predictionText');
    const confidenceBar = document.getElementById('confidenceBar');
    const confidenceText = document.getElementById('confidenceText');
    
    let selectedFiles = [];

    // Drag and Drop handlers
    ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
        dropZone.addEventListener(eventName, preventDefaults, false);
    });

    function preventDefaults(e) {
        e.preventDefault();
        e.stopPropagation();
    }

    ['dragenter', 'dragover'].forEach(eventName => {
        dropZone.addEventListener(eventName, () => {
            dropZone.classList.add('drag-over');
        }, false);
    });

    ['dragleave', 'drop'].forEach(eventName => {
        dropZone.addEventListener(eventName, () => {
            dropZone.classList.remove('drag-over');
        }, false);
    });

    dropZone.addEventListener('drop', (e) => {
        const dt = e.dataTransfer;
        const files = dt.files;
        handleFiles(files);
        // Sync files with input
        fileInput.files = files;
    });

    fileInput.addEventListener('change', (e) => {
        handleFiles(e.target.files);
    });

    function handleFiles(files) {
        selectedFiles = [...files];
        updatePreview();
        analyzeBtn.disabled = selectedFiles.length === 0;
        resultContainer.classList.add('hidden');
    }

    function updatePreview() {
        previewContainer.innerHTML = '';
        selectedFiles.forEach(file => {
            if (file.type.startsWith('image/')) {
                const reader = new FileReader();
                reader.onload = (e) => {
                    const div = document.createElement('div');
                    div.className = 'preview-item';
                    const img = document.createElement('img');
                    img.src = e.target.result;
                    div.appendChild(img);
                    previewContainer.appendChild(div);
                };
                reader.readAsDataURL(file);
            }
        });
    }

    uploadForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        if (selectedFiles.length === 0) return;

        // UI state changes
        analyzeBtn.disabled = true;
        resultContainer.classList.add('hidden');
        loadingIndicator.classList.remove('hidden');

        // Existing error message cleanup
        const oldError = document.querySelector('.error-message');
        if (oldError) oldError.remove();

        const formData = new FormData();
        selectedFiles.forEach(file => {
            formData.append('files[]', file);
        });

        try {
            const response = await fetch('/predict', {
                method: 'POST',
                body: formData
            });

            const data = await response.json();

            if (!response.ok) {
                throw new Error(data.error || 'Prediction failed');
            }

            // Update UI with results
            predictionText.textContent = data.prediction.replace(/_/g, ' ').toUpperCase();
            
            // Animation reset for confidence bar
            confidenceBar.style.width = '0%';
            setTimeout(() => {
                confidenceBar.style.width = `${data.confidence}%`;
            }, 100);
            
            confidenceText.textContent = `${data.confidence}%`;
            
            // Reveal result
            loadingIndicator.classList.add('hidden');
            resultContainer.classList.remove('hidden');

        } catch (error) {
            loadingIndicator.classList.add('hidden');
            const errorDiv = document.createElement('div');
            errorDiv.className = 'error-message';
            errorDiv.textContent = `Error: ${error.message}`;
            uploadForm.parentNode.insertBefore(errorDiv, resultContainer);
        } finally {
            analyzeBtn.disabled = false;
        }
    });
});
