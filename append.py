import os

file = input('Main Wordlist: ') # main file
new = input('File to add to main: ') # second file

def get_diff(mFile, nFile): # check for differnce
    os.system("diff -u " + mFile + " " + nFile + "| grep '^\+' | sed -E 's/^\+//' > Diff.txt") #get difference and output to file
    with open('Diff.txt', 'r') as fin: #open diff list(list containing differnces in files)
        data = fin.read().splitlines(True) #read list
    with open('Diff.txt', 'w') as fout: #open list in write mode
        fout.writelines(data[1:]) # removes any uneccesary text    
    fin.close() #close read
    fout.close() # close write
    apend_new(mFile) # call append


def apend_new(mList): # append differnce
    List = open(mList, 'a') # open main file in append mode
    DiffList = open('Diff.txt', 'r') # open list in read mode
    List.write(DiffList.read()) # write differnce to main file
    List.close() # close main file
    DiffList.close() # close main file
    os.system('rm Diff.txt') # deletes diff list

get_diff(file, new) # call get diff