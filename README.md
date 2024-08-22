# Wordle game
For my third portfolio project with Code Institute I built a python game based on a game I play everyday, **Wordle**.

I will recreate a version of the game to be played on a Command-Line Interface (CLI) coded with python.

**Wordle** is a word game of deduction.

Players are given 6 chances to guess the 5-letter word of the day. 
With each guess, the web-based game indicates whether any of the letters used are in the word of the day and whether they are in the correct place. 
Should the player deduce the word of the day, the game tracks the winning streak as the player wins consecutive days.
If the player misses a day or fails to guess the word, the winning streak is broken and the score resets to 0.


<!-- [View the deployed website here](https://dasic002.github.io/GameOfKings/) -->

<!-- ![Responsive design mock-up](documentation/ResponsiveDesign.PNG) -->

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

Build a MVP version of the game, that does not keep any data once the game has stopped running. Thereafter add features that build on the existing code.

### Scope

<!-- Give the visitor a fun game to play that provides as much of the real life fun the game of kings provides when playing with friends. -->

### Structure

<!-- A single page that reveals different sections with game play or menu items. The page is composed of the following sections:
- **Header** - Contains title of the page, visible always.

- **Menu** - the hamburger/bars icon visible always.

- **How to play** - hidden until selected in menu or ? icon button clicked. This section is composed of several subsections for step-by-step instructions on how to play the game. Navigation buttons become available to go through the steps.

-  **Credits** - hidden until selected in menu. It will hold credits pertaining to the site composition and inspiration and a link to the GitHub repository. -->

<!-- - **Game-area** - visible on loading of page, whenever How to play or Credits section is hidden. Composed of other subsections to navigate through the game:
  - Welcome - visible on page load.
  - Player form - visible on clicking the start button or New Game in the Menu. Players can enter their name, in the absence of names, the website presumes those fields as bot players.
  - Other players - displays the other players' information.
  - Decks area - presents the draw and discard stacks to pick from.
  - Main player - presents the current player's information.
  The Game-area is manipulated by JavaScript to present the live game information and prompt actions from the human player. -->

### Skeleton

<!-- [Landing Page](documentation/PP2-GameofKings-LandingPg.jpg)

[Nav Menu](documentation/PP2-GameofKings-navMenu.jpg)

[Player entry form](documentation/PP2-GameofKings-playerEntryForm.jpg)

[Player Prompt](documentation/PP2-GameofKings-playerPrompt.jpg)

[Card hand setup for first reveal](documentation/PP2-GameofKings-cardHandSetup.jpg)

[Table Setup](documentation/PP2-GameofKings-tableSetup.jpg)

[Game play](documentation/PP2-GameofKings-gamePlay.jpg) -->

### Surface
#### Colour theme
<!-- For the Classic card game look, palette made up of 2 greens and a deep purple and off white and black. The dusty (lighter green) used to mimic the sort of matte finish of felted card tables, whilst the dark green offers better contrast for information pertaining to the players. The deep purple was selected on buttons so it complimented the greens chosen and offered plenty of contrast to its labels in the off white colour. This palette was used to create a fun and reminiscent feel of card games whilst still offering a comfortable viewing experience.

![Colour theme produced using Adobe Color tool](documentation/AdobeColor-Kings_theme.PNG) -->

<!-- #### Typography -->

## Technologies
<!-- - Languages used:
  - [HTML5](https://en.wikipedia.org/wiki/HTML5)
  - [CSS3](https://en.wikipedia.org/wiki/CSS)
  - [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [GitPod](https://www.gitpod.io/) - Cloud-based IDE to edit code and Git version control.
- [GitHub](https://github.com/) - to store and publish the project.
- [Google Fonts](https://fonts.google.com/) - to import fonts "Bree Serif" and "Patua One" into the website's CSS.
- [Font Awesome](https://fontawesome.com/) - to import icons for more recognizable action buttons. It has been used in:
  - The expandable Nav bar on narrow displays.
  - The X icon in expandable projects section.
  - The clear and submit form.
  - The contact platforms in the footer.
- [FavIcon generator](https://favicon.io/) - used to create the favicons to embed on our site.
- [Am I Responsive](https://ui.dev/amiresponsive) - to visualise the website in various display sizes.
- [Adobe Color](https://color.adobe.com/create/color-wheel) - to generate the colour palette and Accessibility tools checking for contrast for legibility and colour-blind viewing.
- [W3C HTML Validator](https://validator.w3.org/) - to validate the HTML code.
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) - to validate the CSS code.
- [JS hint](https://jshint.com/) - to validate the JS code. -->

## Features 

### Existing Features
- __Welcome__
  <!-- - The landing page consists of a simple Heading "Welcome to Kings", big "PLAY" button and a "?" icon button. 
  - Just so it offers the main point of focus, to play the game. The "?" icon button is there to offer a support, should the player not know the game, it makes it convenient for the visitor to easily reveal the instructions.<br>
  ![Welcome section mobile](documentation/Feat-WelcomeMobile.PNG) -->

- __How to Play__
  <!-- - This section revealed on clicking the "How to play" button in the menu or the "?" icon button on the landing page or player prompts, contains various subsections providing instructions with illustrations on how to play the game of kings.<br>
  ![How To Play pg1 of 10](documentation/Feat-htp1_10.PNG) ![How To Play pg2 of 10](documentation/Feat-htp2_10.PNG) ![How To Play pg3 of 10](documentation/Feat-htp3_10.PNG) 
  - The steps are provided in subsections that are navigated using the left and right arrow buttons at the bottom. Whilst the "X" button returns to the game area, this is so the player can refer to the instructions at any time and easily resume their game.<br>
  ![How To Play navigation](documentation/Feat-htp_nav.PNG)  -->

- __Credits__
  <!-- - Includes mentions to those that taught me the game, a link to the repository and a link to contact via my business (Studio Silva) WhatsApp.<br>
  ![Credits section](documentation/Feat-Credits.PNG) -->

- __Error 404 Page__
  <!-- - A page in keeping with the style of the main page of the site to indicate the visitor has stumbled upon an non-existent URL of our site and to point them back to our homepage.<br>
  ![Error 404 page](documentation/Feat-404page.PNG) -->

- __Player Prompt__
  <!-- The player prompt screen prompts the human player(s) that it is their turn, particularly useful when more than one human is playing on the same device, to help keep the player's hand and picks a secret. The prompt includes a section with last actions taken by each player. The prompt will always include the button "READY" for the player to move on to their next action and the "?" icon button as a shortcut to review the instructions. -->

  <!-- - __Initial prompt__ - At the start of the game or round this section will have an entry of "New Game!" or "New Round!" and any actions by players that have taken their turn. Mostly indicating that the players have had a turn to look at their bottom 2 cards and if any of them have decided knock already. The button "READY" will move the player to see their hand, allow shuffling and reveal the bottom 2 cards when done.<br>
  ![Early player prompt](documentation/Feat-player_prompt.PNG) -->

  <!-- - __Mid round prompt__ - After all players have had a chance to see their bottom 2 cards, the "READY" button brings the player to the table view where they can opt to take the card from the discard stack or draw from the draw stack. Hence, the first difference in the prompt is the addition of "Pick a card!" on the heading. The players' actions should also describe them as the player would view on the table. For example:
      - If a player has picked the top card from the discard stack and used it to swap with another in their hand, the syntax will follow <br>
      __"[playerName]__ took the __[name of card on discard stack]__ for their __[position of card in hand]__ , __[name of card discarded from their hand]"__<br>
      This is useful in gameplay to get an idea of how good the other players are doing and for the intriguing moment the player may have lost a good card from their hand.
      - If a player has drawn a new card and swapped a card in their hand, the syntax becomes <br>
      __"[playerName]__ drew for their __[position of card in hand]__ , __[name of card discarded from their hand]"__<br>
      The difference being that it omits the name of the card drawn as in real life no other player would have visibility of what was picked up.
      - If a player has drawn and discarded a card, presumably because the value was too high.<br>
      __"[playerName]__ drew and discarded __[name of card discarded]"__<br>
  ![Mid Round player prompt](documentation/Feat-player_prompt2.PNG) -->

  <!-- - __Last playing prompt of the round__ - After a player has opted to knock on their cards, all players thereafter will see the prompt with the heading changed to "last card!" and see the text "**KNOCKED!**" added at the end of that player's action. This is to offer the others a chance to have their last turn of the round.<br>
  ![last playing prompt of the round](documentation/Feat-player_prompt3.PNG) -->

  <!-- - __End of round prompt__ - Only visible to the knocking player (if human) or to the next human player. This triggers the scoring of all players' cards and the "READY" button will reveal the table view with the scores, players' cards and outcome of the round or game.<br>
  ![end of round prompt](documentation/Feat-player_prompt4.PNG) -->

<!-- - __Player card hand__
  - __Selecting to shuffle and countdown to reveal__
  After the player has gone through the initial prompt, the game displays the player's card hand as they'd see on the table. The player can opt to shuffle 2 cards at a time on their hand in the hope it may reveal higher values on the bottom 2 cards. On clicking "Done" the cards can no longer be selected and the game counts down to reveal these bottom cards.<br>
  ![before selecting to shuffle](documentation/Feat-card_to_shuffle.PNG) 
  ![selecting cards to shuffle](documentation/Feat-card_to_selected_pair.PNG)
  ![Countdown to reveal](documentation/Feat-card_to_btm_reveal.PNG) -->
  
  <!-- - __Selecting a card to swap with picked__
  After the player as picked a card from either stack on the table and accepted to swap that card with one in their hand, the game reuses the same player card hand display to show the player's hand so the player can select which to swap it with. On selection of the card, the game will reveal the card being discarded and countdown the knocking button before moving on to the next player.<br>
  ![selecting cards to shuffle](documentation/Feat-card_to_swap.PNG) -->
  
<!-- - __Knocking - bell icon button__
Available after the player has viewed their bottom 2 cards or swapped or discarded a card, the button for knocking appears with a 3 seconds countdown to allow the player to lock in their hand if they believe they have the winning hand.<br>
![knock after viewing hand for first time](documentation/Feat-knock_on_start.PNG)
![knock after discarding a card](documentation/Feat-knock_after_pick.PNG)<br>
If no other player has knocked yet, the button is enabled still and the icon will appear in the deep purple and contrast well with the background. After another player has knocked, the button is disabled, the content is shown in grey and the countdown is shortened to 1 second as it the player cannot act any longer on it.<br>
![enabled knocking button](documentation/Feat-Knock_enabled.PNG) 
![disabled knocking button](documentation/Feat-Knock_disabled.PNG)<br> -->

<!-- - __Table view__
  - __To pick a card__ - shown after the player has been prompted to pick up a card, this screen displays the table with the other players above, the stacks to pick from in the middle and the player's hand below. In this view, the stacks section has the deep purple background to indicate to the player that their next action involves making a selection here. Should another player have knocked for their hand, a bell icon will appear next to their name.<br>
  ![picking a card from a stack](documentation/Feat-table-cards-dealt.PNG)
  ![knocking player indicated by icon](documentation/Feat-table_knocked.PNG)
  
  - __End of Round/Game__ - shown after the human player has been prompted with end of round, the same view is displayed, except this time the players' cards are all revealed, scores assigned and in place of the stacks of cards in the middle, the round or game outcome is announced and a button prompting the player to move on to the next round or a new game. Also visible at this stage are icons next to the players' names, the winner of the round or game will have a trophy icon. Should the winner not be the player that knocked the icon "2X" is assigned to the knocking player to indicate their score of this round has been doubled. All other players are assigned an "X" icon.<br>
  ![end of round table](documentation/Feat-end_of_round.PNG)
  ![end of round table, knocking player lost](documentation/Feat-end_of_round_doubled.PNG)
  ![end of game table](documentation/Feat-end_of_game.PNG) -->

<!-- - __Player picked card__
This view is displayed when the player has made a selection of picking the card from either stack. It present the picked card in a larger format and offers a reject and an accept button to make their decision. Accepting the card will display the player's hand to select the position in their hand that they are swapping it with. Should the card be picked from the discard stack, rejecting this card will simply return to the table, whilst picking from the draw stack it will discard the card. This is because the player's turn must always end with discarding a card, be it from the draw stack or from their hand.<br>
![view of picked card](documentation/Feat-picked_card.PNG) -->

### Features Left to Implement
<!-- - A more intuitive game for a single human player would display the game on the table and show the moves the bot players make as you would playing the game in real life. For example, the game depicts the table with the players' cards face down and as a bot makes its moves of drawing a card from the draw stack, a card is animated as being removed from the stack and if swapped it displays that movement too. There it is easier to visualise the game as opposed to having to read the summary of steps between turns where some might find it too disjointed in the gameplay.

- To make the game play as accurate to real life, knocking on viewing of the bottom 2 cards of the player's hand should record time taken by the player from the moment the knock button appears and compare that to whoever has knocked too, whoever was quickest to knock after viewing their cards gets the status. However, this is rare for players to want to knock this early and even more so for more than one player to feel confident enough to knock this early and would only be necessary if the game remains played on one single device.

- The game is made to play as a multiplayer, the initial idea was to make the game playable over the internet with multiple human players joining a table, but was advised by my mentor that this is a feature outside of the scope of JavaScript alone and have not learnt about WebSocket yet.

- The original intent with the BotSkill value, was to mimic a bot player that might have poorer memory for remembering the cards accurately. So 1 - as novice, might be a bot that remembers a particular card as being in another position or have thought it's value was higher and risk losing good cards. Whilst level 3 - expert, might remember the cards it has seen with great accuracy or that it employs a very discerning tactic of wanting for only the best cards to be picked up before "knocking", locking their hand.

- More game interactions. Initially planned to include:
  - the option of having sounds on the game;
  - customisable colour theme of cards artwork and table appearance;
  - Illustrated and/or animated reactions on reveals of the cards swapped out, for instance a good swap could display a thumbs up and a "Nice!" text over the card, whereas a bad swap could momentarily turn the image monochrome and display a message of "Oh no!". -->

## Testing 

### Validator Testing 

- Python
  <!-- - No errors were found when passing through [PEP8](http://pep8online.com/)<br>
  ![error free screenshot](documentation/Test-JS_Validation.PNG) -->
<!-- - Accessibility
  - Running the site through lighthouse analysis confirms the colours and fonts used legible and accessible on either:
    - Mobile:<br>
  ![Lighthouse mobile analysis](documentation/Lighthouse_analysis-Mobile.PNG)
 
    - Desktop:<br>
  ![Lighthouse desktop analysis](documentation/Lighthouse_analysis-Desktop.PNG)

  - Running the site through [WAVE accessibility tool](https://wave.webaim.org/report#/https://dasic002.github.io/GameOfKings/index.html) showed no obvious errors after some improvements were made.<br>
  ![Wave accessibility evaluation results](documentation/Test-wave-accessibility.PNG) -->

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



### Unfixed Bugs

<!-- - __KeyDown Enter/Carriage return on player Form - refreshes page__
Whilst a form field is in focus pressing the enter key refreshes the page. Need to make it so this keyDown starts the game with what information has been entered, the same way clicking on start game button does. A few attempts have been made, but have only brought up more errors. It has not been prioritised since the game is primarily designed to play on touchscreen.

- __No card in discard stack at the start of the game__
When testing the game on the phone sometimes the discard stack does not show a card and if picked from, it presents an undefined value. The only correlation leading to this error is selecting the cards to shuffle in the player's hand so fast that it does not seem to register the second selection properly. It will highlight it, but not remove the highlight after the timeOut which could mean it is also not running all functions necessary to swap those 2 cards. Select a 3rd card and it clears the highlight, but of course, we don't know which 2 were actually swapped. I've tested the game after adding a code that disabled the card buttons from the moment one is selected until the last function has run its course in registering the last selection, that prevented selecting more that 2 cards at a time, but the error was still seen. It's difficult to replicate this error on a desktop or laptop with mouse clicks, to able to diagnose what is happening via the console. Either there is a way of linking my phone to the computer to view the errors or perhaps I can use a mouse control app to program rapid clicks to mimic that of taps on the touchscreen.
 - __May be fixed now__
 After further testing, it seems the error appeared when the human player makes a single card selection to shuffle but does not complete the move with a second selection, and when the next player is a bot it seems to run a function to swap cards and when the values the variable holds at that time are not compatible and produces an undefined entry.
 After adding some code that on clicking "DONE" it clears the variables that would retain the values for the card hand selection, this issue has not appeared again since.

 Also, to remove the ambiguity of the card selection, code has also been added to disable the card buttons from the moment one is clicked until the script is done registering the card selection. -->

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

### Content 
<!-- - Icons used in the nav bar, some buttons and indicators were sourced from [Font Awesome](https://fontawesome.com/)
- Fonts used in the whole site sourced from [Google fonts](https://fonts.google.com/)
- All text written by developer -->

### Media
<!-- - Artwork for card back and suits icons generated by the developer. -->

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
- Reference for dictionary list - [values()](https://www.w3schools.com/python/ref_dictionary_values.asp)
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
