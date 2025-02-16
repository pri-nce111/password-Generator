# password-Generator
# Password Generator and Manager

A secure password generator and manager built with Python and Streamlit. This application allows users to generate strong passwords with customizable criteria and save them for future reference.

## Features

- Generate secure passwords with customizable options:
  - Adjustable password length
  - Include/exclude letters, numbers, and special characters
  - Visual feedback for generated passwords
- Save passwords with associated information:
  - Username
  - Website/Application name
  - Creation timestamp
- View all saved passwords in an organized interface
- Simple and intuitive user interface

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/password-manager.git
cd password-manager
```

2. Install the required dependencies:
```bash
pip install streamlit
```

## Usage

1. Run the application:
```bash
streamlit run app.py
```

2. The application will open in your default web browser.

3. To generate a password:
   - Use the sidebar to customize password options
   - Click "Generate Password"
   - Fill in the username and website details
   - Click "Save Password" to store it

4. To view saved passwords:
   - Click the "View Saved Passwords" tab
   - Click on any entry to view the details

## Security Considerations

- Passwords are stored locally in a JSON file
- For enhanced security, consider:
  - Implementing encryption for stored passwords
  - Adding user authentication
  - Using a secure database instead of JSON file storage

## Project Structure

```
password-manager/
├── app.py
├── passwords.json
└── README.md
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

