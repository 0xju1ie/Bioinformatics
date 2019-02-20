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
import random
from random import choice, randint
import re
import queue

# Constants
FRAGMENT_LEN = 200
MAX_RAND_LEN = 100
PRIMER_LEN = 20
NUM_CYCLES = 8


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
  section_complement = "" 

  complementary_dna = complement_dna(dna, 0)
  if len(dna) == 2000:
    section_complement = complementary_dna[300:500]
  else:
    section_complement = complementary_dna[:]

  #this primer has to be checked that it is unique
  while is_unique != 1: #of that 200, we need to get the primer of 20
    primer = section_complement[primer_start:primer_end] #search this complement for a match of the pirmer
    is_unique = complementary_dna.count(primer)
    primer_start += 1
    primer_end += 1
  return primer



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

#get fall-off rate
def d_plus_r():
    return random.randint(150,250)

#checking if it is long enough to duplicate
def is_long_enough(template, primer):
    comp_template = complement_dna(template, 0)
    is_present = comp_template.count(primer)
    return is_present


print("denaturing - 96 degrees celcius. Breaking up the DNA into two strands")
dna = generate_dna_strands()
complimentary_dna = complement_dna(dna, 0)
print("DNA strand 1: ", dna[300:500])
print("DNA strand 2: ", complimentary_dna[300:500])

print("generating Primers for each strand") 
primer1 = generate_primer(dna) 
primer2 = generate_primer(complimentary_dna) #could also do complement_dna(primer1, 0) 
print("primer 1: ", primer1) 
print("primer 2: ", primer2)

#getting the length of the first strands to replicate
fall_off_rate = d_plus_r()
print("fall off rate: ", fall_off_rate)
dna_end = 300 + fall_off_rate 
dna_section = dna[300:dna_end]
print(dna_section)
fall_off_rate = d_plus_r()
end = fall_off_rate + 300
complimentary_dna_section = complimentary_dna[300:end]

print("annealing - 55 degrees celcius. Binding the primers to the DNA strands") 

current_dna_q = queue.Queue(0)
current_primer_q = queue.Queue(0)
new_dna_q = queue.Queue(0)
new_primer_q = queue.Queue(0)

current_dna_q.put(dna_section) #comes out first
current_dna_q.put(complimentary_dna_section) 

current_primer_q.put(primer1) #comes out first
current_primer_q.put(primer2)

replicant = ""
compliment = ""

counter_150_to_159 = 0
counter_160_to_169 = 0
counter_170_to_179 = 0
counter_180_to_189 = 0
counter_190_to_199 = 0
counter_200_to_209 = 0
counter_210_to_219 = 0
counter_220_to_229 = 0
counter_230_to_239 = 0
counter_240_to_250 = 0

# Replication loop:
# need to check that the strand is long enough to duplicate
#while current_dna_q is not empty
for i in range(NUM_CYCLES):
    while current_dna_q.qsize() != 0:
        can_duplicate = True
        while can_duplicate == True:
            template = current_dna_q.get()  
            primer = current_primer_q.get()
            contains = is_long_enough(template, primer) 
            if contains == 1:
                print("yay, long enough!")
                can_duplicate = True
                compliment_end = d_plus_r()
                print("d+r = ", compliment_end)
                compliment = template[20:compliment_end]
                compliment =complement_dna(compliment, 0)
                print("compliment:", compliment)
                replicant = primer + compliment
                print("replicant: ", replicant)
                new_dna_q.put(template)
                new_dna_q.put(replicant)
                replicant_primer = generate_primer(replicant)
                print("primer: ", primer)
                print("replicant Primer: ", replicant_primer)
                new_primer_q.put(primer)
                new_primer_q.put(replicant_primer)

            else:
                print("too short")
                can_duplicate = False
            can_duplicate = False
    while new_dna_q.qsize() != 0:
        current_dna_q.put(new_dna_q.get())
        current_primer_q.put(new_primer_q.get())
print("size: ", current_dna_q.qsize())
while current_dna_q.qsize() != 0:  
    popped = current_dna_q.get()
    size_of_popped = len(popped)
    print("size of popped: ", size_of_popped)
    if size_of_popped in range(150, 160):
        counter_150_to_159 += 1
    elif size_of_popped in range(160, 170):
        counter_160_to_169 += 1
    elif size_of_popped in range(170, 180):
        counter_170_to_179 += 1
    elif size_of_popped in range(180, 189):
        counter_180_to_189 += 1
    elif size_of_popped in range(190, 200):
        counter_190_to_199 += 1
    elif size_of_popped in range(200, 210):
        counter_200_to_209 += 1
    elif size_of_popped in range(210, 220):
        counter_210_to_219 += 1
    elif size_of_popped in range(220, 230):
        counter_220_to_229 += 1
    elif size_of_popped in range(230, 240):
        counter_230_to_239 += 1
    elif size_of_popped in range(240, 250):
        counter_240_to_250 += 1
    print("size of it now: ", current_dna_q.qsize())
print("counter_150_to_159: ", counter_150_to_159)
print("counter_160_to_169: ", counter_160_to_169)
print("counter_170_to_179: ", counter_170_to_179)
print("counter_180_to_189: ", counter_180_to_189)
print("counter_190_to_199: ", counter_190_to_199)
print("counter_200_to_209: ", counter_200_to_209)
print("counter_210_to_219: ", counter_210_to_219)
print("counter_220_to_229: ", counter_220_to_229)
print("counter_230_to_239: ", counter_230_to_239)
print("counter_240_to_250: ", counter_240_to_250) 
       
 # need to empty the new qs into the current q
 # decrease cycle       


    # Use two queues to hold original dna segments, and newly complemented dna segments of differing lengths.
    # In using two different queues we are able to branch out the new dna segments and multiply the number
    # of copied dna segments by 2^n, where n is the number of replication cycles.

# Original segment of dna:
#~~~~~~~ and complement? 

# Initialize Q, and new Q with infinite number of members for large amount of copied segments


# Insert initial dna section, and the complement of that section
# current_q.put(section)
# current_q.put(section_complement)

# for i in range(NUM_CYCLE):
  # Perform PCR on the elements on the current queue  
