import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser(description="Simple plot for GDBx data. Expects same measure_name, location, cause_name and metric_name in every line!")
parser.add_argument('--infile', "-i", dest="infile", help='Input filename', required=True)
parser.add_argument('--outfile', "-o", dest="outfile", help='Output png filename', required=True)
args = parser.parse_args()

f = open(args.infile)
lines = [x.strip().split(",") for x in f.readlines()[1:]]
f.close()

what = lines[0][1]
how = lines[0][11]
why = lines[0][9]
where = lines[0][3]

data = [(x[12], x[13]) for x in lines]
data.sort(key = lambda x: x[0])

years = [x[0] for x in data]
vals = [float(x[1]) for x in data]
fig, ax = plt.subplots()
ax.plot(years, vals)
ax.set(xlabel="Year", ylabel=what + " (" + how + ")", title=what + " (" + how + ") due to " + why + " in " + where)
ax.set_xticklabels(labels=years, rotation=45)
fig.set_figwidth(10)
fig.set_figheight(10)
fig.savefig(args.outfile)
