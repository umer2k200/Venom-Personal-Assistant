# Venom - Personal Assistant

Venom is a voice-controlled personal assistant designed to execute various system tasks, interact with web applications, and manage day-to-day operations efficiently. The assistant leverages AI capabilities and a modular design to ensure extensibility and customization.

## Features

- **Voice Authentication:** Secures access with passphrase-based voice authentication.
- **AI Integration:** Provides answers to queries using OpenAI's GPT-3.5 Turbo API.
- **System Automation:** Manages volume, brightness, system state, and folder access.
- **Web Interaction:** Automates browser operations, including website navigation and searches.
- **Task Management:** Includes features for opening/closing applications, checking the weather, and more.
- **Utility Tools:** Takes screenshots, opens resumes, and announces the current time.

## Project Structure

```
Venom - Personal Assistant
|
├── core/
│   ├── execute_command.py  # Handles command execution.
│   ├── launcher.py         # Entry point for launching the assistant.
│   └── voice.py            # Contains voice input/output logic.
|
├── tasks/
│   ├── .env                # Configuration file with environment variables.
│   ├── ai.py               # Handles AI-based responses.
│   ├── authentication.py   # Implements voice-based authentication.
│   ├── service.py          # Opens and closes system services.
│   ├── system.py           # Manages system state and hardware control.
│   ├── system_initiate.py  # Initiates custom system workflows.
│   ├── utility.py          # Utility functions like weather, time, screenshots.
│   └── web.py              # Web interaction using browsers and automation.
|
├── launch/
│   ├── main.bat            # Batch file for launching the assistant.
│   └── main.vbs            # VBScript file for executing the assistant.
|
├── main.py                 # Main script for initializing the assistant.
├── requirements.txt        # Python dependencies.
```

## Prerequisites

Ensure the following are installed on your system:

1. Python 3.9+
2. Required Python modules (specified in `requirements.txt`).
3. Google Chrome and Chromedriver (path configured in `.env`).

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/username/venom.git
   cd venom
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Configure the `.env` file:

   - Update paths and credentials to match your system configuration.

## Usage

1. Run the main script:

   ```bash
   python main.py
   ```

2. Follow the voice prompts for authentication and task execution.

## Environment Variables

The `.env` file contains the following configuration variables:
Place this file inside the tasks directory

```env
ROLL_NUMBER=your_roll_bumber
FLEX_PASSWORD=your_password
OPEN_AI_API_KEY=your_openai_api_key
CHROME_DRIVER=path_to_chromedriver
GITHUB=your_github_url
VSCODE=path_to_vscode
CHROME=path_to_chrome
DOWNLOADS_FOLDER=path_to_downloads
OFFICE_WORK_FOLDER=path_to_office_work
PROJECTS_FOLDER=path_to_projects
VENOM_FOLDER=path_to_venom
UNIVERSITY_FOLDER=path_to_university
RESUME=path_to_resume
SCREENSHOT=path_to_screenshots
CODE=venom here
CODE2=why do we fall
CODE3=you are not brave
```

## Core Functionalities

### Voice Authentication

- **Script:** `authentication.py`
- **Description:** Ensures secure access with three chances to provide the correct voice passphrase.

### AI-Powered Responses

- **Script:** `ai.py`
- **Description:** Integrates OpenAI's GPT-3.5 Turbo for natural language interaction.

### System Operations

- **Scripts:** `system.py`, `system_initiate.py`
- **Description:** Handles shutdown, restart, sleep, volume, brightness, and folder access.

### Web Automation

- **Script:** `web.py`
- **Description:** Automates web browsing and searches using Selenium and the webbrowser module.

### Utility Tools

- **Script:** `utility.py`
- **Description:** Provides tools like time announcements, weather updates, screenshots, and resume access.

### Command Execution

- **Script:** `execute_command.py`
- **Description:** Dynamically routes commands to appropriate functions based on voice input.

## Launching Options

- **Batch File:** Use `main.bat` for launching Venom in Windows. 

- **VBScript:** Use `main.vbs` for alternative Windows execution.

  You can place the main.vbs file inside the startup folder. You can do this by pressing: 

  Windows + R and type: 

  ```
  shell:startup
  ```

- Now, you can place the main.vbs file inside this folder. 

- After doing that, everytime you start your PC, the program is launched and ready to listen. 

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch.
3. Make your changes and submit a pull request.

## License

This project is licensed under the MIT License. See `LICENSE` for details.

## Acknowledgments

Special thanks to:

- OpenAI for GPT-3.5 Turbo.
- Python community for libraries and support.

---

Happy Coding!

