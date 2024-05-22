# Vannesaha Ui

## Overview

The program currently features three example menus and the ability to view device updates. The screen size adjusts automatically based on the display, and the frames scale according to the content. The layout has been tested on a Raspberry Pi computer and may differ on other platforms. An MQTT connection is needed at the start of the program or program may not start.

## Table of Contents

1. [Overview] (##Overviev)

## Getting Started

To set up and run the project, follow these steps:

### Prerequisites

- Python3
- PIP3 package management system
- MQTT broker server (e.g., Mosquitto)

### Installation

- Check that the requirements.txt file contains all necessary dependencies.
- Install the packages using the command: pip3 install -r requirements.txt.
- Ensure Python3 and pip3 package management system are already installed.

## Project Structure

Explanation of the main directories and files in the project.

### `UI/`

General overview of what the `UI` directory contains and its role in the project.

### `assets/`

Not in use but includes images for menus if they are needed.

#### `config/`

- `settings.py`: Contains configuration variables required for the application.

#### `src/`

- General description of the source code.

#### `frames/`

- Detailed description of each UI frame component.
  - `info_frame.py`: Handles the construction of the info frame.
  - `main_frame.py`: Handles the construction of the main frame.
  - `menu_frame.py`: Handles the construction of the menu frame.
  - `status_frame.py`: Handles the construction of the status frame and manages the status section and its contents.
  - `navigation_frame.py`: Handles the construction of the navigation frame and contains navigation buttons and functionalities.

#### `Menus/`

- Detailed description of each menu component.
  - `base_meny.py`: Includes shared functions for menus.
  - `control_meny.py`: Controls menu-related functionalities.
  - `hydraulic_menu.py`: Manages hydraulic-related functionalities.
  - `start_menu.py`: Handles the start menu functionalities.

### `utils/`

- Contains utility functions and tools for the application.
  - `button_manager.py`: functions for creating buttons and keyboard focus.
  - `mqtt_publisher.py`: Outline the responsibilities of handling MQTT messaging.
  - `update_status.py`: Function for device status update.
  - `window_utils.py`: Function for setting max size for the window.

### `main.py`

Describe the entry point of the application.

### `maincontroller.py`

Responsible for managing the core functionalities of the application.

### `.gitignore`

Specifies the types of files that should be ignored by version control.

### `requirements.txt`

Lists all dependencies required by the project.

## Usage

Instructions on how the end-user should use the application, including navigation through different menus and executing core functions.

## Contributing

Guidelines for how to contribute to the project, including coding standards, pull request process, etc.
