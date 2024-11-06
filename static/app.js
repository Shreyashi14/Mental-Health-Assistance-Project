document.getElementById('userDetailsForm').addEventListener('submit', function(event) {
    event.preventDefault();  // Prevents default form submission

    // Collect form data
    const name = document.getElementById('name').value;
    const age = document.getElementById('age').value;
    const email = document.getElementById('email').value;
    const responses = [
        document.getElementById('question1').value,
        document.getElementById('question2').value,
        document.getElementById('question3').value,
        document.getElementById('question4').value,
        document.getElementById('question5').value
    ];

    const userDetails = {
        name: name,
        age: age,
        email: email
    };

    // Prepare data to send in POST request
    const postData = {
        userDetails: userDetails,
        responses: responses
    };

    // Send POST request to the server
    fetch('/analyze', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(postData)
    })
    .then(response => response.json())
    .then(data => {
        // Handle the response and display the analysis
        console.log(data);
        const report = data.report;
        const detailedAnalysis = data.detailed_analysis;

        // Display the report in a new page or section
        window.location.href = `/report?report=${encodeURIComponent(report)}&analysis=${encodeURIComponent(JSON.stringify(detailedAnalysis))}`;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
