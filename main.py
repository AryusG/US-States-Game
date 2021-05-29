import pandas as pd
import turtle as t

screen = t.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
t.shape(image)

data = pd.read_csv("50_states.csv")
correct_answers = []


while len(correct_answers) < 50:
    answer_state = screen.textinput(title=f'{len(correct_answers)}/50 States Correct',
                                    prompt="What's another state's name?").title()
    state_list = data['state'].to_list()

    if answer_state == "Exit":
        missed_states_list = []
        for state in state_list:
            if state not in correct_answers:
                missed_states_list.append(state)

        df = pd.DataFrame(missed_states_list)
        df.to_csv("missed_states.csv")
        break

    if answer_state in state_list:
        state_row = data[data.state == answer_state]

        state_text = t.Turtle()
        state_text.hideturtle()
        state_text.penup()
        state_text.goto(int(state_row.x), int(state_row.y))
        # state_text.write(f"{answer_state}", align='center', font=("Arial", 10, "normal"))
        state_text.write(state_row.state.item())

        correct_answers.append(answer_state.title())

# States to learn.csv

