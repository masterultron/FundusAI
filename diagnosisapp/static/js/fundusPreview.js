// Function to handle file upload
function handleImageUpload(event) {
    const fileInput = event.target;

    // Check if a file is selected
    if (fileInput.files.length > 0) {
        const uploadedImage = document.getElementById('uploaded-image');
        const imagePreviewCard = document.getElementById('image-preview-card');
        const uploadCards = document.querySelector('.upload-cards');
        const graphContainer = document.querySelector('.analytics-container');
        const buttonsContainer = document.getElementById('buttons-container');

        // Display the uploaded image
        const file = fileInput.files[0];
        const reader = new FileReader();
        reader.onload = function(e) {
        uploadedImage.src = e.target.result;
        };
        reader.readAsDataURL(file);

        // Toggle visibility of upload cards, image preview card, graph container, and buttons container
        uploadCards.style.display = 'none';
        imagePreviewCard.style.display = 'flex';
        graphContainer.style.display = 'none';
        buttonsContainer.style.display = 'flex';
}
}

// Function to handle retake button click
function handleRetakeButtonClick() {
    // Reset the uploaded image and hide stage components
    var testResult = document.getElementById('testResult');
    var resultText = document.getElementById('resultText');
    var retinopathyStatus = document.getElementById('retinopathy-status');
    var patientInfoCard = document.getElementById('patientInfoCard');
    var imagePreviewCard = document.getElementById('image-preview-card');
    var makeDiagnosisHeader = document.getElementById('makeDiagnosisHeader');
    var uploadedImage = document.getElementById('uploaded-image');
    var buttonContainer = document.getElementById('buttons-container');
    var DiagnosisButtonContainer = document.getElementById('severity-button-container');
    var resultButtonContainer = document.getElementById('result-button-container');
    
    if (testResult) {
        testResult.style.display = 'none';
    }
    if (resultText) {
        resultText.style.display = 'none';
    }
    if (retinopathyStatus) {
        retinopathyStatus.style.display = 'none';
    }
    if (patientInfoCard) {
        patientInfoCard.style.display = 'none';
    }
    if (imagePreviewCard) {
        imagePreviewCard.style.display = 'none';
    }
    if (uploadedImage) {
        uploadedImage.src = '';
    }

    // Show the upload cards, "Make Diagnosis" and graph container then restore original imagePreviewCard dimensions
    document.querySelector('.upload-cards').style.display = 'flex';
    document.querySelector('.analytics-container').style.display = 'block';
    makeDiagnosisHeader.style.display = 'block';
    imagePreviewCard.style.width = '600px';
    imagePreviewCard.style.marginLeft = '180px';
    imagePreviewCard.style.padding = '80px';

    // Hide the buttons container
    if (buttonContainer) {
        buttonContainer.style.display = 'none';    
    }
    if (DiagnosisButtonContainer) {
        DiagnosisButtonContainer.style.display = 'none';    
    }
    if (resultButtonContainer) {
        resultButtonContainer.style.display = 'none';    
    }

    // Reset the file input to allow selecting a new image
    // document.getElementById('camera-input').value = '';
    document.getElementById('upload-input').value = '';
}


// Event listener for retake button click
document.getElementById('retakeButton').addEventListener('click', handleRetakeButtonClick);

// Event listener for retake Diagnosis button click
document.getElementById('retakeDiagnosisButton').addEventListener('click', handleRetakeButtonClick);

// Event listener for retake Test button click
document.getElementById('retakeTestButton').addEventListener('click', handleRetakeButtonClick);

// Event listener for camera icon click
// document.getElementById('camera-input').addEventListener('change', handleImageUpload);

// Event listener for upload icon click
document.getElementById('upload-input').addEventListener('change', handleImageUpload);