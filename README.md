# Battleships

This is based on the classic boardgame of the same name. The player will challenge the computer in a head to head game and whoever destoy their opponents fleet wins.

Players must place their ships manually on the game board, the computers game board is automatically created and hidden from the player. 

When all boards are ready the battle begins, a players guesses board is displayed showing their previous guesses and the players board is also shown.

The ste is created using Python and displays the skills i have learnt during the Pythonmodule.

### Live site

Please see my live site below, this was deployed using [Heroku](https://id.heroku.com/login)

## User Experience (UX)

**User Stories**

### Planning

## Features

### Future Features

## Technologies Used


## Testing 

### Bugs Found

## Deployment

### Forking a GitHub Repository

### Making a Local Clone

### Deploying to Heroku

The project was deployed to Heroku using the following steps...

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




