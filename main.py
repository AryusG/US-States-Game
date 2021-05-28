import pandas as pd
import turtle as t

screen = t.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
t.shape(image)

data = pd.read_csv("50_states.csv")



answer_state = screen.textinput(title='Guess the State', prompt="What's another state's name?").title()

# check if answer_state is in 50 states.csv
state_series = data['state']

for state in state_series:
    if answer_state == state:
        # Write correct guess onto map
        state_row = data[data.state == state]
        x_coord = state_row.y
        y_coord = state_row.x
        print(int(x_coord))
        print(int(y_coord))

        state_text = t
        state_text.goto(x_coord, y_coord)
        state_text.write(f"{state}", align='center', font=("Arial", 10, "normal"))

# Use loop to allow constant guessing

# Record correct guesses in a list

# Keep track of score


t.mainloop()
