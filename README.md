# Biological-Sequence
## About
In this repository I design a code following the logic of the Needleman-Wunsch algorithm. In this project, I had the opportunity to apply my dynamic programming skills and tabing approaches to develop highly efficient algorithms for genetic data processing. This experience allowed me to acquire deep knowledge in the algorithms design field such as Dynamic Programing algorithms.

## Needleman-Wunsch algorithm
The Needleman–Wunsch algorithm is an algorithm used in bioinformatics to align protein or nucleotide sequences. This algorithm first analyzes the sequences and builds a table with numbers to analyze it and make a backtracking process to find a solution to the problem.

## How the matrix is created
Fill the matrix with the initial values to be able to do the Backtrackingprocess. Iterates through each row from top to bottom and for each row (list) iterates through its elements (columns). The first row and the first column contain the words to make the "Biological Sequence Alignments" in the form of lists in which each character is an element. The process of filling the table is as follows:

The first row and column after the row and column containing the words will contain increments of twice the gap penalty starting at 0 going left to right and top to bottom. After that, each cell will be filled with the largest number of 3 calculations that will be made for each cell, which are:

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

## Backtracking process
Calculates the "Biological Sequence Alignments" passing it as a parameter a matrix with its respective values already calculated. It is located in the last row and in the last column to start the "Backtracking" process. For each cell it calculates the scores of its neighboring cells to its left, above and diagonally above to the left. The way to calculate these scores are as follows:

leftCellScore = the score of that cell + gap penalty

upCellScore = the score of that cell + gap penalty

diagonalCellScore = the score of that cell + 1 if the letters in that column and row match or -1 if they don't match

The direction in which it will move is towards the cell with the highest score. If the direction is up, a gap (-) is added to the word found horizontally in the matrix at the letter position of that column. If the direction is to the left, a gap (-) is added to the word found vertically in the table at the letter position of that row. If there is a tie between the diagonal and one of the other two, the one on the left or above is prioritized. In the same way that if there is a tie between the 3, either the one on top or the one on the left is chosen. If during this path tracking the position of the cell that we are analyzing reaches the first column or row (those that contain only the multiple values of the gap penalty) then gaps (-) will be added until it reaches the cell that It is higher to the left of the matrix. Taking into account what was mentioned before. If it moves to the left the gap goes to the word in the column and if it moves up the gap goes to the word in the row.

### Output
Next, the Code output will be displayed with respect to the in.csv file to illustrate how the biological sequence analysis techniques implemented in the "Biological-Sequence" repository are applied.
```
          C    T    A    G    C    T    A    G    C    T    A    G    C    T
     0   -2   -4   -6   -8  -10  -12  -14  -16  -18  -20  -22  -24  -26  -28
K*   -2   -1   -3   -5   -7   -9  -11  -13  -15  -17  -19  -21  -23  -25  -27
L*  -4*   -3   -2   -4   -6   -8  -10  -12  -14  -16  -18  -20  -22  -24  -26
C   -6  -3*   -4   -3   -5   -5   -7   -9  -11  -13  -15  -17  -19  -21  -23
B   -8   -5  -4*   -5   -4   -6   -6   -8  -10  -12  -14  -16  -18  -20  -22
A  -10   -7   -6  -3*   -5   -5   -7   -5   -7   -9  -11  -13  -15  -17  -19
A*  -12   -9   -8  -5*   -4   -6   -6   -6   -6   -8  -10  -10  -12  -14  -16
G  -14  -11  -10   -7  -4*   -5   -7   -7   -5   -7   -9  -11   -9  -11  -13
C  -16  -13  -12   -9   -6  -3*   -5   -7   -7   -4   -6   -8  -10   -8  -10
T  -18  -15  -12  -11   -8   -5  -2*   -4   -6   -6   -3   -5   -7   -9   -7
A  -20  -17  -14  -11  -10   -7   -4  -1*   -3   -5   -5   -2   -4   -6   -8
G  -22  -19  -16  -13  -10   -9   -6   -3   0*   -2   -4   -4   -1   -3   -5
C  -24  -21  -18  -15  -12   -9   -8   -5   -2   1*   -1   -3   -3    0   -2
T  -26  -23  -20  -17  -14  -11   -8   -7   -4   -1   2*    0   -2   -2    1
A  -28  -25  -22  -19  -16  -13  -10   -7   -6   -3    0   3*    1   -1   -1
G  -30  -27  -24  -21  -18  -15  -12   -9   -6   -5   -2    1   4*    2    0
C  -32  -29  -26  -23  -20  -17  -14  -11   -8   -5   -4   -1    2   5*    3
T  -34  -31  -28  -25  -22  -19  -16  -13  -10   -7   -4   -3    0    3    6
KLCBAAGCTAGCTAGCT --CTA-GCTAGCTAGCT 6
```
```
              T    G    A    C    C    G    C    G    T   T*
        0*   -2   -4   -6   -8  -10  -12  -14  -16  -18  -20
    X   -2  -1*   -3   -5   -7   -9  -11  -13  -15  -17  -19
    Z   -4   -3  -2*   -4   -6   -8  -10  -12  -14  -16  -18
    G   -6   -5   -2  -3*   -5   -7   -7   -9  -11  -13  -15
    T   -8   -5   -4   -3  -4*   -6   -8   -8  -10  -10  -12
    C  -10   -7   -6   -5   -2  -3*   -5   -7   -9  -11  -11
    G  -12   -9   -6   -7   -4   -3  -2*   -4   -6   -8  -10
    X  -14  -11   -8   -7   -6   -5   -4  -3*   -5   -7   -9
    K  -16  -13  -10   -9   -8   -7   -6   -5  -4*   -6   -8
    T  -18  -15  -12  -11  -10   -9   -8   -7   -6  -3*   -5
    XZGTCGXKT- TGACCGCGTT -5
 ```
```
              T   G*    C    C    C    Y    K    A   C*    G    T
        0*   -2   -4   -6   -8  -10  -12  -14  -16  -18  -20  -22
    A   -2  -1*  -3*   -5   -7   -9  -11  -13  -13  -15  -17  -19
    C   -4   -3   -2  -2*   -4   -6   -8  -10  -12  -12  -14  -16
    C   -6   -5   -4   -1  -1*   -3   -5   -7   -9  -11  -13  -15
    T   -8   -5   -6   -3   -2  -2*   -4   -6   -8  -10  -12  -12
    G  -10   -7   -4   -5   -4   -3  -3*   -5   -7   -9   -9  -11
    G  -12   -9   -6   -5   -6   -5   -4  -4*   -6   -8   -8  -10
    A  -14  -11   -8   -7   -6   -7   -6   -5  -3*  -5*   -7   -9
    G  -16  -13  -10   -9   -8   -7   -8   -7   -5   -4  -4*   -6
    T  -18  -15  -12  -11  -10   -9   -8   -9   -7   -6   -5  -3*
   G*  -20  -17  -14  -13  -12  -11  -10   -9   -9   -8   -5   -5
    A-CCTGGA-GTG TGCCCYKACGT- -5
```
```
              C    C    C    T    G    A    A    C    G    X
        0*   -2   -4   -6   -8  -10  -12  -14  -16  -18  -20
    A   -2  -1*   -3   -5   -7   -9   -9  -11  -13  -15  -17
    C   -4   -1   0*   -2   -4   -6   -8  -10  -10  -12  -14
    C   -6   -3    0   1*   -1   -3   -5   -7   -9  -11  -13
    T   -8   -5   -2   -1   2*    0   -2   -4   -6   -8  -10
    G  -10   -7   -4   -3    0   3*    1   -1   -3   -5   -7
    G  -12   -9   -6   -5   -2    1   2*    0   -2   -2   -4
    A  -14  -11   -8   -7   -4   -1    2   3*    1   -1   -3
    G  -16  -13  -10   -9   -6   -3    0    1   2*    2    0
    T  -18  -15  -12  -11   -8   -5   -2   -1    0   1*    1
    G  -20  -17  -14  -13  -10   -7   -4   -3   -2    1    0
    ACCTGGAGTG CCCTGAACGX 0
```
```
              A    T    G    G    T    A    A    T
        0*   -2   -4   -6   -8  -10  -12  -14  -16
    A   -2   1*   -1   -3   -5   -7   -9  -11  -13
    T   -4   -1   2*    0   -2   -4   -6   -8  -10
    C   -6   -3    0   1*   -1   -3   -5   -7   -9
    G   -8   -5   -2    1   2*    0   -2   -4   -6
    T  -10   -7   -4   -1    0   3*    1   -1   -3
    X  -12   -9   -6   -3   -2    1   2*    0   -2
    G  -14  -11   -8   -5   -2   -1    0   1*   -1
    C  -16  -13  -10   -7   -4   -3   -2   -1   0*
   B*  -18  -15  -12   -9   -6   -5   -4   -3  -2*
   B*  -20  -17  -14  -11   -8   -7   -6   -5   -4
    ATCGTXGCBB ATGGTAAT-- -4
```
```
              G    G    G    T    G    C    T    A    G
        0*   -2   -4   -6   -8  -10  -12  -14  -16  -18
    T   -2  -1*   -3   -5   -5   -7   -9  -11  -13  -15
    C   -4   -3  -2*   -4   -6   -6   -6   -8  -10  -12
    G   -6   -3   -2  -1*   -3   -5   -7   -7   -9   -9
    A   -8   -5   -4   -3  -2*   -4   -6   -8   -6   -8
    T  -10   -7   -6   -5   -2  -3*   -5   -5   -7   -7
    T  -12   -9   -8   -7   -4   -3  -4*   -4   -6   -8
    T  -14  -11  -10   -9   -6   -5   -4  -3*   -5   -7
    G  -16  -13  -10   -9   -8   -5   -6   -5  -4*   -4
    A  -18  -15  -12  -11  -10   -7   -6   -7   -4   -5
    TCGATTTGA GGGTGCTAG -5
```
