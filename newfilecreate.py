import os
import shutil


def move(pathold, pathnew):
    '''exacte path naar file, ook naar destination file'''
    shutil.copyfile(pathold, pathnew)

move(r'C:\Users\tomcl\Documents\Offertes\offerte.xlsx', r'C:\Users\tomcl\Documents\Offertes\Dir\offerte2.xlsx')