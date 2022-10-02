function sendEmail(){
    Email.send({
        Host : "smtp.gmail.com",
        Username : "20ec072@jssaten.ac.in",
        Password : "Harshil@0351",
        To : 'awasthi0351@gmail.com',
        From : document.getElementById("email").value,
        Subject : "New Enquiry",
        Body : "Name: "+document.getElementById("name").value
        +"<br> Email: "+document.getElementById("email").value
        +"<br> Subject: "+document.getElementById("subject").value
        +"<br> Message: "+document.getElementById("message").value
    }).then(
      message => alert("Messege sent successfully.")
    );
}