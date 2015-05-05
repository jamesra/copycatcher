import metrics 
from operator import itemgetter


def _PrintDivider():
    print('\n**********************\n')
      
def PrintSharedTextBlocks(text_block_dict):
    _PrintDivider()
    for rec_list in text_block_dict.values():
        text = rec_list[0].text
        print(text)
        students = metrics.get_student_list(rec_list)
        print_student_list(students)
        
    _PrintDivider()
        
def PrintNumMatchesForStudentGroups(text_block_dict):
    
    _PrintDivider()
    
    dict_match_count = metrics.BuildNumMatchesForStudentGroups(text_block_dict)
    
    for (students_key, match_count) in sorted(dict_match_count.items(), key=itemgetter(1), reverse=True):
        print(students_key)
        print("%d Matches\n\n" % match_count)
        
    _PrintDivider()

def print_student_list(known_students):
    outstr = []
    for s in known_students:
        outstr.append("\t" + s)
    
    print('\n'.join(outstr))
        