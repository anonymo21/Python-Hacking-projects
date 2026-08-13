# Port Scanner Using Socket

A simple Python port scanner built with the `socket` module. It checks whether TCP ports on a specified host are open, closed, or filtered.

## Features

- Scan a single port
- Scan a range of ports
- Scan all ports from `1` to `65535`
- Uses a 1-second connection timeout

## Requirements

- Python 3.x
- No external libraries required

## Usage

Run the script:

```bash
python port_scanner.py
```

Then enter the target hostname/IP and select a scan option.

> **Note:** Only scan hosts you own or have explicit permission to test. Unauthorized port scanning may violate policies or laws.

## How It Works

The scanner creates a TCP socket for each port and uses `connect_ex()` to test the connection. A return value of `0` indicates that the port is open.

## Author

GitHub: [anonymo21](https://github.com/anonymo21)
