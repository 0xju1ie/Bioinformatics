from random import choice, randint

# Create complement of DNA
dna = ""
count = 1
for count in range(400):
 dna += choice("ATCG")
# print(dna)

primer1 = dna[300:400]
# print(primer1)

print("\n\n")


# index = ""
# for index in dna:

#     if index == "A":
#         print("T")
#     elif index == "T":
#         print("A")
#     elif index == "C":
#         print("G")
#     elif index == "G":
#         print("C")



print("testing now")

primer1 = dna[300:400]
print(primer1)


# Create complement of DNA
def complement_dna(self, index):
    index = ""
    new_dna = ""
    for index in self:
        if index == "A":
            new_dna += "T"
        if index == "T":
            new_dna += "A"
        if index == "C":
            new_dna += "G"
        if index == "G":
            new_dna += "C"
    return new_dna


complemented = complement_dna(primer1, len(primer1))

print(complemented)

