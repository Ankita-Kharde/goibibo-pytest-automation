Goibibo Flight Booking Automation - Test Suite
This project automates the end-to-end flight booking process on the Goibibo platform using **Python**, **Pytest**, and **Selenium WebDriver**.

Key Test Scenarios Covered
Launch Application
- Open the **Goibibo** website
- Verify the homepage is loaded and the **flight booking section** is visible

🔍 Select Flight Search Criteria
- Enter source and destination cities
- Select departure and return dates via the **date picker**
- Specify the number of travelers

🔎 Execute Search
- Click on the **Search** button
- Wait for the **flight results** page to load completely

🎯 Apply Filters
- **One-stop filter**: Select to view only one-stop flights
- **Airline filter**: Choose specific airlines (e.g., Indigo, Air India)
- Validate that the flight list is updated according to the applied filters

📋 Flight List Validation
- Ensure that the displayed flights match the selected filters
- Capture and log flight details such as:
  - Flight name
  - Departure and arrival time
  - Price and duration

---

Tools & Technologies Used

- **Python** with **Pytest** for writing and executing test cases
- **Selenium WebDriver** for automating browser interactions
- **ChromeDriver** for communication with the Chrome browser
- **Pytest Fixtures** for structured setup and teardown
- **Custom Utility Functions** for:
  - Interacting with the date picker
  - Validating filter selections
  - Extracting flight data dynamically
