"""Compute compact PRISMA counts from screening CSVs."""
import csv, json, sys

def read(path):
    with open(path, newline="", encoding="utf-8-sig") as f: return list(csv.DictReader(f))

def main(screening, fulltext, out):
    s, f = read(screening), read(fulltext)
    result = {
        "records_screened": len(s),
        "title_abstract_excluded": sum(r.get("reviewer1_decision","").lower()=="exclude" and r.get("reviewer2_decision","").lower()=="exclude" for r in s),
        "full_text_assessed": len(f),
        "full_text_included": sum(r.get("adjudication","").lower()=="include" for r in f),
        "full_text_excluded": sum(r.get("adjudication","").lower()=="exclude" for r in f),
        "full_text_exclusion_reasons": {},
    }
    for r in f:
        if r.get("adjudication","").lower()=="exclude":
            reason = r.get("primary_exclusion_reason", "other") or "other"
            result["full_text_exclusion_reasons"][reason] = result["full_text_exclusion_reasons"].get(reason, 0) + 1
    with open(out, "w", encoding="utf-8") as fh: json.dump(result, fh, ensure_ascii=False, indent=2)
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    if len(sys.argv) != 4: raise SystemExit("Usage: build_prisma_counts.py screening.csv fulltext.csv output.json")
    main(*sys.argv[1:])

