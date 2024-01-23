/*  JavaScript for File Input Handling and Drag-and-Drop
    DEBUG: Accept only image files, drag and drop function, proper file uploads */

// Function to trigger file input click
function triggerFileInput(inputId) {
  document.getElementById(inputId).click();
}

// // Event listener for camera icon click
// document.getElementById('camera-input').addEventListener('change', function () {
//   // Handle selected file (you can add your logic here)
//   const selectedFile = this.files[0];
//   console.log('Selected file:', selectedFile);
// });

// Event listener for upload icon click
document.getElementById('upload-input').addEventListener('input', function () {
  // Handle selected file (you can add your logic here)
  const selectedFile = this.files[0];
  console.log('Selected file:', selectedFile);
});

// Function to handle dragover event
function handleDragOver(event) {
  event.preventDefault();
  event.dataTransfer.dropEffect = 'copy';
}

// Function to handle drop event
function handleDrop(event) {
  event.preventDefault();
  const files = event.dataTransfer.files;

  // Check if any files are dropped
  if (files.length > 0) {
    
    // Log the MIME type of the dropped file
    console.log('Dropped file MIME type:', files[0].type);

    // Check if the dropped file is an image
    if (files[0].type.startsWith('image/')) {
      // Handle the dropped image file (you can add your logic here)
      console.log('Dropped image file:', files[0]);
      document.getElementById('upload-input').files = files
    } else {
      alert('Please drop only image files.');
    }
  }
}

