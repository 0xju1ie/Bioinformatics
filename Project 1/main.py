<<<<<<< HEAD
#PCR = denaturation, annealing, extension
#denaturing- heats it up and splits the dna in to the two seperate strands
#annealing- primers bind to a matching sections
#extension- starting from the primers the dna starts to be replicated by matching the base pairs of the template DNA.

#our template dna is 2000 base pairs long (n). This is created randomly, made up of A,T,C,G. (basically denaturing but not actually)
#our primers are 20 base pairs long and randomly generated.
#these primers will match up to a sequence in the template dna of 2000 base pairs.
#the primer then binds (annealing)
#now the dna can be replicated starting from the primer. This will go for a segment of about 200 (m)
#the stopping point of the replication/amplification is determined by d+r, d is equivalent to 200 (m) and r is random generated number between 50 and -50. So total length will be between 150 and 250.

# denaturation, annealing, extension
=======
>>>>>>> cb9c1dd86be73757e382f7b7f0f1fa9de1190c81
# denaturing- heats it up and splits the dna in to the two seperate strands
# annealing- primers bind to a matching sections
# extension- starting from the primers the dna starts to be replicated by matching the base pairs of the template DNA.

# our template dna is 2000 base pairs long (n). This is created randomly, made up of A,T,C,G. (basically denaturing but not actually)
# our primers are 20 base pairs long and randomly generated.
# these primers will match up to a sequence in the template dna of 2000 base pairs.
# the primer then binds (annealing)
# now the dna can be replicated starting from the primer. This will go for a segment of about 200 (m)
# the stopping point of the replication/amplification is determined by d+r, d is equivalent to 200 (m)
# and r is random generated number between 50 and -50. So total length will be between 150 and 250.

# Import Libraries
from random import choice, randint
import re
import queue

# Constants
FRAGMENT_LEN = 200
PRIMER_LEN = 20
NUM_CYCLES = 12

# Generate random DNA strand, n, of length 2000
def generate_dna_strands():
  dna = ""
  count = 1
  for count in range(2000):
    dna += choice("ATCG")
  return dna

# Pick DNA segment, m, of length 200 
def generate_primer(dna):
  #choose a section of 200
  is_unique = 0
  primer_start = 0
  primer_end = 20
  primer = ""
    
  #this primer has to be checked that it is unique
  complementary_dna = complement_dna(dna, 0)
  section_complement = complementary_dna[300:500]
  
  while is_unique != 1: #of that 200, we need to get the primer of 20
    primer = section_complement[primer_start:primer_end] #search this complement for a match of the pirmer
    is_unique = complementary_dna.count(primer)
    primer_start =+ 1
    primer_end =+ 1
  return primer

  

# Create complement of DNA
def complement_dna(self, index):
 complementary_dna = ""
 for index in self:
  if index == "A":
   complementary_dna = complementary_dna + "T"
  if index == "T":
   complementary_dna = complementary_dna + "A"
  if index == "C":
   complementary_dna = complementary_dna + "G"
  if index == "G":
   complementary_dna = complementary_dna + "C"
 return complementary_dna
    
    
# Replication loop:
# Use two queues to hold original dna segments, and newly complemented dna segments of differing lengths.
# In using two different queues we are able to branch out the new dna segments and multiply the number
# of copied dna segments by 2^n, where n is the number of replication cycles.

# Original segment of dna:
#~~~~~~~ and complement? 

print("denaturing - 76 degrees celcius. Breaking up the DNA into two strands")
dna = generate_dna_strands()
complimentary_dna = complement_dna(dna, 0)
print("DNA strand 1: ", dna)
print("DNA strand 2: ", complimentary_dna)

print("generating Primers for each strand")
primer1 = generate_primer(dna)
primer2 = generate_primer(complimentary_dna)
print("primer 1: ", primer1)
print("primer 2: ", primer2)

print("annealing - ")


   	
# Initialize Q, and new Q with infinite number of members for large amount of copied segments
current_q = queue.Queue(0)
new_q = queue.Queue(0)

# Insert initial dna section, and the complement of that section
current_q.put(section)
current_q.put(section_complement)

for i in range(NUM_CYCLE):
  # Perform PCR on the elements on the current queue  
    
    
    
    
    
    
    


