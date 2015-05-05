'''
Created on Jun 12, 2014

@author: James
'''

import filehandler
import string


class MatchRecord():
    
    @property 
    def name(self):
        return self._name
    
    @property
    def key(self):
        return self._key
    
    @property
    def text(self):
        return self._text
    
    def __init__(self, name, key, text):
        self._name = name
        self._key = key
        self._text = text
        

def BuildTextBlockDict(folder_path, block_size, trigger_set):
    '''
    :param str folder_path: Directory containing assignment files
    :return: Dictionary containing blocks of adjacent text as keys and MatchRecord values
    :rtype: dict
    '''
    
    text_block_dict = {}

    for (student, text) in filehandler.FilesToText(folder_path, '*'): 
        
        print("Processing %s" % student)
        text_block_dict = UpdateTextBlocks(text_block_dict, student, text, block_size=block_size, trigger_set=trigger_set)
        
    return text_block_dict

def RemoveIsolatedTextBlocks(text_block_dict):
    '''
    Remove all entries which only have one instance
    :param dict text_block_dict: Dictionary to remove entries from
    '''

    for (text_block, rec_list) in list(text_block_dict.items()):
        if len(rec_list) < 2:
            del text_block_dict[text_block]
    
    return

def RemoveTextBlocksWithSingleStudent(text_block_dict):
    for (text_block, rec_list) in list(text_block_dict.items()):
        student_list = get_student_list(rec_list)
        if len(student_list) == 0:
            del text_block_dict[text_block]
            
def RemoveTextBlocksFromTemplates(text_block_dict, template_name):
    '''Remove any text_blocks from the template names.  This is used if students are filling in a form that 
    has standard text that should not be counted'''
    
    if template_name is None:
        return 
    
    template_set = frozenset([template_name])
    
    for (text_block, rec_list) in list(text_block_dict.items()):
        student_list = frozenset(get_student_list(rec_list))
        if len(student_list.intersection(template_set)) >= 1:
            del text_block_dict[text_block]
        

def BuildNumMatchesForStudentGroups(text_block_dict):
    '''Construct a dictionary mapping the number of times students appear with the same text blocks'''
    
    dict_match_count = {}
    for rec_list in text_block_dict.values():
        students = get_student_list(rec_list)
        
        if len(students) > 0:
            students_key = '\n'.join(students)  
            if students_key not in dict_match_count:
                dict_match_count[students_key] = 1
            else:
                dict_match_count[students_key] += 1
    
    return dict_match_count
                
        
def Calculate_metrics(folder_path, block_size, template_name, trigger_set=None):
    
    text_block_dict = BuildTextBlockDict(folder_path, block_size, trigger_set)
    RemoveIsolatedTextBlocks(text_block_dict)
    RemoveTextBlocksWithSingleStudent(text_block_dict)
    RemoveTextBlocksFromTemplates(text_block_dict, template_name)
    
    return text_block_dict

                    
def get_student_list(rec_list):
    known_students = []
        
    for r in rec_list:
        if not r.name in known_students:
            known_students.append(r.name)
        
    if len(known_students) <= 1:
        return []
      
    known_students.sort()
    
    return known_students

def RemovePunctuation(text):
    return text.translate(string.maketrans("",""), string.punctuation)

def RemoveConnectorWords(textparts):
    for i in range(len(textparts)-1, 0,-1):
        if len(textparts[i]) <= 3:
            del textparts[i]
            
    return textparts

def IsSuperset(trigger_set, text_block):
    '''
    Frozenset would be better, but in the original test cases HPI/Assessment was often a trigger.  It was necessary to search substrings.
    '''
    if trigger_set is None:
        return True
    
    for word in trigger_set:
        if not word in text_block:
            return False
        
    return True

def UpdateTextBlocks(text_block_dict, student, text, block_size, trigger_set):
    '''
    :param dict text_block_dict: Dictionary to update
    :param str student: Name of student associated with text
    :param str text: Text we are cutting into blocks and adding into dictionary
    :param int block_size: How many words in each text block
    :param lits trigger_set: A set of words that must be present in a text_block before we begin adding blocks to the dictionary.  Used to remove headers or common text..
    '''
    
    text = text.lower() 
    text = RemovePunctuation(text)
    textparts = text[0:].split()
    
    for i in range(0, len(textparts)):
        textparts[i] = textparts[i].strip()
    
    textparts = RemoveConnectorWords(textparts)
    
    trigger_set_found = trigger_set is None
    
    if not trigger_set is None:
        if not isinstance(trigger_set, frozenset):
            trigger_set = frozenset(trigger_set)
    
    for i in range(0, len(textparts)-block_size):
        
        text_key = ' '.join(sorted(textparts[i:i+block_size]))
        text_block = ' '.join(textparts[i:i+block_size])
        
        if IsSuperset(trigger_set, text_block):
            trigger_set_found = True
             
        if not trigger_set_found:
            continue
        
        text_block = text_block.lower()
        record = MatchRecord(name=student, key=text_key, text=text_block)
        
        if text_block in text_block_dict:
            text_block_dict[text_block].append(record)
        else:
            text_block_dict[text_block] = [record]
            
    if not trigger_set_found:
        print("%s did not have trigger text %s" % (student, ' '.join(trigger_set)) )
            
    return text_block_dict