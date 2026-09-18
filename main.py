import sys

def h_a(s):
    if s:
        return sum(b * (i + 1) for i, b in enumerate(s.encode())) & 0xFFFFFFFF
    return 0

def h_b(s):
    if s:
        return sum(b ^ (i + 1) for i, b in enumerate(s.encode())) & 0xFFFFFFFF
    return 0

out = []
for raw in sys.stdin:
    line = raw.rstrip("\n").strip()
    if not line:
        continue
    parts = line.split()
    if parts[0] == "HASH":
        s, m, k = parts[1], int(parts[2]), int(parts[3])
        ha = h_a(s)
        hb = h_b(s)
        positions = [str((ha + i * hb) % m) for i in range(k)]
        out.append(",".join(positions))
    elif parts[0] == "HA":
        out.append(str(h_a(parts[1])))
    elif parts[0] == "HB":
        out.append(str(h_b(parts[1])))

sys.stdout.write("\n".join(out) + "\n")