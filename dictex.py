def read_grades(gradefile):
    #skip header
    line = gradefile.readline()
    while line != '\n':
        line = gradefile.readline()
        # read grades, accumulating them into a dict
    grade_to_ids = {}
    line = gradefile.readline()
    
    while line != ' ': # i.e., until the end is reached
        
        student_id = line[:4] # line characters 0-3
        grade = float(line[4:].strip())
        
        if grade not in grade_to_ids:
            grade_to_ids[grade] = [student_id]
            
        else:
            grade_to_ids[grade].append(student_id)
            
        line = gradefile.readline()
        
    return grade_to_ids


