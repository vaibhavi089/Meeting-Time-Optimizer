Project Overview
Meeting Time Optimizer is a simple web application designed to help teams identify the optimal meeting time based on individual availabilities. Users input their time slots in a 24-hour format, and the application calculates the best overlap.

Features
User-friendly interface for inputting availabilities.
Real-time communication with a backend API to compute the optimal meeting time.
Clear visual presentation of the result.
How to Use
Input Availability:

Enter each participant's availability in the text area in the format HH:MM-HH:MM.
Each availability should be on a new line.
Example:

makefile
Copy code
09:00-12:00
10:00-11:00
13:00-14:00
Submit Form:

Click the Find Optimal Time button to submit the availabilities.
View Results:

The application will display the optimal meeting time or an error message if no suitable time is found.
Technical Details
Frontend
HTML: Provides the structure and layout for the application.
CSS: Styles the form and buttons for a clean, modern appearance.
JavaScript: Handles user input, form submission, and communication with the backend API.
Backend API (Expected Endpoint)
URL: http://127.0.0.1:5000/api/optimal_time
Method: POST
Request Payload:
json
Copy code
{
    "availabilities": [
        {"start": "09:00", "end": "12:00"},
        {"start": "10:00", "end": "11:00"}
    ]
}
Response:
Success:
json
Copy code
{
    "optimal_time": "10:00-11:00"
}
Error:
json
Copy code
{
    "error": "No overlapping time found."
}
Local Testing
Set up a backend service at the specified endpoint (http://127.0.0.1:5000/api/optimal_time).
Serve the HTML file locally using a web server (e.g., Python's http.server module).
Access the application via a browser.
Dependencies
A running backend service capable of processing the POST request and calculating the optimal time.
Modern web browser for running the frontend.
Customization
API URL: Update the API endpoint in the fetch function if your backend is hosted at a different address.
Styling: Modify the CSS within the <style> tag to customize the appearance.
Troubleshooting
Error: Could not calculate optimal time:

Ensure the backend API is running and accessible.
Verify the format of input availability.
No Optimal Time Found:

Check if there are overlapping availabilities between participants.
Future Improvements
Add client-side validation for input format.
Allow users to upload availability files.
Support multiple time zones.
License
This project is licensed under the MIT License.











