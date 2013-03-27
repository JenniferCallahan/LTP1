def get_length(dna):
    ''' (str) -> int
    Return the length of the DNA sequence dna.
    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    '''
    return len(dna)
	# works


def is_longer(dna1, dna2):
    ''' (str, str) -> bool
    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.
    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    '''
    return len(dna1) > len(dna2)
    #works



def count_nucleotides(dna, nucleotide):
    ''' (str, str) -> int
    Return the number of occurrences of nucleotide in the DNA sequence dna.
    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    '''
    return dna.count(nucleotide)
    #works
    


def contains_sequence(dna1, dna2):
    ''' (str, str) -> bool
    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.
    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False
    '''
    return dna2 in dna1
    #works

	
def is_valid_sequence(dna): 
	''' (str) -> bool 
	Return True if and only if the DNA sequence is valid (that is, it 
	contains only nucleotide characters: 'A', 'T', 'C' and 'G').
	>>> is_valid_sequence('ABCDEFG')
	False
	>>> is_valid_sequence(ATCGGC')
	True 
	'''
	valid = True
	for char in dna: 
	    if char not in 'ATCG':
		    valid = False
	return valid
	#works
	
def insert_sequence(dna1, dna2, point):
	'''(str, str, int) -> str 
	The first two parameters are DNA sequences and the third parameter is an index. Return 
	the DNA sequence obtained by inserting the second DNA sequence into the first DNA sequence 
	at the given index. (You can assume that the index is valid.) 
	>>> insert_sequence('ATTCC', 'GAGA', 2)
	'ATGAGATCC'
	>>> insert_sequence('GCCTT', 'AG', 1)
	'GAGCCTT'
	'''
	return dna1[:point] + dna2 + dna1[point:]
	#works
	
def get_complement(nucleotide): 
    ''' (str) -> str 
	The first parameter is a nucleotide ('A', 'T', 'C' or 'G'). Return the nucleotide's complement. 
	>>>'A'
	'T'
	>>>'C'
	'G'
    '''
    if nucleotide == 'A':
        return 'T'
    if nucleotide =='T':
        return 'A'
    if nucleotide =='C':
        return 'G'
    if nucleotide == 'G':
        return 'C'
    #works

def get_complementary_sequence(sequence):
    ''' (str) -> str
    The parameter is a DNA sequence. Return the DNA sequence that is complementary to the given
    DNA sequence.
    >>> 'AT'
    'TA'
    >>> 'GAGA'
    'CTCT'
    '''
    complement = ''
    for char in sequence:
        complement = complement + get_complement(char)
    return complement
    #works

	
    



