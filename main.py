import pandas
from turtle import Screen, colormode, shape
from state_names import StateNames

colormode(255)
screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
shape(image)


data = pandas.read_csv("50_states.csv")
all_states = data.state.tolist()


def get_coordinates(selected_state):
    x = int(data[data["state"] == selected_state].get("x"))
    y = int(data[data["state"] == selected_state].get("y"))
    return x, y


def save_missing_state(list_of_states):
    missing_data = pandas.DataFrame(list_of_states)
    missing_data.to_csv("missed_states.csv")


guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Guess the State", prompt="What's the state name?")\
        .title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        save_missing_state(missing_states)
        break
    if answer_state in all_states:
        coordinates = get_coordinates(answer_state)
        print_state = StateNames(state_name=answer_state, position=coordinates)
        guessed_states.append(answer_state)
