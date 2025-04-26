# KeyLogger

A Python-based keylogging tool that captures keyboard input, takes screenshots, and logs clipboard content. This tool is designed for educational purposes only to demonstrate how keyloggers work and should not be used maliciously.

## Features

- **Keylogging**: Records every keystroke made on the system.
- **Clipboard Logging**: Logs the content copied to the clipboard.
- **Screenshot Capture**: Takes screenshots when the Enter key is pressed.
- **Cross-platform**: Works on Windows, Linux, and macOS.

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/aaryanshlok0/KeyLogger.git
    ```

2. Navigate to the project directory:
    ```bash
    cd KeyLogger
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the script**: Simply run the main script:
    ```bash
    python keylogger.py
    ```

2. **Log Files**:
    - `key_log.txt`: Logs keystrokes with timestamps.
    - `clipboard_log.txt`: Logs copied clipboard content.
    - Screenshots are saved in the `screenshots/` folder.

## Warning

This project is intended for educational purposes only. Unauthorized use of keyloggers and other malicious tools is illegal and unethical. Always ensure you have explicit consent before running such tools.

## License

This project is open-source and available under the [MIT License](LICENSE).
