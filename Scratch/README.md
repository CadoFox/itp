# SearchLight Game
## Simple search and destroy type mini game!

### (I must admit, I totally forgot to document this project AS I was making it, so this will be a sort of explanation/ recounting of the debugging process)

# How it works / hurdles

## Main functionality
## Objective: Find and click each next circle before the time runs out. There are 20 seconds to find the 20 circles, so every second counts! The circle get progressively smaller as you get closer to the end, and you are penalized for missing the circle, so be careful!

## Circle Sprite
### Circle sprite has its opacity tied to its distance from the pointer, and when it is clicked it will pick a new random location within the bounds that I set with the random number gen object

- I had originally wanted it to pick a new location that was over a certain distance from old location so that you couldn't see its new location before "looking" for it, but I actually decided I liked the "randomized advantage" that it would give. Felt like it made me wanna play it again and see if I could do it faster.

- **bug**: later on decided I wanted to introduce some difficulty, so I decided to make the circle start really big, and then get smaller and smaller as you get closer to winning the game. The initial functionality was easy to figure out, but it took some thinking to get it to properly reset the size so that it was big again at the start of the game.
(note: because the distance-opacity is tied to the center of the sprite, not the bounds, the circle starting bigger actually tricks you into thinking it'll be easier, when its actually not that much easier to **find**, just to **click**)

## Score keeping/ level system
### I decided to use broadcast and a custom variable to keep all the score logic in the backdrop object so that I could change around the functionality of the game without needing to re-code the score into each new sprite. I also didn't like that the score variable would be labeled as part OF the sprite, and that label is absent if its tied to the backdrop instead.

## The game only has one level before completion, which is when you pass 10. Nothing changes when you pass 10, it was just an excuse to make a "level cleared" sound too.

- Scoring is handled with some simple math operations and conditions. This was actually the second thing I implemented, and I started with just getting it to count up UNTIL a certain number and then resetting.

- **note**: I actually used broadcast a lot to handle the main game states and scoring, the reason being I could use those broadcasts to trigger things like initializing the game after win or lose (**bug**: see game reset section). It also let me keep all the sound triggers neatly separate and easy to read.

- The level clear functionality was actually really fun to figure out. Initially I began with an equals boolean, but I realized if I wanted more levels, I would need to have blocks for each one. Instead, I looked into the documentation and found the modulo object, which allowed me to check if the score was divisible by 10. This allowed the game length to be fairly dynamically scalable, as it will just automatically trigger the level cleared state when it hits any score divisible by 10 (this version only goes up to 20).

- **bug**: Using the modulo object did force me to think outside the box a little bit, as it resulted in both the click sound and the level clear sound to be played at the same time, which is not what I intended. I resorted to an if else condition on the level clear and level complete triggers, so that it would ignore the trigger if the score was equal to 10 (level clear state) or 20 (win state).

## Lives
### Lives system is an even simpler subtractive version of the score keeping, except it resets the game when it hits 0.

- While not the most elegant or thorough solution, I just have two if conditions triggering lose state if it hits 0, and reset to 5 when it tries to go below 0 (which only happens if the sprite is clicked after win or lose state, which would have to be once the game has already reset).

## Timer
## Timer is triggered by the score hitting 1, allowing a static reset state instead of having the game just continuously running.

- I used a "repeat until" condition with a custom variable so that I could have a visible counter that I could customize to count down with some math operations. The time object also outputs decimal, which I didn't want, so I used the round object to have it ignore everything after the decimal point.

- The timer reset is triggered by the win or lose game states.

## Game Reset Bug
### Biggest bug I encountered: getting the game to re-initialize all parameters, the timer, and also stop the game so that the user can decide when it start again instead f it just running

- **bug**: I could not get the circle size to reset properly; it would simply either stay small after playing it once, or it wouldn't reset until the game was started again. I discovered this was a timing issue, as the code was stopping before the reset could go through. I fixed this with a "wait x seconds" object.

- **bug (ongoing)**: Using the "wait x seconds" object to fix the game reset meant I needed to make sure I was aware of anything else I was also timing at the end of the win or lose states. This caused some headaches at first when I realized if I set something to wat the same amount of time or more, it could end up not working. If I was to re-do this functionality, I might find another method for fixing the reset issues such that I don't have to rely on whether or not something is timed correctly in order for all the necessary triggers to be hit before game reset.

- **bug**: I had some trouble with resetting the timer at the end of the game, as I could not get it to reset with the win and BOTH of the lose triggers, AND also START the timer at the start of the game (this was also part of why I used broadcast for these triggers: no redundancy). Using the condition to check when the score hits "1" ended up working for me, as this would only happen after the game has been lost or completed, and thus reset.

## Fun fact: Sprites, screens, and game sounds
### I just thought you'd enjoy knowing I designed the main sprite + the text screens all myself in Adobe Illustrator, and also made all the little sci-fi game sounds myself in my DAW!
