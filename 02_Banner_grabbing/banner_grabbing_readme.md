# SSH Banner Grabbing

A simple Python script that connects to a specified host and port and attempts to retrieve the service banner. It is useful for basic network/service identification.

## Features

- Accepts a host/IP and port from the user.
- Establishes a TCP connection with a 3-second timeout.
- Reads up to 4096 bytes of banner data.
- Handles connection timeouts, refused connections, and OS errors.
- Displays the retrieved banner.

## Usage

```bash
python banner_grabber.py
```

Enter the target host/IP and port when prompted.

Example:

```text
Enter Host domain/IP : 192.168.1.4
Enter port number : 22
192.168.1.4, 22 -> SSH-2.0-OpenSSH_...
```

> Use this script only on systems you own or are authorized to test.

## Author

GitHub: [anonymo21](https://github.com/anonymo21)
