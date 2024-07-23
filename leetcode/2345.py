s = "leetcode"
r = s[::-1]
sl = []
rl = []

# Create lists of adjacent character pairs for the original and reversed strings
for i in range(1, len(s)):
    sl.append(s[i-1] + s[i])
    rl.append(r[i-1] + r[i])

# Find the common pairs between sl and rl
common_pairs = set(sl).intersection(set(rl))

print(common_pairs)
