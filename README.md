# Security Scripts

Small Python scripts for security basics.

## Log Parser
Reads an auth log and counts failed login attempts per IP address.
This helps spot brute-force attacks.

Usage:
python log_parser.py

Sample output:
192.168.1.10: 2 failed attempts
