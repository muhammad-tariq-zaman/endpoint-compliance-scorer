"""Score endpoint compliance from a CSV and list the worst first.

Usage: python3 main.py endpoints.csv
CSV columns: endpoint,os_patched,antivirus,encrypted,firewall,last_seen_days
yes/no columns score: patched 30, antivirus 25, encrypted 20, firewall 15;
seen within 7 days scores 10. Grades: >=90 COMPLIANT, >=70 AT RISK,
otherwise NON-COMPLIANT.
"""
import argparse
import csv
import sys

WEIGHTS = {"os_patched": 30, "antivirus": 25, "encrypted": 20, "firewall": 15}


def score(row):
    total = 0
    for column, weight in WEIGHTS.items():
        if row[column].strip().lower() == "yes":
            total += weight
    if int(row["last_seen_days"]) <= 7:
        total += 10
    return total


def grade(points):
    if points >= 90:
        return "COMPLIANT"
    if points >= 70:
        return "AT RISK"
    return "NON-COMPLIANT"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", help="CSV endpoint file")
    args = parser.parse_args(argv)
    scored = []
    with open(args.path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            points = score(row)
            scored.append((points, row["endpoint"], grade(points)))
    scored.sort()
    for points, endpoint, state in scored:
        print(f"{endpoint}: {points}/100 {state}")
    non_compliant = sum(1 for _, _, state in scored if state == "NON-COMPLIANT")
    print(f"{non_compliant}/{len(scored)} endpoint(s) non-compliant.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
