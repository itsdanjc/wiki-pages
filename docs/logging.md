# Logging
File: `WikiPages/utils/log.py`

Last Updated: `28/02/2025`

---
## Overview
WikiPages logs various details about its operation, including accessed routes and active users. Logs are available in both the terminal and log files, depending on the mode and configuration.
### File Logging

The location of log files differs,  depending on the operating system.
#### Windows
```powershell
%APPDATA%\Temp\wikipages\wikipages_<ui/api>_<timestamp>.log
```
#### Linux
```shell
/var/log/wikipages/wikipages_<ui/api>_<timestamp>.log
```
#### MacOS
```
~/Library/Logs/wikipages/wikipages_<ui/api>_<timestamp>.log
```
### Terminal Logging
Logs are displayed in the terminal when WikiPages is running in debug or [verbose](#) modes.

## Environment Variables
- The format of terminal messages can be customized using `LOG_FORMAT`. The syntax follows python's built-in logging library.
- The logging level can be changed from the default `WARN` via `LOG_LEVEL`. This only effects log files, the level of terminal logs is always `DEBUG`.