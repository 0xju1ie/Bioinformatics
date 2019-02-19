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
  is_unique = 0;
  pri
  primer_start = 0
  primer_end = 20e 
  section = dna[300:500]
  section_complement = complement_dna(section)
  
  #this primer has to be checked that it is unique
 	complement_dna = complement_dna(dna)
  
  while(is_unique != -1)
  {
    #of that 200, we need to get the primer of 20
  	primer = section_complement[primer_start:primer_end]
    
 		#search this complement for a match of the pirmer
  	is_unique = complementary_dna.find(primer)
    primer_start++
    primer end++
    
  }
 	return primer
  
  #if is_unique is -1 then it is unique!

  

# Create complement of DNA
def complement_dna(self, index):
  index = ""
  new_dna = ""
  for index in self:
  	if index == "A":
      new_dna + "T"
    if index == "T":
      new_dna + "A"
    if index == "C":
      new_dna + "G"
    if index == "G":
      new_dna + "C"
  return new_dna


def PCR(dna):
  # Denaturing - split the current dna strand and hold itself and its complement
  _3_to_5 = 
  _5_to_3 = 
  
  # See if the primer is in the new dna sections
  count = _3_to_5.count(primer)
  try:
    count == 1
  except:
    
  
  # Annealing - bind primers
  
  # Extension - double dna 
    
# Replication loop:
# Use two queues to hold original dna segments, and newly complemented dna segments of differing lengths.
# In using two different queues we are able to branch out the new dna segments and multiply the number
# of copied dna segments by 2^n, where n is the number of replication cycles.

# Original segment of dna:
#~~~~~~~ and complement? 
   	
# Initialize Q, and new Q with infinite number of members for large amount of copied segments
current_q = queue.Queue(0)
new_q = queue.Queue(0)

# Insert initial dna section, and the complement of that section
current_q.put(section)
current_q.put(section_complement)

for i in range(NUM_CYCLE):
  # Perform PCR on the elements on the current queue  
    
    
    
    
    
    
    


