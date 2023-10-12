# SFTP Auto File Transfer Program

[![Python Version](https://img.shields.io/badge/python-%3E%3D%203.6-blue.svg)](https://www.python.org/downloads/) [![Paramiko Version](https://img.shields.io/badge/paramiko-2.7.2-blue)](https://pypi.org/project/paramiko/)

## Overview

This Python program facilitates automatic file transfer from one server to another using SFTP. The program reads configurations from `config.py` and uses a JSON file (`sftp.json`) to determine the source and destination paths for file transfer.

## Requirements

Ensure you have Python 3.6 or higher installed:

```bash
pip3 install paramiko
```

## Configuration

### config.py

1. Set the following parameters in `config.py`:

    ```python
    hostname = ''  # Hostname of the target system
    username = ''  # Username of the target system
    key_filename = '.pem'  # PEM file path of the target system in the source system OR
    key_password = ''  # Password of the target system (used above username)
    sftppath = '/opt/outbox'  # Path where you want to send the files on the target system
    logpath = '/opt/SFTP/log'  # Log path for file transfer on the source system
    JSONpath = 'sftp.json'  # JSON-based config file path for inbox and outbox paths
    ```

### sftp.json

2. Configure `sftp.json` with source and destination paths:

    ```json
    [
      {
        "source": "File1",
        "path": "/opt/fileonegenofsystem/inbox",
        "outboxpath": "/opt/fileonegenofsystem/outbox"
      }
    ]
    ```

## How to Run

1. Navigate to the source code directory.

2. Run the following command in the command prompt or shell:

    ```bash
    python3 index.py
    ```

    or

    ```bash
    py index.py
    ```

## Working Steps

1. **Configuration Reading:**
   - The `index.py` script reads the configuration from `config.py` and the JSON file specified by `JSONpath`.

2. **Inbox Check:**
   - The program checks the inbox path for files based on the configurations in `sftp.json`.

3. **SFTP Connection:**
   - Initiates an SFTP server connection using the provided details (hostname, username, key_filename/key_password).

4. **File Transfer:**
   - Upon successful connection, it transfers the files to the target destination (`sftppath`).

5. **Outbox Transfer:**
   - After a successful transfer, the program moves the same file to the outbox (`outboxpath`).

6. **Logging:**
   - The system creates logs in the specified log path (`logpath`) for tracking and logging purposes.

## Note

- Ensure that both configurations (`config.py` and `sftp.json`) are correctly configured.
- Verify that the specified paths exist.
- Run the program responsibly after thorough configuration checks.