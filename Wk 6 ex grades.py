def read_grades(gradefile):
    '''(file open for reading) -> list of float # b/c all numbers in file are floats
    Read and return the list of grades in gradefile.
 
    Precondition: gradefile starts with a header that contains
    no blank lines, then has a blank line, and then lines
    containing a student number and a grade.
    '''

    # Skip over the header.
    line = gradefile.readline()
    while line != '\n':
        line = gradefile.readline() # follows precondition structure above --
		# read the next line until you find the new line character

    # Read the grades, accumulating them into a list.

    grades = []
	# accumulator for all grades in the file
    
    line = gradefile.readline()
    while line != '':
        # Now we have s string containing the info for a single student.
        # Find the last space (i.e., space before the grade number) and take 
		# everything after that space.
        grade = line[line.rfind(' ') + 1:] 
		# rfind finds from the right -- gives index for rightmost space; 
		# line[] here will slice the string from one past that space to 
		#the end of the grade-number string
        grades.append(float(grade))
		# append number to grade list after turning it into a float
        line = gradefile.readline()
		# read & process next line

    return grades
	# returns a list of the grades in the order they appear in the list

def count_grade_ranges(grades):
    '''(list of float) -> list of int

    Return a list of int where each index indicates how many grades were in these
    ranges:

    0-9: index 0
    10-19: 1
    20-29: 2
      :
    90-99: 9
    100:   10

    >>> count_grade_ranges([77.5, 37.5, 0.5, 9.5, 72.5, 100.0, 55.0, 70.0, 79.5])
    [2, 0, 0, 1, 0, 1, 0, 4, 0, 0, 1]
    '''

    range_counts = [0] * 11
	# creates a list of length 11 in which all items are 0 -- these
	# will be updated as we look at each number

    for grade in grades:
        which_range = int(grade // 10)
		# the index for each number in the output list above -- index[0] is 
		# range 0-9, index[1] is range 10-19, index[2] is range 20-29, etc --
		# index no. is the tens digit, which is why the division in the line
		# above works: this gives back, for example, just the 7 in 77.5, so it
		# counted in the range for index 7
		
		# the division gives back a float, but to be used as an index
		# this must be an int -- hence int() above
        range_counts[which_range] = range_counts[which_range] + 1
		# adds 1 to the initial count for that range each time a grade from
		# that range is found

    return range_counts


def write_histogram(range_counts, histfile):
    '''(list of int, file open for writing) -> NoneType
	# doesn't return anything -- just writes the file

    Write a histogram of *s based on the number of grades in each range.

    The output format:
    0-9:   *
    10-19: **
    20-29: ******
      :
    90-99: **
    100:   *
    
    '''

    histfile.write('0-9:   ')
	# write the range being counted in this row of the histogram --
	# note inclusion of extra spaces here & for 100, so that the
	# data lines up properly
	
    histfile.write('*' * range_counts[0])
	# after the range, write the appropriate number of *
    histfile.write('\n')
	# write does not put a new line character at the end of a line, so it
	# needs to be included explicitly

    # Write the 2-digit ranges (up to but not including 10)
    for i in range(1, 10):
	    # figure out the numbers on each end of the range
        low = i * 10
        high = i * 10 + 9
        histfile.write(str(low) + '-' + str(high) + ': ')
		# write the range, with hyphen, colon, and space
        histfile.write('*' * range_counts[i])
		# multiply by range counts at index i
        histfile.write('\n')
		# write new line character

    histfile.write('100:   ')
    histfile.write('*' * range_counts[-1])
	# range count at the last index
    histfile.write('\n')
