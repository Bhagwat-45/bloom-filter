import sys

# A basic Bloom filter with two hand-computable hashes.
# Parameters fixed: m = 64 bits, k = 2 hash functions.

m = 64
k = 2
bits = [0] * m

def h1(s):
    # TODO: return sum of bytes mod m
    total = 0
    if s:
        for char in s:
            total += ord(char)
        return total%m
    return 0

def h2(s):
    # TODO: return sum of (byte * (position+1)) mod m
    #   for "apple"  ->  97*1 + 112*2 + 112*3 + 108*4 + 101*5  mod 64
    total = 0
    if s:
        for i,char in enumerate(s): 
            total += ord(char)*(i+1)
        return total%m
            
    return 0

out = []
for raw in sys.stdin:
    line = raw.rstrip("\n")
    if not line:
        continue
    parts = line.split(" ", 1)
    cmd = parts[0]
    arg = parts[1] if len(parts) > 1 else ""

    if cmd == "ADD":
        # TODO: set bits[h1(arg)] and bits[h2(arg)] to 1, then output "OK"
        bits[h1(arg)] = 1
        bits[h2(arg)] = 1
        print("OK")
        
    elif cmd == "CHECK":
        # TODO: if BOTH bits are 1, output "MAYBE"; otherwise output "NO"
        if bits[h1(arg)] == 1 and bits[h2(arg)] == 1:
            print("MAYBE")
        else:
            print("NO")
        pass
    elif cmd == "BITS":
        # TODO: output the bit array as a 64-character string
        print("".join(str(b) for b in bits))

sys.stdout.write("\n".join(out) + "\n")
