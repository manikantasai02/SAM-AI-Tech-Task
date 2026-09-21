# File Integrity Checker

A lightweight Python tool to monitor, calculate, and verify the integrity of files using cryptographic hashing algorithms (**SHA-256** and **MD5**). This script helps detect unauthorized modifications, corruption, or missing files by establishing a baseline hash snapshot and comparing it against subsequent checks.

## Features

* **Dual Hashing Support:** Supports both `SHA-256` (default) and `MD5` hashing protocols.
* **Efficient Chunk Processing:** Reads files in binary chunks (4096 bytes) to remain performance-friendly even for large files.
* **Status Detection:** Automatically classifies files into one of three statuses during comparisons:
  * ✅ `Unmodified`: The file has not changed.
  * ⚠️ `Modified`: The file's contents have changed since the baseline check.
  * `Missing`: The file was deleted or cannot be found at the path specified.

## Core Functions

* **`calculate_hash(file_path, algorithm)`**: Computes the hexadecimal digest of a specific file.
* **`check_integrity(files, algorithm)`**: Batch processes a list of files to return a dictionary of their calculated hashes.
* **`compare_hashes(original_hashes, current_hashes)`**: Discovers discrepancies between an early baseline map and a current snapshot.

## Getting Started

### Prerequisites
* Python 3.x Installed

### Setup and Execution

1. Clone or download the script file.
2. Edit the file path list inside the execution block to match files on your local drive:
   ```python
   files_to_check = [r"C:\path\to\your\file1.txt", r"C:\path\to\your\file2.txt"]
   ```
3. Run the script using your terminal or IDE:
   ```bash
   python script_name.py
   ```

## Example Output

When executed, the system logs structural dictionaries representing the lifecycle of your checks:

```python
Baseline Hashes: {'C:\\sai\\INTERN2\\TEST1.txt': 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'}
Current Hashes: {'C:\\sai\\INTERN2\\TEST1.txt': 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'}
Integrity Status: {'C:\\sai\\INTERN2\\TEST1.txt': 'Unmodified ✅'}
```
