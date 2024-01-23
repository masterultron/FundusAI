//<!-- IMAGE QUALITY CHECK: AJAX script for hiding Make Diagnosis Button -->
$(document).ready(function () {
// Event listener for the file input change
$('#camera-input, #upload-input').on('change', function () {
    const fileInput = this;
    const tickIcon = document.getElementById('green-tick');
    const xIcon = document.getElementById('x-icon');

    // Check if a file is selected
    if (fileInput.files.length > 0) {
    const file = fileInput.files[0];
    const formData = new FormData();

    // Append the image to the FormData object
    formData.append('image', file);

    // Perform AJAX request to check image quality
    $.ajax({
        url: "{% url 'check_image_quality' %}",  // Replace with your actual URL
        type: "POST",
        data: formData,
        processData: false,
        contentType: false,
        success: function (data) {
        // If quality is not high, disable the Make Diagnosis button
        if (!data.is_high_quality) {
            $('#makeDiagnosisButton').prop('disabled', true);
            tickIcon.style.display = 'none';
            xIcon.style.display = 'flex';
            alert('Image quality is not high enough for diagnosis.');
        } else {
            // If quality is high, enable the Make Diagnosis button
            $('#makeDiagnosisButton').prop('disabled', false);
            tickIcon.style.display = 'flex';
            xIcon.style.display = 'none';
        }
        },
        error: function (error) {
        console.error('Error checking image quality:', error);
        }
    });
    }
});
});


//<!-- IS RETINOPATHY PRESENT: AJAX script for making diagnosis -->
$(document).ready(function () {
// Event listener for the Make Diagnosis button click
$('#makeDiagnosisButton').on('click', function () {
    // Hide the white sidebar and buttons-container
    $('.white-sidebar, #buttons-container, #makeDiagnosisHeader').css('display', 'none');
    // Show the retinopathy status and patientInfoCard
    $('#retinopathy-status, #patientInfoCard, #severity-button-container').css('display', 'block');

    // Get the button and image-preview-card elements
    var imagePreviewCard = document.querySelector('.image-preview-card');

    imagePreviewCard.style.width = '400px';
    imagePreviewCard.style.marginLeft = 'auto';
    imagePreviewCard.style.padding = '50px';

    // Get the uploaded image file
    const fileInput = document.getElementById('upload-input');
    const uploadedImage = fileInput.files[0];

    // Create FormData and append the image
    const formData = new FormData();
    formData.append('image', uploadedImage);

    // Perform AJAX request to check if retinopathy is present
    $.ajax({
    url: "{% url 'is_retinopathy_present' %}",  // Replace with your actual URL
    type: "POST",
    data: formData,
    processData: false,
    contentType: false,
    success: function (data) {
        // Get the status span element
        const statusSpan = $('#status');

        // Set the text and color based on the response
        if (data.is_retinopathy_present) {
        statusSpan.text('Found').css('color', 'red');
        $('#severityButton').prop('disabled', false);
        } else {
        statusSpan.text('Absent').css('color', 'green');
        $('#severityButton').prop('disabled', true);
        }
    },
    error: function (error) {
        console.error('Error checking retinopathy:', error);
    }
    });
});
});
        

//<!-- CHECK SEVERITY: AJAX script for checking severity level -->
$(document).ready(function () {
// Event listener for the Check Severity button click
$('#severityButton').on('click', function () {
    // Hide unnecessary elements
    $('#retinopathy-status, #severity-button-container').css('display', 'none');
    // Show the severity results and button container
    $('#result-button-container, .result-text').css('display', 'block');

    // Get the uploaded image file
    const fileInput = document.getElementById('upload-input');
    const uploadedImage = fileInput.files[0];

    // Create FormData and append the image
    const formData = new FormData();
    formData.append('image', uploadedImage);

    // Perform AJAX request to check severity level
    $.ajax({
    url: "{% url 'severity_level' %}",  // Replace with your actual URL
    type: "POST",
    data: formData,
    processData: false,
    contentType: false,
    success: function (data) {
        // Update the result and recommendation paragraphs
        $('#result').text('Result: ' + data.result[0]);
        $('#recommendation').text(data.result[1]);
    },
    error: function (error) {
        console.error('Error checking severity level:', error);
    }
    });
});
});
