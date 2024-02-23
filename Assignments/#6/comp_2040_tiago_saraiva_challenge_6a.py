
"""
This program reads a text file and overwrites one line

@author: Tiago Saraiva
@date: 2024-02-07
"""


def find_aqua():
    """

    Open file and reads line by line, then overwrites the file
    changing the third line, return the lines in a list.

    """
    with open('text_file.txt', 'r') as myfile:
        lines = myfile.readlines()
       
    with open('text_file.txt', 'w') as myfile:
        for line in lines:
            if line.strip() == 'Aqua #00ffff':
                line = line.replace('Aqua #00ffff', 'Azure #007fff')
            myfile.write(line)   
    return lines


# Call the function and overwirtes the file
find_aqua()

# Display the return showing the file in a list
print(find_aqua())
