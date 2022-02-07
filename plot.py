f = open("data/example.csv")
lines = [x.strip().split(",") for x in f.readlines()[1:]]
print(len(lines))
f.close()
