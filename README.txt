*** This submission is for Yobota's challenge ***

_There are several clarifications that I would like to mention_

1. HOW TO RUN

After downloading the repository, in order to run the file 'connectz.py', you have to install the "sys" package.

Then, please make sure that you have your data file within the directory folder before running the file 'connectz.py' or you have to type the input path where you store the data (for example: "home/data.txt") when the programme asks for it.

Please refer to 'ConnectZ.pdf' for output example for each case.

'connectz.py' was written under Python3.7.

2. EXPLAINATION

The basic logic behind this solution was:

- 1. Create a virtual playing board as a X by Y zero matrix.

- 2. Scan data for each player's information, then fill the move into the board after it satisfies all the conditions expected. If there is no data left to scan, STOP and return the result.

- 3. Scan around the latest move for the solution.

- 4. If found, STOP and return the result.
	Else GO TO 2

3. EXTRA

The file 'test_connectz.py' is used to test fuctions within 'connectz.py' using 'unittest'.
