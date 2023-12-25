with open("in.txt", "r") as f:
    lines = f.readlines()

ans = ""
for l in lines:
    for c in l:
        if c == "T":
            ans += "U"
        else: ans += c
        
print(ans)