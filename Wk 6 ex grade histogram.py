import tkinter.filedialog
#allows the user to call the function on any file
import grade # mine is called Wk 6 ex grades.py
#separate file containing the functions needed to make the list & histogramS

a1_filename = tkinter.filedialog.askopenfilename()
a1_file = open(a1_filename, 'r')
# file of grade information now open for reading

a1_histfilename = tkinter.filedialog.asksaveasfilename()
a1_histfile = open(a1_histfilename, 'w')
# histogram file opened for writing, as 'save' location

# Read the grades into a list -- function from other file; note that 
# grade.read_grades() is formatted to use these through the name of 
# the module
grades = grade.read_grades(a1_file)

# Count the grades per range.
range_counts = grade.count_grade_ranges(grades)

# print(range_counts)

# Write the histogram to the file.
grade.write_histogram(range_counts, a1_histfile)

a1_file.close()
a1_histfile.close()
