# Battleships

This is based on the classic boardgame of the same name. The player will challenge the computer in a head to head game and whoever destoy their opponents fleet wins.

Players must place their ships manually on the game board, the computers game board is automatically created and hidden from the player. 

When all boards are ready the battle begins, a players guesses board is displayed showing their previous guesses and the players board is also shown.

The ste is created using Python and displays the skills i have learnt during the Pythonmodule.

### Live site

Please see my live site below, this was deployed using [Heroku](https://id.heroku.com/login):

[Battleship game](https://battleship-game-python-project.herokuapp.com/)

## User Experience (UX)

**User Stories**

### Planning

When planning the game I created a flow chart to get an understanding of how I wanted my game to work using OOP. This was created to get a basic flow of the games logic and during the development of the game I relaised I needed more functions to solve the bugs I was encountering.

![Flowchart](https://user-images.githubusercontent.com/79532281/162234360-0594996b-f696-4f2a-8ea8-c2c9f578598d.png)


## Features

#### Arrival Menu

When the player opens the site they are greated with the games header and below text asking do they want to play the game(p) or instructions on the games(i)
If the player selects **p** they are taking to a new screen and asked to input their name. If the select **i** they are taken to a new screen and the games rules and game legend are displayed.

![home screen](https://user-images.githubusercontent.com/79532281/162566809-a3d2e585-8a8e-4c59-91b2-ea0ae7ced5f7.png)

#### Instructions screen.

**How to play**

On this screen the user is shown the steps needed to play the game, how to place their battleships, if they hit or miss and finally how you win the game. 

![how to play](https://user-images.githubusercontent.com/79532281/162566884-67594775-1ec3-47a2-83be-ca0a3086a935.png)

**Legend**

This gives the user a description of what each icon means on the game board so when they play the game they can understand what they are looking at.

![Legend](https://user-images.githubusercontent.com/79532281/162566938-8748688e-1387-4813-a228-21e07d0f9eb1.png)

#### Welcome Message

After the user selects **p** to play they game they are taking to a new screen and asked to enter their name. The player must enter a name or else they will get the below warning message. The player also cannot enter **computer** as their user name as the computer knows this is their name and won't let anybody steal it.

![no name entered](https://user-images.githubusercontent.com/79532281/162567284-814fe4b5-3be6-491c-98c5-e93bc8883ffc.png)

![computer name](https://user-images.githubusercontent.com/79532281/162567287-8289e252-6080-49e2-87ba-d2ea68bbbaed.png)

### Future Features

Below are the features I would like to implement into the game when I learn more about Python:

**Display ships on board**

I would like to discplay an icon for each ship to appear on the gameboard, for example if the ship is a Carrier then C would appear on the board and would appear over 5 spaces to match the vessel length. After a ship is sunk I would like a message to appear letting you know ship type sunk, "Well done, you have sunk {ship.type}"

**Display Gameboards Side by Side**

I would like for the gameboards to appear side by side. This will stop the user from having to scroll up to look at the game board where the computer has attacked and provide a better UX.

**Better computer AI**

I would like to increase the computers AI when attacking. If the computer hits the players board, I would then like the computer to attack the positions around the hit until they sink a ship. Currently if the computer gets a hit, it's next attack is a random position. This will make games more challenging for the players and improve the UX.

## Technologies Used


## Testing 

### Bugs Found

**Gameboard**

When creating the gameboard I came across the below bug. The bottom row of the grid was out of sequence with the rest of the board and didn't provide the positive UX.

![game board bug](https://user-images.githubusercontent.com/79532281/162245500-1682d231-52fb-4529-801e-e27d2535cd6b.png)

To solve the issue, in my function ```print_board``` I added spacing to any row number less than 10, the idea behind this is the same as adding padding in CSS.

![board bug code](https://user-images.githubusercontent.com/79532281/162247201-8404c09d-6bb8-4fbf-a726-7cc705f94050.png)

This fixed the layout issue on the board and now the layout is uniformed.

![final board](https://user-images.githubusercontent.com/79532281/162246532-68e83cc1-8c80-4b4c-902d-87fa46f8e939.png)

### Bugs not fixed

When playing the game on Heroku I cannot clear the screen totally during the firing rounds. A bit of the old board carry over on every turn. I tried to clear the console at various points throughout the game to try and fix it but no luck with it. To solve this issue, I added a Battleship heading at the top of the boards to break up the space between the boards.

![heroku bug](https://user-images.githubusercontent.com/79532281/162592570-d0e26d57-1119-4ab7-8890-fc720ccdcc62.png)

## Deployment

### Making a Local Clone

1. Log into GitHub and locate the GitHub repositary you want to clone.
2. Open the respositary and under it's name click "Code"
3. To clone, under "HTTPS" copy the link.
4. Open your Gitpod terminal.
5. In the terminal type in ```git clone``` and the repositarys name:

     ![git clone](https://user-images.githubusercontent.com/79532281/162242570-7a6029c1-11da-469c-99b8-4b0d6f8ea7f1.png)
6. Press enter and your clone will be created:
     ![git clone 2](https://user-images.githubusercontent.com/79532281/162243069-6abe04aa-ff12-4825-9841-3c7533473ed7.png)
     
     ![git clone 3](https://user-images.githubusercontent.com/79532281/162243138-b50b3fa1-2030-4c97-991b-fd4c447721cd.png)



### Deploying to Heroku

The project was deployed to Heroku using the following steps:

1. Log in to [Heroku](https://id.heroku.com/login) and if not taken there automatically, navigate to your personal app dashboard.
2. At the top of the page locate the 'New' drop down, click it and then select 'Create new app'.
3. Give your application a unique name, select a region appropriate to your location and click the 'Create app' button.
4. Your app should now be created so from the menu towards the top of the page click 'Settings'
5. Click 'Reveal Config Vars' in the Config vars section and enter the key as PORT and the value as 8000. Click the Add button.
6. Under the 'Buildpacks' section click 'Add buildpack'.
      * Select 'Python' and then click the 'Save changes' button.
      * Click 'Add buildpack' again, select 'nodejs' and click the 'Save changes' button again.
      * Ensure the build packs are ordered as below:
  
          ```heroku/python```
    
          ```heroku/nodejs```
7. Navigate to the 'Deploy' page using the menu towards the top of the page.
8. Select 'GitHub' from the 'Deployment method' section and you will be prompted to 'Connect to GitHub'.
9. Once connected to your GitHub account you will be able to search for your repository which contains the battleships code.
10. Once the repository is found click 'Connect'.
11. At the bottom of the page find the section named 'Manual deploy', select the 'main' branch in the drop down and click the 'Deploy' button.
12. Once deployment is complete, click the 'View' button to load the URL of the deployed application.


## Credits

* [Black Playground](https://black.readthedocs.io/en/latest/)
     * I used Black Playground to ensure my code was indented correct to meet PEP8 standards.

* [Patorjk](https://patorjk.com/software/taag/#p=display&f=Ivrit&t=Battleships)
     * To create the headers used for Battleship and instructions menu.

* [Lucid](https://lucid.co/)
     * I used Lucid to create my Flowchart.

* [Heroku](https://id.heroku.com/login)
     * For deplyment of the live site

* [Stack overflow - clear_console](https://stackoverflow.com/questions/2084508/clear-terminal-in-python)
     * Used to create clear_console.

* [Stack overflow - Python](https://stackoverflow.com/search?q=battleships+python&s=87361546-624c-486c-98c9-d8a5cd81f924&s=b0c77bec-adf6-4812-932e-c25b8b2cc5ed)
     * Also used Stackoverflow to get guidence on creating my code.

* [Pythondex](https://pythondex.com/python-battleship-game)
     * Also used for guidence creating my game. Idea for creating variables and calling into functions in board.py was taken from here.

* [PEP8](http://pep8online.com/)
     * Used to check code and no errors appearing.![attack computers board]


