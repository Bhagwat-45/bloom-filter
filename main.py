import sys
import math

out = []
for raw in sys.stdin:
    line = raw.rstrip("\n").strip()
    if not line:
        continue
    parts = line.split()

    if parts[0] == "OPTIMAL":
        p = float(parts[1])
        n = float(parts[2])
        m_opt = math.ceil(-n * math.log(p) / (math.log(2) ** 2))
        k_opt = max(1, round((m_opt / n) * math.log(2)))
        out.append(f"m={m_opt} k={k_opt}")

    elif parts[0] == "FP":
        m = float(parts[1])
        n = float(parts[2])
        k = float(parts[3])
        fp = (1 - math.exp(-k * n / m)) ** k
        out.append(f"{fp:.6f}")

    elif parts[0] == "BPI":
        p = float(parts[1])
        bpi = -math.log(p) / (math.log(2) ** 2)
        out.append(f"{bpi:.4f}")

sys.stdout.write("\n".join(out) + "\n")