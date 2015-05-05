'''
Created on Jun 12, 2014

@author: James
'''

import glob
import os
# a script that converts word file to txt files
# requires word application on Windows machine
# requirement:
#    1. Windows platform
#    2. python 2.7
#    3. pywin32, download from http://sourceforge.net/projects/pywin32/
#    4. word application installed on running machine
from win32com.client import constants, Dispatch
import pythoncom
from zipfile import ZipFile


def pdf_to_text(file_path):
    import pdf2txt
    
    (outpath,ext) = os.path.splitext(file_path)
    outfile = outpath + '.txt'
    
    print(os.path.abspath(outfile))
    if os.path.exists(outfile):
        return text_from_txt_file(outfile)
    
    outfile =  os.path.abspath(outfile)
    file_path =  os.path.abspath(file_path) 
    pdf2txt.main(argv=['pdf2txt', '-o', outfile, file_path ])
    return text_from_txt_file(outfile)


# convert the word file to a text file.
# @arg wordapp: The word IDispatch object
# @arg wordfile: The word file name
# @returns: The txt file name
def doc_to_text(wordfile):
    wordapp = Dispatch("Word.Application")
    name, ext = os.path.splitext(wordfile)
    if ext != '.doc' and ext != '.docx':
        return None
    txtfile = name + '.txt'
    if os.path.exists(txtfile):
        return text_from_txt_file(txtfile)
    
    print txtfile
    try:
            
        wordapp.Documents.Open(os.path.abspath(wordfile))
        wdFormatTextLineBreaks = 3
        wordapp.ActiveDocument.SaveAs(os.path.abspath(txtfile), 
                                      FileFormat=wdFormatTextLineBreaks)
        wordapp.ActiveDocument.Close()
    except Exception as e:
        print("***Could not process " + wordfile + " ****")
    
    return text_from_txt_file(txtfile)
    
ConvertFunctions = {'.pdf' : pdf_to_text,
                    '.doc' : doc_to_text,
                    '.docx' : doc_to_text,
                    '.docx' : doc_to_text}

def FilesToText(folder_path, ext):
    global ConvertFunctions
    
    glob_path = os.path.join(folder_path, "*." + ext)
    files = glob.glob(glob_path)
    
    for file_path in files:
        (b, f_ext) = os.path.splitext(file_path)
        basename = os.path.basename(file_path)
        if basename[0] == '~':
            continue
        
        if f_ext.lower() in ConvertFunctions:

            convert_function = ConvertFunctions[f_ext]
            text = convert_function(file_path)
            base_name = os.path.basename(file_path)
            if base_name[0] == '~':
                continue
            
            (base_name, ext) = os.path.splitext(base_name)
            yield (base_name, text)
    
def text_from_txt_file(text_path):
    f = file(text_path, 'r')
    text = f.read()
    f.close()
    return text