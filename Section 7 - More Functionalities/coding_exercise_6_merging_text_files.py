"""
Udemy: The Python Mega Course:  Building 10 Real World Applications
Coding Exercise 6: Merge multiple text files to one.

This code contains my own solution for the exercise indicated above,
without refering to Udemy solution

Author: Jhesed Tacadena
Date: 2017-01-24

Section 7 contents:
    41. Introduction
    42. Modules, Libraries and Packages
    43. Commenting and Documenting your Code
    44. Working with Dates and Times
    45. Coding Exercise 6: Merging Text Files
    46. Tips for Exercise 6
    47. Solution 6

"""

# -----------------------------------------------------------------------------
# Imports

import os
import datetime

# -----------------------------------------------------------------------------
# Main program

def merge_files(directory="."):
    """
    Merge files inside `directory`

    Argument:
        directory (str): The directory that contains the files to be merged.

    Note:
        Output file will also be written in `directory`
    """

    file_names = os.listdir(directory)

    if directory[-1] == '/':
        # remove trailing slash, as this will be dynamically appended later on
        directory = directory[:-1]

    if file_names:
        
        print("(INFO) Files in directory: `{}`".format(file_names))
        
        # Name of the output file
        output_file_name = "{}/{}.txt".format(
            directory, 
            datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f"))

        with open(output_file_name, 'w') as output_file:
            
            # loop thru all input files in directory
            for fname in file_names:
                
                with open("{}/{}".format(directory, fname)) as input_file:
                    
                    print("(INFO) Opening file: `{}`".format(fname))

                    for line in input_file:
                        # Write to output file
                        output_file.write("{}\n".format(line))

        print("(INFO) Done merging files.")
    
    else:

        # No files exist, don't do anything
        print("(WARNING) No files in directory.")


# Stand alone test
if __name__ == '__main__':
    merge_files('res')