import os
import re
import sys

REVIEW_DIR = "reviews"
REQUIRED_FILES = ["architecture.md", "threat-model.md", "findings.md", "summary.md", "assumptions.md"]

def validate_math(row, line_num, file_path):
    # Regex to extract numeric values from cells like "4 (Likely)"
    # Matches " | ... | 4 (Likely) | 5 (Critical) | **20** | ..."
    match = re.search(r"\|\s*(\d+).*?\|\s*(\d+).*?\|\s*\**(\d+)\**\s*\|", row)
    if not match:
        return # Skip rows that don't look like data (headers/separators)
    
    likelihood = int(match.group(1))
    impact = int(match.group(2))
    score = int(match.group(3))
    
    if likelihood * impact != score:
        print(f"ERROR: Math mismatch in {file_path}:{line_num}")
        print(f"  Likelihood ({likelihood}) * Impact ({impact}) != Score ({score})")
        return False
    return True

def validate_review(review_path):
    print(f"Scanning {review_path}...")
    failures = 0
    
    # 1. Check Required Files
    for req in REQUIRED_FILES:
        if not os.path.exists(os.path.join(review_path, req)):
            print(f"  FAIL: Missing {req}")
            failures += 1
            
    # 2. Validate Findings Table Logic
    findings_path = os.path.join(review_path, "findings.md")
    if os.path.exists(findings_path):
        with open(findings_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                if line.strip().startswith("|") and not ("Likelihood" in line or ":---" in line):
                    if not validate_math(line, i+1, findings_path):
                        failures += 1
                        
    return failures

def main():
    if not os.path.exists(REVIEW_DIR):
        print(f"Error: Directory {REVIEW_DIR} not found.")
        sys.exit(1)
        
    total_failures = 0
    reviews = [d for d in os.listdir(REVIEW_DIR) if os.path.isdir(os.path.join(REVIEW_DIR, d))]
    
    for review in reviews:
        total_failures += validate_review(os.path.join(REVIEW_DIR, review))
        
    if total_failures > 0:
        print(f"\n❌ Validation Failed with {total_failures} errors.")
        sys.exit(1)
    else:
        print("\n✅ All reviews passed validation!")
        sys.exit(0)

if __name__ == "__main__":
    main()
