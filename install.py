#!/usr/bin/env python

import os

if __name__ == '__main__':
    working_directory = os.path.dirname(os.path.realpath(__file__))
    home_directory = os.path.expanduser('~')
    for each in os.listdir(working_directory):
        if os.path.isfile(each) and each.startswith('.'):
            full_file_path = os.path.join(working_directory, each)
            link_path = os.path.join(home_directory, each)
            cmd = 'ln -sf {} {}'.format(full_file_path, link_path)
            print(cmd)
            os.system(cmd)
