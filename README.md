# WHSYSTEM

**WHSYSTEM** is a Python tool that identifies the operating system of a remote IP address based on the TTL (Time To Live) value obtained from a ping.

## Features

- **Operating System Detection:** Sends a ping to the provided IP address and analyzes the TTL value of the response to determine the remote host's operating system.
  - **TTL 0-64:** Typically indicates a Linux-based system.
  - **TTL 65-128:** Typically indicates a Windows-based system.
  - **TTL outside these ranges:** Indicates that the operating system could not be determined.

## Usage

1. Clone the repository or download the `WichSystem.py` file.
2. Run the script from the command line, providing the target IP address:
   ```sh
   python WichSystem.py <ip-address>

## Requirements
1. Python 3.x
2. Modules re, sys, subprocess, and art (for logo visualization).

## Example 
```sh
python WichSystem.py 192.168.10.1
```

### Breakdown:

- **General Description:** Explains what the program does.
- **Features:** Details the main functionalities of the script.
- **Usage:** Instructions on how to run the script.
- **Requirements:** Lists necessary dependencies.
- **Example:** Shows how to use the script with a specific command.

This summary provides a clear and concise overview of the program’s purpose and usage, which you can add to your `README.md` file in the root of your repository.

<h3> <em> Script Status </em> </h3>

![Badge in Development](https://img.shields.io/badge/STATUS-IN%20DEVELOPMENT-green)
