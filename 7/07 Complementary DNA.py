"""
DESCRIPTION:
Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.

If you want to know more: http://en.wikipedia.org/wiki/DNA

In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". Your function receives one side of the DNA (string, except for Haskell); you need to return the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).

More similar exercise are found here: http://rosalind.info/problems/list-view/ (source)

Example: (input --> output)

"ATTGC" --> "TAACG"
"GTAT" --> "CATA"
"""


def DNA_strand(dna):
    conv_dict = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C"
    }
    trans_dict = str.maketrans(conv_dict)
    # return ''.join(conv_dict[char] for char in dna)
    return dna.translate(trans_dict)


if __name__ == '__main__':
    print(DNA_strand("ATTGC"))
    print(DNA_strand("GTAT"))
