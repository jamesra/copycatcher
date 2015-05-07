'''
Created on Jun 12, 2014

@author: James
'''

import argparse
import sys
import os 

import filehandler
import metrics
import report

def CreateParser():
    parser = argparse.ArgumentParser(__name__)
    
    parser.add_argument('folder_path',
                        action='store',
                        default=None,
                        type=str,
                        help='Folder to check for duplicate strings'
                        )
    
    parser.add_argument('-blocksize','-s',
                        action='store',
                        default=6,
                        type=int,
                        help='Number of adjacent words in a text block.  Larger values may result in false negatives but decrease the number of results to check.',
                        dest='blocksize'
                        )
    
    parser.add_argument('-template', '-t',
                        action='store',
                        default=None, 
                        type=str,
                        help='Filename of assignment template.  Words in the template are never considered duplicates.',
                        dest='template') 
    return parser

def Execute(prog_args=None):
    
    if prog_args is None:
        prog_args = sys.argv[1:]
        
    
    parser = CreateParser()

    args = parser.parse_args(prog_args)
    
    template = None
    if not args.template is None:
        (template,ext) = os.path.splitext(args.template)
    
    #TODO: Trigger set tells the scoring system to not count blocks of text before a specific set of words in encountered in a single block.
    #However there is nosupport for this feature from the command-line yet
    trigger_set = []
    text_block_dict = metrics.Calculate_metrics(args.folder_path, args.blocksize, template, trigger_set)
    
    report.PrintNumMatchesForStudentGroups(text_block_dict)
    report.PrintSharedTextBlocks(text_block_dict)
    

if __name__ == '__main__':
    Execute()
    pass