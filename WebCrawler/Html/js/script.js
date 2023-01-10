$(document).ready(() => {
  // Adding 'click' event listener to button
  $("#btn").click(() => {
    // Fetching key's input field data
    const key = $("#key").val();
  
    // Fetching values input field data
    const value = $("#value").val();
  
    // Initializing array of objects to 
    // store key-value pairs
    
    let data = {};
  
    // assigning key-value pair to data object
    data[key] = value;
  
    // jQuery Ajax Post Request
    $.post(
      "Php/shellExec.php",
      {
        data,
      },
      (response) => {
        // response from PHP back-end
        alert(`Response from sever side is: ${response}`);
      }
    );
  });
});