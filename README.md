# Hermes

Hermes is a simple digital assistant that helps users with scheduling events, setting reminders, and quick information retrieval through natural language queries.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The purpose of Hermes is to enhance users' productivity by providing a user-friendly interface for managing daily tasks. It offers the following key features:

- **Scheduling:** Users can schedule events with specific dates and times.
- **Reminders:** Set reminders for scheduled events with timely notifications.
- **Information Retrieval:** Natural language queries for quick information retrieval.

## Features

- Modular Python codebase for easy maintenance.
- Test-driven development with unit tests in the `tests/` directory.
- Documentation in the `docs/` directory, including requirements and project plan.

## Getting Started

### Prerequisites

- Python 3.x
- Pip (Python package installer)

### Installation

1. Clone the repository:
   ```bash
   git clone git@github.com:eduardoalsilva/Hermes.git
   cd Hermes
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

- Run the main application:
  ```bash
  python src/app.py
  ```

- Run tests:
  ```bash
  python -m unittest discover -s tests
  ```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the project.
2. Create a new branch (`git checkout -b feature/my-feature`).
3. Make your changes and commit them (`git commit -am 'Add my feature'`).
4. Push to the branch (`git push origin feature/my-feature`).
5. Open a pull request.

## License

This project is licensed under the [MIT License](LICENSE).