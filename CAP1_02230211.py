####################################
#Dawa Wangdi
#First Year, Instrumentation and Control Enginnering
#02230211
####################################
#REFERENCES
#https://www.w3schools.com/python/python_tuples.asp
#https://www.geeksforgeeks.org/python-programming-examples/
#https://stackoverflow.com/questions/32293947/assistance-on-python-rock-paper-scissors-using-input-file?newreg=747149a1330a46c5a1699c21443093a3

################################
#SOLUTION
#YourSolutionScore: 50055
#input_1_cap1.txt
################################


def read_game_data(file_path):    
    # defines a function named read_game_data that takes one parameter: file_path.
    # represents the path to the input file containing game data.
    game_rounds = []
    #initializes an empty list named game_rounds.

    with open(file_path, 'r') as file:
        #Opens the file specified by file_path in read mode ('r') and assigns it to the variable file.
        #The `with` statement ensures automatic file closure, even in case of exceptions.
        for line in file:
        #This line iterates over each line in the opened file.    
            
            opponent_turn, outcome = line.strip().split() 
           #It removes any leading or trailing whitespace from the line.  strip.()
           #splits the line into two parts based on whitespace. split.()
           #assigns the first part to the variable opponent_play.
           #Iassigns the second part to the variable outcome.
            game_rounds.append((opponent_turn, outcome))
            #adds a record of a game round, including the opponent's move and the outcome, to the game_rounds list.
    return game_rounds #function returns a list (`game_rounds`) containing the extracted game data.
def calculate_score(game_rounds):
 #defines a function named calculate_score that takes one parameter: game_rounds, which is a list of tuples representing game rounds data.
    
    score = 0 #initializes a variable score to 0, which will be used to store the total score calculated from game rounds.
    
    
    for opponent_turn, outcome in game_rounds:
     #checks if the opponent's play is "A", "B", or "C"
     #And calculate the score based on outcome
  
        if opponent_turn == "A": 
            round_score = 3 if outcome == "X" else (4 if outcome == "Y" else 8)
        elif opponent_turn == "B":
            round_score = 1 if outcome == "X" else (5 if outcome == "Y" else 9)
        else:
            round_score = 2 if outcome == "X" else (6 if outcome == "Y" else 7)
            
        
        score += round_score
    return score ##Add the round score to the total score.



input_file_path = read_game_data('input_1_cap1.txt')
#Calls the function read_game_data() and passes the string 'input_1_cap1.txt'(file) as an argument.


total_score = calculate_score(input_file_path)  
#It calls the function and calculate the total score using the function and store it in 'total_score'.


print("Total Score:",total_score)  #Prints the total score calculated from the game data.