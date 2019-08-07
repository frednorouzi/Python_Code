## Summary of Part One
### – Stock Market Prediction Model:
This part of project represents stock trading by using supervised Machine Learning with SVM (Support Vector Machine) approach in Python.  In order to create model, I gather one-year historical data of the ticker 'GE' as a sample data and fit to linear and Radial Basis Functions (RBF) regression models for predicting future values. Then train SVC classifier algorithm with the regime to predict the current day’s trend at the opening of the market. And finally visualize the performance of this strategy on the test data.
For implement this program we need following necessary package and libraries to import:                                                      Time, csv, numpy, matplotlib.pyplot, and from sklearn.svm import SVR
![alt tag](https://github.com/frednorouzi/Python_Code/master/Capture_Result_Project1.JPG)

## Summary of Part Two 
### – GUI Programing of Connect Four Game:
The program enables two players to place red and yellow disks in turn.  To place a disk, the player needs to click on an available cell.  An available cell is unoccupied and its downward neighbor is occupied. The program flashes the four winning cells if a player wins, and reports no winners if all cells are occupied with no winners. This program include two classes that named “Board” which it is subclass of Canvas (GUI part of program) and “ConnectFour”. 
Also I created simple image for represent a square with a circle that named connect_four_small. 
Board class include createToken and dropToken methods respectively  creates a disk with specified color and column and next method which iterates moving the disk drop down in the correct place.
ConnectFour class contains seven methods including:
makeSelection: If the user clicks on an available space, a token is dropped into that column.
isWinner: Checks if there is a winner.  If so it sets gameOver to True, displays a message for the users, turns the winning tokens turquoise, and returns true. Otherwise, it returns false.
moreSpace: Checks if the game board is completely filled.  If it is, gameOver is set to True and a message is displayed to the users.
Reset: This method resets everything so play can begin again.
checkRows: Checks for four-in-a-row. Returns a list of [row, column] lists if there are four-in-a-row. Otherwise, it returns the empty list.
checkColumns: Checks for four-in-a-column. Returns a list of [row, column] lists if there are four-in-a-column. Otherwise, it returns the empty list.
checkDiagonals: Checks for four-in-a-diagonal.  There are two types of diagonals, so it checks them individually. Returns a list of [row, column] lists if there are four-in-a-diagonal. Otherwise, it returns the empty list.

