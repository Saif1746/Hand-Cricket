 Hand Cricket

### Video Demo:
[Watch the demo here](https://youtu.be/neuEXquIhxE)

---

## Game Description:

Hand Cricket is a traditional game that has long been a favorite pastime among school children during breaks and leisure periods. The game is played between two players, each using hand signs to represent numbers between 1 and 9. The simplicity of the game, combined with its competitive nature, makes it an entertaining and engaging experience.

This Python program is an implementation of Hand Cricket, providing an opportunity to enjoy this classic game in a virtual format.

---

## Rules of the Game:

The rules for Hand Cricket are straightforward:

1. *Toss*: The game begins with a toss to decide which player gets to choose whether to bat or bowl first.
   
2. *Gameplay*: 
    - The player who bats enters a number between 1 and 9 (representing runs) in each turn.
    - The bowler also selects a number between 1 and 9. However, the bowler's goal is not to score but to take a wicket by matching the batsman's number.
    - If both players choose the same number, the batsman is declared out, and the innings ends.

3. *Innings*:
    - The game consists of two innings.
    - After the first innings, the players switch roles. The previous bowler becomes the batsman, and vice versa.
    - In the second innings, the new batsman must try to beat the score set by the first batsman without getting out.

4. *Winning*: 
    - The player who scores more runs at the end of both innings is declared the winner.

---

## Code Explanation:

The program is organized into six functions, including the main() function, which controls the flow of the game and manages input and gameplay decisions.

### 1. *main()*:
   - The main() function handles user input for the initial toss and passes the input to the toss() function. Based on the toss outcome, it determines which player (human or system) will bat or bowl first.

### 2. *toss()*:
   - This function simulates the toss, with the winner getting the opportunity to choose whether to bat or bowl first. 

### 3. *batorball()*:
   - The batorball() function determines the player's choice (bat or ball) and directs the game accordingly by invoking the respective functions bat() or ball().

### 4. *bat()*:
   - The bat() function simulates the batting phase. It takes an optional argument, sysscore, which is passed during the second innings when the player needs to beat the system's score. In the first innings, no argument is required since no target score is set.
   
   - The player inputs a number representing their runs, and the game continues until the player is "out" (i.e., the bowler matches their number).

### 5. *ball()*:
   - The ball() function mirrors the bat() function, but this time for the system's batting and the player's bowling. The goal for the bowler is to prevent the system from scoring more than the player's runs. The function takes an optional userscore argument, which is passed during the second innings when the system attempts to beat the player's score.

### 6. *getnum()*:
   - This utility function handles input validation, ensuring that only numbers between 1 and 9 are accepted as valid runs. It helps to prevent erroneous inputs and maintain the smooth flow of the game.

---

### How the Game Works:

1. *Toss*: The game begins with a toss, where the player can choose between heads or tails. The outcome of the toss is determined randomly, and the winner can choose to bat or bowl first.

2. *Batting and Bowling*:
   - The player batting enters a number between 1 and 9. This number is added to their score unless the bowler selects the same number, in which case the batsman is out.
   - The player bowling selects a number as well, but their goal is not to accumulate runs but to "take a wicket" by matching the batsman's number.

3. *Innings*: After the first innings, the players switch roles. The player who batted now bowls, and vice versa. In the second innings, the new batsman must score more than the target set by the first batsman to win.

4. *Winning the Game*: The game ends when both innings are complete, and the player with the higher score wins.

---

This program is a fun and simple way to relive the joy of playing Hand Cricket, bringing a nostalgic game into the world of programming. Whether you're a beginner learning Python or an experienced coder, this project serves as a great example of how to combine game logic with basic programming concepts.