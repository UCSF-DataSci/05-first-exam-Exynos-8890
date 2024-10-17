import argparse
import re
import os

parser = argparse.ArgumentParser()
parser.add_argument('dnaseq_file', type=str, help="Path to the file containing the DNA sequence")
parser.add_argument('cutsite',type=str, nargs='?',default='T|C',help = 'cut site sequence')
args = parser.parse_args()
with open(os.getcwd() +"/bioinformatics_project/" +args.dnaseq_file, 'r') as file:
    dnaseq = file.read()
dnaseq = dnaseq.strip().replace(" ", "").replace("\n","")
cut_site = parser.parse_args().cutsite.strip().replace(" ","")
print("Analyzing cut site: ", cut_site.replace("|",""))
print("Original sequence: ", len(dnaseq))
cut_positions = [m.start() for m in re.finditer(cut_site.replace('|', ''), dnaseq)]
print("Total cut sites found: ",len(cut_positions))
pair_dict = {}
for i in range(len(cut_positions)):
    for j in range(i, len(cut_positions)):
        if 80000 < cut_positions[j] - cut_positions[i] < 120000:
            pair_dict[str(cut_positions[i])] = cut_positions[j]
print("Cout site pairs 80-120 kbp apart: ",len(pair_dict))
print("First 5 pairs:")
for idx, (key, value) in enumerate(pair_dict.items()):
    if idx >= 5:
        break
    print(f"{idx + 1}. {key} -> {value}")

with open(os.getcwd() + '/bioinformatics_project/results/distant_cutsite_summary.txt', 'w') as f:
    f.write("Analyzing cut site: " + cut_site.replace("|", "") + "\n")
    f.write("Total cut sites found: " + str(len(cut_positions)) + "\n")
    f.write("Cut site pairs 80-120 kbp apart: " + str(len(pair_dict)) + "\n")
    f.write("First 5 pairs:\n")
    for idx, (key, value) in enumerate(pair_dict.items()):
        if idx >= 5:
            break
        f.write(f"{idx + 1}. {key} -> {value}\n")
print("Results saved to bioinformatics_project/results/distant_cutsite_summary.txt")