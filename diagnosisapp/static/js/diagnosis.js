document.addEventListener('DOMContentLoaded', function () {
  var imageInput = document.getElementById('img');
  var submitButton = document.getElementById('submitButton');

  imageInput.addEventListener('change', function () {
    // Check if an image is selected
    if (imageInput.files.length > 0) {
      submitButton.removeAttribute('disabled');
    } else {
      submitButton.setAttribute('disabled', 'disabled');
    }
  });

  // You can also add additional logic for form submission
  document.getElementById('uploadForm').addEventListener('submit', function (event) {
    event.preventDefault();
    alert('Form submitted!');
    // Add your form submission logic here
  });
});