import sys
import csv

def convert(string):
    """convert a string to a list where each character is an element

    Parameters:
    string (str): The string to convert into a list

    Returns:
    list: the string converted to a list

   """
    list1 = []
    list1[:0] = string
    return list1

def printMatrix(matrix):
    """Print the matrix for debugging purpose.

    Parameters:
    matrix (list): It is a two-dimensional matrix in which its 
    first column and row contain strings and the rest contain integers.

    Returns:

   """
    longestNumberOfSpaces = len(str(matrix[len(matrix)-1][1])) if len(matrix) > len(matrix[0]) else len(str(matrix[1][len(matrix[0])-1]))
    spacing = longestNumberOfSpaces / 2 if longestNumberOfSpaces % 2 == 0 else (longestNumberOfSpaces+1) / 2

    print("------------------------------------", end="")
    for i in range(len(matrix)):
        print("")
        for j in range(len(matrix[0])):
            print(" " * int(spacing+(longestNumberOfSpaces - len(str(matrix[i][j])) ))+str(matrix[i][j]), end="")
    print("\n------------------------------------")
    
    
def NeedlemanWunschBackTracking(matrix, str1, str2, gapPenalty):
    """Calculates the "Biological Sequence Alignments" passing it as a parameter a matrix
    with its respective values already calculated. It is located in the last row and in
    the last column to start the "Backtracking" process. For each cell it calculates the
    scores of its neighboring cells to its left, above and diagonally above to the left.
    The way to calculate these scores are as follows:

    leftCellScore = the score of that cell + gap penalty
    upCellScore = the score of that cell + gap penalty
    diagonalCellScore = the score of that cell + 1 if the
    letters in that column and row match or -1 if they don't match

    The direction in which it will move is towards the cell with the highest score. If the
    direction is up, a gap (-) is added to the word found horizontally in the matrix at the
    letter position of that column. If the direction is to the left, a gap (-) is added to
    the word found vertically in the table at the letter position of that row. If there is
    a tie between the diagonal and one of the other two, the one on the left or above is
    prioritized. In the same way that if there is a tie between the 3, either the one on top
    or the one on the left is chosen. If during this path tracking the position of the cell that
    we are analyzing reaches the first column or row (those that contain only the multiple
    values of the gap penalty) then gaps (-) will be added until it reaches the cell that
    It is higher to the left of the matrix. Taking into account what was mentioned before.
    If it moves to the left the gap goes to the word in the column and if it moves up the
    gap goes to the word in the row.

    Parameters:
    matrix (list): It is a two-dimensional matrix in which its 
    first column and row contain strings and the rest contain integers.
    str1 (str): is the first string words to make the "Biological Sequence Alignments"
    str2 (str): is the second string words to make the "Biological Sequence Alignments"
    gapPenalty (int): is a constant value
    
    Returns:
    list: a list with three elements:
    first element: it is the first string with the "Biological Sequence Alignments" already made
    second element: it is the second string with the "Biological Sequence Alignments" already made
    third element: It is the total score of those two strings. It is what indicates that so much alike they had.

   """
    lstr1 = []#The results will be saved here
    lstr2 = []#The results will be saved here
    i = len(matrix)-1
    j = len(matrix[0])-1
    
    while  not (i == 1 and j ==1) :#It stops only when it reaches exactly index i = 1, j = 1
        
        #in case it reaches the first column or row 
        #(those that only contain the initial numbers
        #that are multiples of the gap penalty)
        
        if(i == 1 and j != 1):#base case for the first row
            lstr1.insert(0,"-")
            lstr2.insert(0,matrix[0][j])
            j = j-1
            continue
        if(i != 1 and j == 1):#base case for the first column
            lstr2.insert(0,"-")
            lstr1.insert(0,matrix[i][0])
            i = i-1
            continue
        
        #The scores of the 3 neighbors are calculated
        leftScore = matrix[i][j-1] + gapPenalty
        upperScore = matrix[i-1][j] + gapPenalty
        diagonalScore = matrix[i-1][j-1] + (1 if matrix[i][0] == matrix[0][j] else -1)
        
        #moves to the one with the highest score
        if(leftScore >= diagonalScore and leftScore >= upperScore): #leftScore >= others
            lstr1.insert(0,"-")
            lstr2.insert(0,matrix[0][j])
            j = j-1
        elif(upperScore >= diagonalScore and upperScore >= leftScore): #upperScore >= others
            lstr1.insert(0,matrix[i][0])
            lstr2.insert(0,"-")
            i = i-1
        elif(diagonalScore >= leftScore and diagonalScore >= upperScore):#diagonalScore > others
            lstr1.insert(0,matrix[i][0])
            lstr2.insert(0,matrix[0][j])
            i = i-1
            j = j-1
        
            
    return ["".join(lstr1), "".join(lstr2), matrix[len(matrix)-1][len(matrix[0])-1]]
            
            
    

def NeedlemanWunschInitialMatrix(str1, str2, gapPenalty):
    """Fill the matrix with the initial values to be able to do the Backtracking
    process. Iterates through each row from top to bottom and for each row (list)
    iterates through its elements (columns). The first row and the first column
    contain the words to make the "Biological Sequence Alignments" in the form of
    lists in which each character is an element. The process of filling the table
    is as follows:

    The first row and column after the row and column containing the words will
    contain increments of twice the gap penalty starting at 0 going left to right
    and top to bottom. After that, each cell will be filled with the largest number
    of 3 calculations that will be made for each cell, which are:

    first number: the number of the cell that is on the top left is chosen and
    1 is added if the letters in that row and column match, if not -1 is added.

    second number: choose the number of the cell on the left and add the gap penalty.

    third number: the number of the cell above is chosen and the gap penalty is added.

    An example matrix would look like this:
    
                 G    T    C    G    A...
            0   -1   -4   -6   -8   -10     
        G  -2    1   -1   -3   -5   -7  
        A  -4   -1    0   -2   -4   -4 
        T  -6   -3    0   -1   -3   -5
        T  -8   -5   -2   -1   -2   -4
        A  -10  -7   -4   -3   -2   -1  
        C  -12  -9   -6   -3   -4   -3 
        A  -14  -11  -8   -5   -4   -3   
        
    

    Parameters:
    str1 (str): it is the first string with the "Biological Sequence Alignments" already made
    str2 (str): it is the second string with the "Biological Sequence Alignments" already made
    gapPenalty (int): is a constant value

    Returns:
    list: returns the matrix with the values ready to do the backtracking process

   """
    lstr1 = [" "] + convert(str1)#str1 is the vertical word in the table
    lstr2 = [" ", " "] + convert(str2)#str2 is the horizontal word in the table
    
    l = []
    for i in range(len(str1)+2):#Each iteration add a list (row)
        if i == 0:
            l.append(lstr2)
            continue
        else:
            l.append([lstr1.pop(0)])
        for j in range(1, len(str2)+2):#Each iteration adds a number to the row
        
            #Initial values that are in the first row and only depend on the gap penalty and the column number.
            if i == 1:
                l[i].append((j-1) * gapPenalty)
            #Initial values that are in the first column and only depend on the gap penalty and the row number.    
            elif j == 1:
                l[i].append((i-1) * gapPenalty)
            #We are neither in the first row nor in the first column. Add the largest number of:
            #1.leftScore + gapPenalty
            #2.upperScore + gapPenalty
            #3.diagonalScore + 1 if the letters match else -1
            else:
                l[i].append(max(l[i-1][j-1] + (1 if l[i][0] == l[0][j] else -1) , l[i-1][j] + gapPenalty, l[i][j-1]+gapPenalty))

    return l
                
                


def NeedlemanWunsch(str1, str2, gapPenalty):
    """The Needleman–Wunsch algorithm is an algorithm
    used in bioinformatics to align protein or nucleotide sequences.

    Parameters:
    str1 (str): the first sequence of protein or nucleotide
    str2 (str): the second sequence of protein or nucleotide 
    gapPenalty (int): is a constant value

    Returns:
    str: returns a string containing the Biological Sequence Alignments
    and its score as follows: "firstSequence secondSequence score"
   """
    l = NeedlemanWunschInitialMatrix(str1,str2,gapPenalty)
    #printMatrix(l) #uncomment to see the tables
    l2 = NeedlemanWunschBackTracking(l, str1, str2, gapPenalty)
    
    return l2[0] + " " + l2[1] + " " + str(l2[2])
    

def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                if not row[0].startswith("sequence"):
                    print(NeedlemanWunsch(row[0],row[1],-2))
                    
                
main()    