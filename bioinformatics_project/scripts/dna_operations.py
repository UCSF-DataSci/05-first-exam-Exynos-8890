import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('dnaseq', type=str, nargs='?', default='ATCG', help="DNA sequence")
    dnaseq = parser.parse_args().dnaseq
    print("Original sequence: ",dnaseq)
    complement = {
        'A' : 'T',
        'C' : 'G',
        'G' : 'C',
        'T' : 'A'
    }
    dnaseq_com = ''.join(complement[i] for i in dnaseq)
    print("Complement: " , dnaseq_com)
    dnaseq_rev = dnaseq[::-1]
    print("Reverse: ",dnaseq_rev)
    dnaseq_com_rev = dnaseq_com[::-1]
    print("Reverse complement: ", dnaseq_com_rev)