# Four Computational Thinking Processes

- **decomposition** - Split the code into smaller varaibles such as plants and zombies, split into health, damage, and name(and moving if for zombies). Then, these will be split into even smaller operations such as; attacking, moving, and taking damage

- **Pattern Recognition** - The actions expected to repeat onward until either side dies is to attack, and take damage (and moving for zombies.)

- **Abstraction** - The only informations both sides need are: damage, health, and name (if we also add the movement for zombies.)

- **Algorithm Design** -  First make the zombie class with the variables; the attack, take damage, and movement. After that, make the plant class with the variables: attack, movement, and take damage. After that we make the objects and variables for each class which will sound as plant1, plant2, and zombie1. And after that, we turn out attention to the game info and while-true loop. The while-true loop will check the distance is zero before doing/taking damage. Then after enough turns, either sides die once reaching 0 health.
