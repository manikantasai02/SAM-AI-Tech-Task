import hashlib
import os

def calculate_hash(file_path, algorithm="sha256"):
    """Calculate hash of a file using SHA-256 or MD5."""
    hash_func = hashlib.sha256() if algorithm.lower() == "sha256" else hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_func.update(chunk)
    return hash_func.hexdigest()

def check_integrity(files, algorithm="sha256"):
    """Check integrity of multiple files."""
    results = {}
    for file in files:
        if os.path.exists(file):
            file_hash = calculate_hash(file, algorithm)
            results[file] = file_hash
        else:
            results[file] = "File not found"
    return results

def compare_hashes(original_hashes, current_hashes):
    """Compare stored hashes with current hashes."""
    status = {}
    for file, orig_hash in original_hashes.items():
        curr_hash = current_hashes.get(file, None)
        if curr_hash is None:
            status[file] = "Missing"
        elif curr_hash == orig_hash:
            status[file] = "Unmodified ✅"
        else:
            status[file] = "Modified ⚠️"
    return status

# Example usage
if __name__ == "__main__":
    files_to_check = ["C:\sai\INTERN2\TEST1.txt", "C:\sai\INTERN2\TEST2.txt"]

    # Step 1: Generate baseline hashes
    baseline_hashes = check_integrity(files_to_check, "sha256")

    # Step 2: Later, re-check files
    current_hashes = check_integrity(files_to_check, "sha256")

    # Step 3: Compare
    integrity_status = compare_hashes(baseline_hashes, current_hashes)

    print("Baseline Hashes:", baseline_hashes)
    print("Current Hashes:", current_hashes)
    print("Integrity Status:", integrity_status)
