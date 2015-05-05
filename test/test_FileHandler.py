'''
Created on Jun 12, 2014

@author: James
'''
import os
import unittest
import copy_catcher.filehandler
import copy_catcher.metrics

class Test(unittest.TestCase):
    
    def test_PDF(self):
        pdf_name = "Brown, Patrick.pdf"
        input_dir = "..\PCP"
        pdf_full_path = os.path.join(input_dir, pdf_name)
        
        text = copy_catcher.filehandler.pdf_to_text(pdf_full_path)
        print text
        return
        
    
    def test_DOC(self):
        pdf_name = "Chan, Connie.doc"
        input_dir = "..\PCP"
        pdf_full_path = os.path.join(input_dir, pdf_name)
        
        text = copy_catcher.filehandler.doc_to_text(pdf_full_path)
        print text
        return
        
    def test_DOCX(self):
        pdf_name = "Carroll, Megan.docx"
        input_dir = "..\PCP"
        pdf_full_path = os.path.join(input_dir, pdf_name)
        
        text = copy_catcher.filehandler.doc_to_text(pdf_full_path)
        print text
        return
       
    def test_metrics(self):
        folder_path = "..\PCP"
        copy_catcher.metrics.Calculate_metrics(folder_path)



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()