import random
from js import document

# Game Constants
GRID_SIZE = 5
NUM_TRAINS = 3
COLORS = ["red", "blue", "green"]

grid = []  # 2D list to represent the grid
trains = []  # List of train objects
exits = {}  # Dictionary of exit locations, keyed by color

def create_grid():
    """Creates a random grid of switches."""
    global grid
    grid = []
    for row in range(GRID_SIZE):
        grid_row = []
        for col in range(GRID_SIZE):
            # Randomly choose a switch type (0, 1, or 2)
            switch_type = random.randint(0, 2)
            grid_row.append(switch_type)
        grid.append(grid_row)

def render_grid():
    """Renders the grid in the HTML."""
    grid_element = document.getElementById("grid")
    grid_element.innerHTML = ""  # Clear existing grid

    grid_element.style.gridTemplateColumns = " ".join(["auto"] * GRID_SIZE) # dynamic grid columns

    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            cell = document.createElement("div")
            cell.classList.add("grid-cell")
            cell.dataset.row = str(row) # Store row and col for click events
            cell.dataset.col = str(col)

            switch_type = grid[row][col]
            switch_element = document.createElement("span")
            switch_element.classList.add("switch")
            switch_element.textContent = str(switch_type) # Display switch type
            switch_element.onclick = switch_click_handler # Attach click handler

            cell.appendChild(switch_element)
            grid_element.appendChild(cell)

def switch_click_handler(event):
    """Handles clicks on switches to change their direction."""
    cell = event.target.parentNode #get the parent div of the clicked switch
    row = int(cell.dataset.row)
    col = int(cell.dataset.col)

    # Change the switch type (0 -> 1 -> 2 -> 0)
    grid[row][col] = (grid[row][col] + 1) % 3
    render_grid()  # Re-render the grid to update the switch display

def create_trains():
    """Creates trains with random colors and starting positions."""
    global trains
    trains = []
    for i in range(NUM_TRAINS):
        color = random.choice(COLORS)
        start_row = random.randint(0, GRID_SIZE - 1)
        start_col = random.randint(0, GRID_SIZE - 1)
        train = {"color": color, "row": start_row, "col": start_col}
        trains.append(train)

def render_trains():
    """Renders the trains on the grid."""
    for train in trains:
        cell = document.querySelector(f'.grid-cell[data-row="{train["row"]}"][data-col="{train["col"]}"]')
        if cell:  # Make sure the cell exists
            train_element = document.createElement("div")
            train_element.classList.add("train", train["color"])
            cell.appendChild(train_element)

def create_exits():
    """Creates exits for each train color."""
    global exits
    exits = {}
    for color in COLORS:
        exit_row = random.randint(0, GRID_SIZE - 1)
        exit_col = random.randint(0, GRID_SIZE - 1)
        exits[color] = (exit_row, exit_col)

def game_loop():
  """main game loop: Move trains, check for collisions and wins"""
  #TODO: Implement movement logic and win/lose conditions.
  pass
def start_new_game(event=None): # Allow calling from button click
    """Starts a new game."""
    create_grid()
    create_trains()
    create_exits()
    render_grid()
    render_trains()  # Initial render of trains

# Initialize the game when the script runs
start_new_game()

# Event listener for the new game button
new_game_btn = document.getElementById("new-game-btn")
new_game_btn.onclick = start_new_game
