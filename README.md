# Wordle game
For my third portfolio project with Code Institute I built a python game based on a game I play everyday, **Wordle**.

I will recreate a version of the game to be played on a Command-Line Interface (CLI) coded with python.

**Wordle** is a word game of deduction.

Players are given 6 chances to guess the 5-letter word of the day. 
With each guess, the web-based game indicates whether any of the letters used are in the word of the day and whether they are in the correct place. 
Should the player deduce the word of the day, the game tracks the winning streak as the player wins consecutive days.
If the player misses a day or fails to guess the word, the winning streak is broken and the score resets to 0.

[View the deployed webapp here](https://wordle-dasic002-367fb61feaeb.herokuapp.com/)

![Responsive design mock-up](documentation/responsive-design.PNG)


## UX - User Experience

### User stories
#### First time player
- Upon visiting the site the first time want to have the option to skip reading the intructions and proceed straight with the game.
- I want to be able to refer to the instructions mid play without losing the current state of my game.

#### An experienced Wordle player introduced to this version
- I want the gameplay to be as accurate to the offical game, this means:
  1) Appearance - the game is similar enough to the official game that it is easy to pick up.
  2) Gameplay - being able to see what guesses have been made for reference in the next guess.
  3) Stats - track my progress, I want to use this game to improve my skill in the offical game.

#### Returning player
- I want to be able to play the game on any device, be it a desktop PC or my mobile.
- Want to share my stats with friends.
- Want to be able to return to my game to resume

### Flowchart
To plan and illustrate how the game will run, I have generated this flowchart.
![Wordle flowchart](documentation/PP3-Wordle_flowchart_rev0-0.png)

### Strategy

Start with an MVP and build on desirable features, to create a simplistic, fun and addictive version of the wordle game that is easy to follow on a CLI display.

### Scope

__Must have features:__
- Word bank of 5-letter words in US english.
- Randomly select the word to guess.
- Allow player to enter up to 6 guess and provide basic feedback on letters correctly guessed, differentiating placement from inclusion.
- Reveal the selected word in case the player has not guessed the word.
- Validation on player input, that the input is:
  - 5 characters long.
  - all letters.
  - a word present in the dictionary.

__Should have:__
- Tracking of scores in the session to feedback to player.
- Invite the player to play another game.
- Clean GUI, using colours rather than symbols for feedback on guesses. Selecting colours that are as accessible for colour blind users too.
- Rules explaning how to play the game. 

__Could have:__
- Save session scores in a database to provide feedback to user on how do they compare against other players.
- Provide an optional breakdown of the player's scores.
- Resume sessions, the game could be made to allow the user to enter their given ID to resume winning streak count.
- Praise from the game matching that of wordle, which depends on how many guesses made before finding the selected word.

__Won't have:__
- Mobile phone or tablet access, the CLI does not seem to accept text entered on these devices and any solutions online don't seem straightforward or universal.

### Surface
#### Colour theme
Considering the limitations in the CLI for colour and formatting, I followed the appearance of wordle in dark mode with some consideration for accessibility for colour blind users.

Originally, the chosen colours were green for correctly guessed letters, dark purple for wrong placement of letters and grey for not existent. This provided an optimum contrast between any colour when run through a simulator.

However, the chosen colours, used an 8-bit configuration in the ANSI escape code, once the code was deployed to Heroku, the terminal did not display any of this formatting.

![Original colour selection](documentation/Adobe-color-original-colours.PNG)

Being constricted to 3-bit and 4-bit palette, it took a few deployments to test the colour the CLI would output. 

Firstly, attempted using the closest colours available, which unfortunately meant the purple/magenta available was too close to the grey being used and produced a low contrast. 

![Deployment with the available green and purple colours](documentation/purple-lacks-contrast.PNG)<br>
![Using Adobe Colour blindness tool](documentation/purple-lacks-contrast_adobe-sim.PNG)

Eventually, a version of the code was deployed that printed out all colours available so we could pick the RGB values and use Adobe Colour to see which might work best for the various types of colour blindness. It was found that the bright yellow, standard green and a darker grey was most suitable.

![Deployment printing all library colours available](documentation/testing-colour-selection.PNG)<br>
![Using Adobe Colour blindness tool](documentation/colour-selection-adobe-sim.PNG)

## Features 

### Existing Features
#### Welcome
Upon the game loading, the terminal will display a simple Heading "Welcome to Wordle", with only a prompt at the bottom of the interface for the user to enter their name. This is to keep the interface as simply and least daunting as possible before the player begins the game.<br>
  ![Welcome page](documentation/feat_welcome.PNG)

#### New game display
Once the player has input a name the terminal generates the user variables and word selection and presents the game in the CLI after clearing the welcome display away.

__Note:__ If the play simply pressed enter without entering a name, the game will use the default of "Player-1".

The display will include:
  1) a personalised message of "Welcome, _player name_".
  2) an instructions how to bring up the rules of the game.
  3) blank guess lines shown as a series of asterisks __` *  *  *  *  * `__.
  4) prompt for player to enter their guess.<br>
  
![New game displayed](documentation/feat_game_display.PNG)
  
#### Player Prompt
The game prompts the player to take a guess, provided it passes the validation checks, the game checks the input guess against the randomly selected word for this session. Every time the guess is incorrect the prompt changes to "Oops! that guess is wrong, please try again!".

![Prompt after incorrect guess]()

#### Invalid guess inputs display
To reduce frustrations over incorrect guesses we have put in place some input validations, as well as adding a `strip()` method to the guess input so should the user enter a whitespace before or after typing their word, it will not trigger the validation checks for a seemingly valid guess.

##### Invalid data: not exactly 5 characters long
This first check verifies the guess is only 5 characters long, not shorter or longer. In the chance the player enters a guess that fails this check the game prints out the game display again but with the message advising the guess was invalid and explaining why so.

![Invalid data: shorter than 5 chars](documentation/feat_invalid-short-input.PNG)

![Invalid data: longer than 5 chars](documentation/feat_invalid-long-input.PNG)

##### Invalid data: includes characters not in the alphabet
Should the guess input pass the 5 characters long verification, the next check verifies that no characters other than letters in the alphabet have been used. Should the player enter punctuation marks, numbers or other special characters, the game will refresh and display the error message explaining why the last entered guess was not valid.

![Invalid data: includes a non-alphabetic character](documentation/feat_invalid-non-alpha-input.PNG)

##### Invalid data: is not a word in the dictionary used
Finally, after passing the other checks, the last check verifies that the input is a word included in our dictionary. Should it not be included in the dictionary, it will refresh the game and advise the word is not in the dictionary.

![Invalid data: not in our dictionary](documentation/feat_invalid-not-a-word-input.PNG)

#### Clues on guesses made
The objective of wordle is that the player gets given clues on all guesses so the player can deduce what the selected word is. In our version of the game:
- Blank lines are shown as plain text asterisks ` * `.
- Letters not existing in the selected word are shown in a dark grey background - these tell the player to avoid using these letters in future guesses.
- Letters existing in the selected word but in the incorrect place are shown in a bright yellow background - these tell the player to try words where this letter is in another place.
- Letters existing in the selected word and in the correct place are shown in a green background - these tell the player to try words where this letter is as it is.

#### End of Round
The round ends when the player has either guessed the selected word or has failed to do so after 6 attempts.
##### Correct guess
On guessing the word, the terminal prints out "Nicely done, _player name_!" and confirms the word of the day.

![Game won](documentation/feat_game-won.PNG)

##### 6 Wrong guesses
On 6 failed attempts, the terminal prints out "GAME OVER", reveals the word of the day and "Oh no, _player name_! You've lost this streak!".

![Game lost](documentation/feat_game-lost.PNG)

##### Scores
In either case the game will keep track of the score, namely the consequitive number of times the player has guessed the word correctly. Should it be the maximum the player has managed to get in this session, the game will record it as a higscore. Should the player, win the game, the "Current streak" counter increments by 1, if the game was lost, it resets to 0.

The game will also calculate and display the average number of guesses the player has needed to guess the word of the day. It will also lookup the player's longest winning streak and rank the player against the other game sessions recorded.

![Game scoring](documentation/feat_game-scoring.PNG)

##### Inviting for a new game
At the end of the round, the game prompts the player for another game. If the player inputs anything but "n" or "N", a new round will start with a new word of the game. Should the player have had enough, they'll enter "n" or "N" for No to exit the game. On doing so a message thanking the player for playing will be printed out.

![Game exit](documentation/feat_game-exit.PNG)

#### Game rules display
Should the player need to be reminded of the rules, the player can enter "help!" as a guess input. This will bypass the usual validations and cause the game to print the rules on a clear terminal and request a prompt just to press 'Enter' when done with the game for when the player feels ready to resume the game.

![Rules display](documentation/feat_rules.PNG)

### Features Left to Implement
<!-- 
Wordle includes the whole keyboard in the display, highlighting which letters have not been used, which are non existing, existing or correctly placed, this helps the player visualise which letters they could use like a checklist of the alphabet and it becomes easier to try sounding out words for the next guess. We have not recreated this feature, but we could potentially use the empty space to the right of the guesses to print out the alphabet and highlighting what letters are still available to use.

Wordle includes __Hard Mode__ which tracks letters the player has guessed that exist in the selected word and should the player not use them in the next guess they attempt, wordle will not accept the entry. Should the letter be in the correct place, wordle will only accept words with the correctly guessed letters in the same places. For example, should the selected word be LIVER and the first guess be PLATE, then L and E are indicated as exiting but being in the wrong place, the second guess would need to include both L and E, so it could not be something like NERVE or LOUSY, but could be LIKED or LOVER. Should the second guess in fact be LIKED, the letters L, I and E will be indicated as correctly guessed and need to be used in the same places for the following guess, something looking like L I _ E _, which could be LIFER, LIMEN, LINEN, LINER, LIVED, LIVER just to name a few. The aim of this feature is to avoid the player trying completely different words in order to find other missing letters without the constraints of considering the words that the could work with the clues given. For instance, without __Hard Mode__ the player's second guess could be VIRUS, it doesn't include L and E that would be highlighted from PLATE, but does include V, I and R. From those 2 guesses, the player should be able to deduce that the selected word is LIVER on the third guess. If we were to implement this feature we could store the list output from the evaluation of previous guesses to evaluate whether use in a validation looking for the previously correct guessed letter placement matching that in the new guess. For letters existing in the selected word, the function evaluating guesses can output a dictionary of these letters, and the input validation check that these letters are used in the latest input before it proceeds to evaluating for the game. 

Feedback messages

logging back to a player's game -->


## Technologies
- Languages used:
  - [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Draw.io](https://app.diagrams.net/#) - a free web-based diagram drawing tool.
- [GitPod](https://www.gitpod.io/) - Cloud-based IDE to edit code and Git version control.
- [GitHub](https://github.com/) - to store and publish the project.
- [Am I Responsive](https://ui.dev/amiresponsive) - to visualise the website in various display sizes.
- [Adobe Color](https://color.adobe.com/create/color-wheel) - to generate the colour palette and Accessibility tools checking for contrast for legibility and colour-blind viewing.
- [PEP8 guide](https://peps.python.org/pep-0008/) - for guidance on python formatting standards. 
- [Code Institute's Python linter](https://pep8ci.herokuapp.com/) - to validate the Python code. 
- [Heroku](https://dashboard.heroku.com/) - for deplayment of our web app.
- [Pilestone - Color Blind Vision Simulator](https://pilestone.com/pages/color-blindness-simulator-1)

## Testing 

### Validator Testing 

- [Code Institute's Python linter](https://pep8ci.herokuapp.com/) - to validate the Python code. 
- Accessibility:
  - Adobe colour - [colour blindness](https://color.adobe.com/create/color-accessibility) - No conflicts found.<br>
  ![adobe colour - full swatch check](documentation/full-swatch-adobe-sim.PNG)
  - [Pilestone - Color Blind Vision Simulator](https://pilestone.com/pages/color-blindness-simulator-1) - visual check, seems distinguishable still<br>
  - [simulated colourblind viewing images here](documentation/simulated_colourblind/)


### Manual Testing

#### Devices and browsers used
<!-- - iPhone 12 Pro - iOS 17.5.1
  - Safari (v17.5.1)
  - Chrome (v127)
  - Google (v325)

- iPad Pro (12.9 inch - 4th Gen) - iPadOS 17.5.1
  - Safari (v17.5.1)
  - Chrome (v127)

- Dell Precision 3510 laptop - Windows 10 Pro (2H22)
  - Chrome (v126)
  - Firefox (v127)
  - Microsoft Edge (v126) -->

#### Manual testing checklist

<!-- | Feature | Action | Expected Behaviour | Pass/Fail | Notes |
|-|-|-|-|-|
|Google fonts|Loading the page|Google fonts load|PASS|
|Font awesome icons|Loading the page|Icons appear as intended|PASS|
|Images|Loading the page|images appear as intended|PASS|
|content text |Loading the page|text appears as intended|PASS|
|Nav bar appearance|Loading the page|Nav bar appears as expected, collapsed hamburger icon for narrow displays|PASS|
|Nav Button - hamburger icon|Click Hamburger icon|hamburger icon expands to reveal nav menu|PASS|
|Nav Button - hamburger icon|Click Hamburger icon|hamburger icon is replaced with an X icon|PASS|
|Nav Button - X icon|Click X icon|X icon is replaced with the hamburger/bars icon and menu collapses|PASS|
|Nav button - New Game|Click button "New Game" just after loading the site|X icon is replaced with the hamburger/bars icon and menu collapses|PASS|
|Nav button - New Game|Click button "New Game" just after loading the site|button brings up the empty player form|PASS|
|Nav button - New Game|Click button "New Game" after starting a game|button brings up the player form prefilled with players' name|PASS|
|Nav Button - How To Play|Click button "How To Play"|X icon is replaced with the hamburger/bars icon and menu collapses|PASS|
|Nav Button - How To Play|Click button "How To Play"|button brings up the instructions section|PASS|
|Nav Button - Credits|Click button "Credits"|X icon is replaced with the hamburger/bars icon and menu collapses|PASS|
|Nav Button - Credits|Click button "Credits"|button brings up the credits section|PASS|
|Page scaling - mobile|Viewing the page on mobile display in portrait|Font size is legible and the page does not require scrolling on timed buttons. No overlapping text or images.|PASS|
|Page scaling - mobile|Viewing the page on mobile display in landscape|Font size scales down to fit in the height of the display. Page includes left and right margins to keep content in the centre still.|PASS|
|Page scaling - desktop|Viewing the page on a desktop/laptop display in landscape with the browser taking the width of the display|Font size scales down to fit in the height of the display. Page includes left and right margins to keep content in the centre still.|PASS|
|Page scaling - desktop|Viewing the page on a desktop/laptop display in landscape with the browser taking the width of the display|Font size scales down to fit in the height of the display. Page includes left and right margins to keep content in the centre still.|PASS|
|PLAY button - Landing page|Click button "PLAY"|button brings up the blank Player form. Blank form fields display placeholders.|PASS|
|? Button - Landing page|Click button "?"|If menu is expanded, X icon is replaced with the hamburger/bars icon and menu collapses|PASS|
|? Button - Landing page|Click button "?"|button brings up the instructions section|PASS|
|Add bots - player form|Click add bot buttons|Adds automated bot player names and skill level, whether field is blank or got a value. Button converts to X icon.|PASS|
|Clear bot - player form|Click the X button in place of add bot button|Clears the adjacent field and bring it to focus ready to type a name.|PASS|
|Gameplay - "Start Game" - player form|Click "Start Game" button with empty fields|Sets up game with assumed values, 1 human player ("player 1") and 3 bot players. Prompts first human player and presents bot player actions.|PASS|
|Gameplay - "Start Game" - player form|Click "Start Game" button with human names in fields|Sets up game limiting the player names to 8 characters long. Prompts next human players and presents actions from any bot players included.|PASS|
|Gameplay - "READY" - player prompts at start of round|Click "READY" button with on player prompt|Brings player to shuffle hand|PASS|
|Gameplay - Selecting to shuffle hand - player hand|click one card|Highlights the card|PASS|
|Gameplay - Selecting to shuffle hand - player hand|click another card|Highlights the 2nd card for a brief moment and removes all highlights|PASS|
|Gameplay - Selecting to shuffle hand - player hand|click another pair of cards|repeats the same highlighting behaviour indefinitely until player presses done|PASS|
|Gameplay - Selecting to shuffle hand - player hand|click one card and then select "Done"|Highlights the card, but clicking Done removes highlight and ignores it|PASS|
|Gameplay - Count down to reveal bottom 2 cards - player hand|Click "DONE"|Page displays text "Ready…" and adds "3," "2," and "1!" revealling the bottom 2 cards for 1 second. Once cards are face down again, the knock button appears and counts down before disappearing and prompting the next human player again.|PASS|
|Gameplay - "READY" - player prompts mid round play|Click "READY" button with on player prompt|Brings player to pick a card|PASS|
|Gameplay - Picking a card from table view|select from discard stack or from draw stack|Isolates and enlarges card selected and offer reject and accept buttons|PASS|
|Gameplay - Rejecting a picked card|after picking a card, reject the card|if from discard stack, display returns to regular table view. If from draw stack, displays message saying the card is being discarded and presents the knock button with countdown before prompting the next human player.|PASS|
|Gameplay - Accepting a picked card|after picking a card, accept the card|displays player's card hand to select the card swapping out.|PASS|
|Gameplay - selecting a card from hand to swap out|select a card from hand to swap with|displays card face of selection with heading of card being discarded,  and presents the knock button with countdown before prompting the next human player.|PASS|
|Gameplay - Last action by player displayed in player prompt|result from discarding or swapping a card|The action taken is displayed correctly in the next player prompt|PASS|
|Gameplay - Bell icon next to knocking player name|click the knock button on a mid round turn|Provided there is a human player before it reaches the knocking player's turn, a bell icon is visible next to the knocking player's name. |PASS|
|Gameplay - Ending the round on first turns|click the knock button on a first turn|A human player knocking on their first turn of the game ends the round immediately, presents the table with all cards revealled and scoring added. A Bot player knocking on their first turn should still prompt the human player to have their first turn before prompting again that for the end of round.|PASS|
|Gameplay - "READY" - player prompts at end of round|Click "READY" button on player prompt|Brings player to table view with cards revealed, scores, icons and round outcome. If any of the players have reached 200pts or more, it should announce the end of the game, otherwise it’s end of round.|PASS|
|Gameplay - "Next Round" - end of Round|Click "next round" button|Prompts next human player as normal, displaying any actions taken by bot players that follow the dealer player of the round. The game remember the names and scores from the last round, but the cards have been freshly shuffled and dealt.|PASS|
|Gameplay - "Next Game" - end of Game|Click "next game" button|Brings player back to the player form prefilled with player names|PASS|
|Instructions - Navigating|Click left or right|Will navigate back and forth through the pages. Clicking left on pg 1 or right on the last page should roll around to the other end (1 backwards to 10 or 10 forwards to 1)|PASS|
|Instructions - closing|Click the X between the arrows|How to play section closes and resumes to whatever stage the gameplay is at.|PASS|
|Credits - closing|Click the X button near the bottom|Credits section closes and resumes to whatever stage the gameplay is at.|PASS|
|Credits - links|Click links for the GitHub repository or the WhatsApp Business|Either links will open in a new tab or open the relevant app should the visitor have the app on their phone whilst visiting from their phone.|PASS|
|Error 404 page|Enter non-existing url for the site|Calls up custom 404.html|PASS|
|Error 404 page|Click on the Home button|Brings viewer back to main page|PASS| -->



### Bugs

- __ANSI escape 8-bit colours not visible on Heroku - FIXED__<br>
Heroku allows for colours in it's app, but these are restricted to 3-bit and 4-bit, so have selected colours from that selection instead.

- __Dictionary includes words with the character "ƒ" - FIXED__<br>
This character appeared on words that should have ended with an accented e (é), like __sauté__. For ease of playing the game this character has been replaced with a plain "e".


## Deployment as a Heroku app

1) Login to Heroku.
2) Once on the dashboard, click _"New"_ and select _"Create new app"_ from dropdown list.
3) Select the applicable region for your app. In our case, it's _Europe_.
4) Give the app a name. _NOTE:_ the form will advise if the name is unique and therefore available.
5) Once a suitable name has been given, click _"Create app"_.
6) You should be directed to the __"Deploy"__ tab of the app. Here you'll see a __"Deployment method"__ section, select __"GitHub"__.
7) Another section should reveal __"Connect to GitHub"__, if you have connected your GitHub account, you should see your account listed and search bar to find the repository to deploy from. Click __"Search"__ and click __"Connect"__ on the correct repository listed below.
8) Before we proceed with deployment further, we need to navigate to the __"Settings"__ tab.
9) Expand Config Vars by clicking __"Reveal Config Vars"__, and add a key of `PORT` with a value of `8000`.
10) If your project contains credentials to access secure data, you'll need to add another Config Var, add a key of `CREDS` and paste the JSON content as the value.
11) Next, we need to add two buildpacks, note the order is __important__, select and add buildpack as follows:

1. `heroku/python`
2. `heroku/nodejs`

12) Navigate back to the __"Deploy"__ tab, scroll down to __"Manual deploy"__, select the appropriate branch and click __"Deploy Branch"__. This step take short while for the server to compile the code and dependencies for the app.

To view the deployed app, scroll to the top and click "Open app".

The deployed app can be found [here.](https://wordle-dasic002-367fb61feaeb.herokuapp.com/)

### Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.


### Branching

<!-- This current branch, is the main branch being submitted for grading, it only differs from the pre-submission-archive branch in that it holds no debug code in the JavaScript file. -->


## Credits 

### Media
- [Am I Responsive](https://ui.dev/amiresponsive) - to visualise the website in various display sizes as the preview used in this readme file.
- [Pilestone - Color Blind Vision Simulator](https://pilestone.com/pages/color-blindness-simulator-1) - used to generate the view of colour blind conditions of the CLI based game.

### Code

- Reference for clearing the screen in python - [Clearing Screen in Linux Operating System](https://www.geeksforgeeks.org/clear-screen-python/)
- Reference for multiline string to print "pages" - [Multiline Strings](https://www.w3schools.com/python/gloss_python_multi_line_strings.asp)
- Reference for readlines() method to list words - [readlines() Method](https://www.w3schools.com/python/ref_file_readlines.asp)
- Validating input - [Love Sandwiches - Validating our data part 1](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+LS101+1/courseware/293ee9d8ff3542d3b877137ed81b9a5b/c92755338ef548f28cc31a7c3d5bfb46/?child=first)
- Reference for alphabetic chars only in a string - [String isalpha() Method](https://www.w3schools.com/python/ref_string_isalpha.asp)
- Reference to check value exists in list - [Check If List Item Exists](https://www.w3schools.com/python/gloss_python_check_if_list_item_exists.asp)
- Reference for while loop until valid data - [Creating our User Request Loop](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+LS101+1/courseware/293ee9d8ff3542d3b877137ed81b9a5b/c92755338ef548f28cc31a7c3d5bfb46/?child=first)
- Reference for centering text in string - [String center() Method](https://www.w3schools.com/python/ref_string_center.asp)
- Reference to create dictionary comprehensions - [Dictionary comprehensions](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+CPP_06_20+3/courseware/f780287e5c3f4e939cd0adb8de45c12a/82a59be9f20a4f36bff58ff4a102d60a/)
- Formatting text - [How do I print colored text to the terminal?](https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal)
- ANSI colours - [ANSI escape code](https://en.wikipedia.org/wiki/ANSI_escape_code#3-bit_and_4-bit)
- Reference for Datetime to use in creating a timestamp based ID - [Datetime](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+CPP_06_20+3/courseware/272f493b4d57445fbd634e7ceca3a98c/4ab3e01af44f4bf2828739c1d0591a45/) and [formatting](https://www.w3schools.com/python/python_datetime.asp#gsc.tab=0)
- Reference for getting values from a dictionary - [values()](https://www.w3schools.com/python/ref_dictionary_values.asp)
- Reference for returning a sum of integers in a list - [math.fsum()](https://www.w3schools.com/python/ref_math_fsum.asp)
- Reference for setup, finding and updating spreadsheet with [gspread](https://docs.gspread.org/en/latest/user-guide.html)

### Acknowledgement
- My mentor Brian Macharia for his insight, guidance and words of encouragement.

<!--## Other General Project Advice

 Below you will find a couple of extra tips that may be helpful when completing your project. Remember that each of these projects will become part of your final portfolio so it’s important to allow enough time to showcase your best work! 

- One of the most basic elements of keeping a healthy commit history is with the commit message. When getting started with your project, read through [this article](https://chris.beams.io/posts/git-commit/) by Chris Beams on How to Write  a Git Commit Message 
  - Make sure to keep the messages in the imperative mood 

- When naming the files in your project directory, make sure to consider meaningful naming of files, point to specific names and sections of content.
  - For example, instead of naming an image used ‘image1.png’ consider naming it ‘landing_page_img.png’. This will ensure that there are clear file paths kept. 

- Do some extra research on good and bad coding practices, there are a handful of useful articles to read, consider reviewing the following list when getting started:
  - [Writing Your Best Code](https://learn.shayhowe.com/html-css/writing-your-best-code/)
  - [HTML & CSS Coding Best Practices](https://medium.com/@inceptiondj.info/html-css-coding-best-practice-fadb9870a00f)
  - [Google HTML/CSS Style Guide](https://google.github.io/styleguide/htmlcssguide.html#General)

Getting started with your Portfolio Projects can be daunting, planning your project can make it a lot easier to tackle, take small steps to reach the final outcome and enjoy the process!  -->


<!-- ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **May 14, 2024**

## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly


---

Happy coding! -->
