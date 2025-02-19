import sys

def parse_record(record):
    parts = record.split(";", 1)
    if len(parts) < 2:
        return None
    field1 = parts[0].strip()
    remainder = parts[1]
    if not remainder.startswith('"'):
        return None
    desc_builder = []
    i = 1
    in_quotes = True
    while i < len(remainder):
        ch = remainder[i]
        if ch == '"':
            if i+1 < len(remainder) and remainder[i+1] == '"':
                desc_builder.append('"')
                i += 2
                continue
            else:
                in_quotes = False
                i += 1
                break
        else:
            desc_builder.append(ch)
        i += 1
    if in_quotes:
        return None
    desc_field = "".join(desc_builder).strip()
    if i >= len(remainder) or remainder[i] != ';':
        return None
    i += 1
    tail = remainder[i:]
    tail_parts = tail.split(";")
    if len(tail_parts) < 5:
        return None
    tail_parts = tail_parts[:5]
    result = [
        field1,
        desc_field,
        tail_parts[0].strip(),
        tail_parts[1].strip(),
        tail_parts[2].strip(),
        tail_parts[3].strip(),
        tail_parts[4].strip()
    ]
    return result

def main():
    raw = sys.stdin.read()
    lines = raw.split("\n")
    if lines and lines[0].startswith("nome"):
        lines = lines[1:]
    rows = []
    buffer = ""
    for line in lines:
        if not buffer:
            buffer = line
        else:
            buffer += "\n" + line
        if buffer.count(";") >= 6:
            rows.append(buffer)
            buffer = ""
    if buffer.count(";") >= 6:
        rows.append(buffer)
    composers = set()
    period_counts = {}
    period_titles = {}
    for row_txt in rows:
        parsed = parse_record(row_txt)
        if not parsed or len(parsed) < 7:
            continue
        nome = parsed[0]
        periodo = parsed[3]
        compositor = parsed[4]
        composers.add(compositor)
        period_counts[periodo] = period_counts.get(periodo, 0) + 1
        period_titles.setdefault(periodo, []).append(nome)
    print("1) Sorted composers:")
    for c in sorted(composers):
        print("   ", c)
    print("\n2) Distribution of works by period:")
    for p, count in period_counts.items():
        print(f"   {p}: {count} works")
    print("\n3) Period -> sorted list of titles:")
    for p, titles in period_titles.items():
        print(f"\n   {p}:")
        for t in sorted(titles):
            print("       ", t)

if __name__ == "__main__":
    main()
