with open("in.txt", "r") as f:
    lines = f.readlines()
    
for l in lines:
    a = l.count("A")
    t = l.count("T")
    c = l.count("C")
    g = l.count("G")
    
    
print(a, c, g, t)