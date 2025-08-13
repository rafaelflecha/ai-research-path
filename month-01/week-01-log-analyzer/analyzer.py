from pathlib import Path

def analyze_logs(log_file_path):
    log_counts = { "INFO": 0, "WARNING": 0, "ERROR": 0 }
    
    try:
        with open(log_file_path, 'r') as file:
            for line in file:
                if "INFO" in line:
                    log_counts["INFO"] += 1
                elif "WARNING" in line:
                    log_counts["WARNING"] += 1
                elif "ERROR" in line:
                    log_counts["ERROR"] += 1
    except FileNotFoundError:
        print(f"Error: File not found at {log_file_path}")
        return None
    
    return log_counts

def print_summary(counts):
    if not counts:
        return 
    print("Log Level Analysis")
    print("------------------")
    for level, count in counts.items():
        print(f"{level}: {count}")

if __name__ =="__main__":
    path = Path("sample.log")
    counts = analyze_logs(path)
    print_summary(counts)