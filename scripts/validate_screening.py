"""Validate the minimum fields and controlled decisions in a screening CSV."""
import csv, sys

REQUIRED = {"record_id", "reviewer1_decision", "reviewer2_decision", "adjudication"}
DECISIONS = {"include", "exclude", "unclear", "not_assessed", ""}

def main(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        raise SystemExit("ERROR: CSV has no data rows")
    missing = REQUIRED - set(rows[0])
    if missing:
        raise SystemExit("ERROR: missing columns: " + ", ".join(sorted(missing)))
    errors, ids = [], set()
    for n, row in enumerate(rows, 2):
        rid = row["record_id"].strip()
        if not rid: errors.append(f"row {n}: empty record_id")
        if rid in ids: errors.append(f"row {n}: duplicate record_id {rid}")
        ids.add(rid)
        for col in REQUIRED - {"record_id"}:
            if row[col].strip().lower() not in DECISIONS:
                errors.append(f"row {n}: invalid {col}={row[col]}")
    if errors:
        print("VALIDATION FAILED")
        print("\n".join(errors))
        return 1
    print(f"VALID: {len(rows)} records; unique IDs; controlled decisions accepted")
    return 0

if __name__ == "__main__":
    if len(sys.argv) != 2: raise SystemExit("Usage: validate_screening.py screening.csv")
    raise SystemExit(main(sys.argv[1]))

