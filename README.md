# Game-Development-Project
Game development.



Implementing a maze game where we have an avatar and some random enemies. The avatar will be placed in a specific point of entrance in the maze (not randomly). Avatar can collect things that adds additional functionality to the avatar, such as becoming invisible or more resistant to enemies’ attack, or even the ability to cross the maze wall, and the ideas mentioned above. At the same time, the enemies are generated randomly to be placed on different spots of the maze after the game starts. Then the enemies should walk inside the maze (Randomly or with specified path). 

Final Design to specify:
1. The Background Story of Game.
2. How NPC move around.
----------------------------------------------------------------------------------------------------
Second Week Update:
Game Plot: Story of vampires from transylvania, inspired by the book "Dracula"

Background: The main character is a man and he was invited to send documents for Count Dracula at Transylvania, which is some documents explainning a real estate purchase.

Scene One: Our main character be initialized on the map and find its way to transylvania. In this scene, Count Dracula will move in a predetermined path and our avartar need to find him in the maze, so that Count Dracula lead the way out. (Note: It would be better if we know how to do limited vision, and how to change map in the same scene)

Scene Two: Avatar chased by wolves

Scene Three: Avatar being held in the castle of Dracula and trying to find the way out the castle through windows. We hope to design the windows as secrectly connected.

So Final Questions: 
One: How to move the view window around as our avatar moves, using the same background.
Two: How to change scenes
Three: How the windows tunelling functionality will be realized. We are thinking collision detection + position update of the avatar.

Techniques that would be employed: A. Collision detection to limit the avatar's motion. B. Collision detection to transimit avatar among windows C. Collision detection to determine whether the avatar have encountered dracula. D. Navigation Algorithm to decide for wolves that chasing down the avatar. E. Navigation technique to lead the way of Dracula. F. How to transit between different background maps
