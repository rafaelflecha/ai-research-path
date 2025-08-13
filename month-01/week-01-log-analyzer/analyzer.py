from pathlib import Path

infoCount = 0
warningCount = 0
errorCount = 0

path = Path('sample.log')

with path.open() as file:
    for line in file:
        if line.find("INFO") > -1: 
            infoCount += 1
        elif line.find("WARNING") > -1:
            warningCount += 1
        elif line.find("ERROR") > -1:
            errorCount += 1     

print("Log Level Analysis")
print("------------------")
print(f"INFO: {infoCount}")
print(f"WARNING: {warningCount}")
print(f"ERROR: {errorCount}")