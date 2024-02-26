// Select the file input element
const fileInput = document.querySelector('#fileInput');

// Create a paragraph element to display the response
const responseParagraph = document.createElement('p');
document.body.appendChild(responseParagraph);

// Listen for changes on the file input element
fileInput.addEventListener('change', (event) => {
  // Get the selected file
  const file = event.target.files[0];

  // Create a new FormData object
  const formData = new FormData();

  // Append the file to the FormData object
  formData.append('file', file);
  formData.append('language', 'pol'); // or any other language you want to set

  // Send a POST request to the endpoint
  fetch('http://127.0.0.1:8000/upload', {
    method: 'POST',
    body: formData
  })
    .then(response => response.json())
    .then(data => {
      // Display the response on the screen
      responseParagraph.innerText = data.text;
    })
    .catch(error => console.error(error));
});
