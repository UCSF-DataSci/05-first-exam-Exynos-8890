import random
import os

random.seed(1234)
line_len = 80
total_len = 10**6  # Use ** for exponentiation
line_num = total_len // line_len  # 12500

output = ""
for i in range(line_num):
    output += "".join(random.choices("ACGT", k=line_len)) + "\n"

output_addr = os.path.join(os.path.dirname(__file__), "../data/random_sequence.fasta")
with open(output_addr, "w") as f:
    f.write(output)

print(f"Random sequence has been generated and saved to {output_addr}")