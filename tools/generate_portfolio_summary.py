import os
import re

REVIEW_DIR = "reviews"
OUTPUT_FILE = "portfolio_summary.md"

def parse_findings(review_path):
    findings_path = os.path.join(review_path, "findings.md")
    findings = []
    if os.path.exists(findings_path):
        with open(findings_path, 'r', encoding='utf-8') as f:
            for line in f:
                # Basic parsing to extract severity
                if "Critical" in line and "|" in line:
                    findings.append("Critical")
                elif "High" in line and "|" in line:
                    findings.append("High")
                elif "Medium" in line and "|" in line:
                    findings.append("Medium")
    return findings

def extract_title(review_path):
    summary_path = os.path.join(review_path, "summary.md")
    if os.path.exists(summary_path):
        with open(summary_path, 'r', encoding='utf-8') as f:
            first_line = f.readline().strip()
            return first_line.replace("# Executive Summary: ", "").strip()
    return os.path.basename(review_path)

def main():
    print("Generating Portfolio Summary...")
    reviews = [d for d in os.listdir(REVIEW_DIR) if os.path.isdir(os.path.join(REVIEW_DIR, d))]
    
    total_critical = 0
    total_high = 0
    
    content = "# Security Design Review Portfolio Summary\n\n"
    content += "## Review Status\n\n"
    content += "| Review Name | Critical Findings | High Findings | Status |\n"
    content += "| :--- | :--- | :--- | :--- |\n"
    
    for review in reviews:
        path = os.path.join(REVIEW_DIR, review)
        title = extract_title(path)
        findings = parse_findings(path)
        
        crit = findings.count("Critical")
        high = findings.count("High")
        
        total_critical += crit
        total_high += high
        
        content += f"| [{title}](./descriptions/{review}/summary.md) | {crit} | {high} | Complete |\n"
        
    content += "\n## Aggregated Metrics\n"
    content += f"*   **Total Reviews**: {len(reviews)}\n"
    content += f"*   **Total Critical Findings Identified**: {total_critical}\n"
    content += f"*   **Total High Findings Identified**: {total_high}\n"
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Generated {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
