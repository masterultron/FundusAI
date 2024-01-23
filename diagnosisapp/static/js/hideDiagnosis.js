// AJAX script for hiding Make Diagnosis Button
    
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
