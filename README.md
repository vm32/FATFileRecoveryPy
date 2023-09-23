# FATFileRecoveryPy

FATFileRecoveryPy is a Python-based tool designed for educational purposes to demonstrate the process of recovering deleted files from a FAT (File Allocation Table) file system. The tool reads the file system structure at a low level, identifies deleted files, and attempts to recover them.

## Disclaimer

This tool is a simplified example and is intended for educational purposes only. It may not handle all edge cases or variations of the FAT file system. For critical data recovery, it is recommended to use professional data recovery tools or services. Always work on a copy of the file system to avoid further data loss.

## Features

- Reads and interprets the FAT file system structure.
- Identifies deleted files in the root directory.
- Recovers and saves deleted files.

## Usage

1. Clone the repository:
   ```git clone https://github.com/vm32/FATFileRecoveryPy.git```
## FAT Directory Entry Status

In the FAT file system, each file or directory has an associated directory entry stored in the root directory or in another directory. The first byte of the directory entry is used to store the file's status. Here are some of the possible values for this byte and their meanings:

| Hex Value | Description |
|-----------|-------------|
| `0x00`    | Entry is available and no subsequent entry is in use (end of directory). |
| `0x05`    | The actual first character of the name is 0xE5. |
| `0x2E`    | Dot entry: either '.' or '..'. |
| `0xE5`    | Entry has been previously erased and is available. File may be recoverable. |
| `0x20` - `0x7F` | The first character of a file or directory name. |

In addition to the first byte, there are other attributes and flags in the directory entry that provide information about the file or directory. These attributes are stored in the 11th byte of the directory entry.

| Bit | Attribute | Description |
|-----|-----------|-------------|
| 0   | Read Only | File is read-only. |
| 1   | Hidden    | File is hidden. |
| 2   | System    | File is a system file. |
| 3   | Volume ID | Entry is a volume label, not a file or directory. |
| 4   | Directory | Entry is a subdirectory. |
| 5   | Archive   | File has been modified since last backup. |

![alt text](https://img001.prntscr.com/file/img001/aJoa9v6ySr-NLfpIA48C7Q.png)
