################### Scope #################



enemies = 1
def increase_enemies():
    """
    #This is not a good practice. Can raise a lot of bugs.
    global enemies 
    enemies += 2
    print(f"Enemies inside function: {enemies}")
    
    """
    # A better approach to tap the global variable
    print(f"Enemies inside function: {enemies}")
    return enemies + 1 
    


increase_enemies()
print(f"Enemies outside Function: {enemies}")


# Local Scope exists within functions

def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()


# Global Scope not defining within functions
player_health = 10

def drink_potion():
    potion_strength = 2
    print(player_health)

print(player_health)



# There is no such this as Block Scope in python
game_level = 3
enemies = ['Sekeleton', 'Zombies', 'Alien']
if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy)


def create_enemy():
    enemies = ['Sekeleton', 'Zombies', 'Alien']
    if game_level < 5:
        new_enemy = enemies[0]
    print(new_enemy)