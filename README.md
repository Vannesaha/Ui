---

# Project Title

## Overview
Briefly describe the project, its functionality, and what it aims to achieve. Mention the technologies used (Python, QML, MQTT).

## Getting Started
Instructions for initial setup and running the project.

### Prerequisites
List the necessary prerequisites to run the application.

### Installation
Step-by-step guide for installing the application.

## Project Structure
Explanation of the main directories and files in the project.

### `UI/`
General overview of what the `UI` directory contains and its role in the project.

#### `config/`
- `settings.py`: Describe the configuration settings that can be modified.

#### `src/`
- General description of the source code.

#### `ui/`
- Detailed description of each QML UI component.
  - `control_menu/`
    - `control_menu.py`: Explain the backend logic for this menu.
    - `control_menu.qml`: Explain the UI layout and elements for the control menu.
  - `hydraulic_menu/`
    - `hydraulic_menu.py`: Backend logic for the hydraulic menu.
    - `hydraulic_menu.qml`: UI layout for the hydraulic menu.
  - `start_menu/`
    - `start_menu.py`: Describe what happens on application start.
    - `start_menu.qml`: UI elements for the starting menu.

### `utils/`
- `device_status.py`: Explain how device status is managed. (not in use att the moment)
- `mqtt_publisher.py`: Outline the responsibilities of handling MQTT messaging.

### `main.py`
Describe the entry point of the application.

### `maincontroller.py`
Discuss the role of this file in the overall application.

### `.gitignore`
List the kinds of files that are intentionally untracked.

### `requirements.txt`
Discuss how to use this file to install dependencies.

## Usage
Instructions on how the end-user should use the application, including navigation through different menus and executing core functions.

## Contributing
Guidelines for how to contribute to the project, including coding standards, pull request process, etc.



---
