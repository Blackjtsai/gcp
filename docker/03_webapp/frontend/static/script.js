alert("ajax data : http://127.0.0.1:8082")
fetch('http://127.0.0.1:8082')
  .then((response) => {
    return response.json();
  })
  .then((response) => {
    alert(response.age);
  })
  .catch((error) => {
    console.log(`Error: ${error}`);
  })