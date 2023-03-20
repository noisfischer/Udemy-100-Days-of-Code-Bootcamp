import turtle
import pandas


def print_state(state, x, y, state_name):
    state = turtle.Turtle()
    state.color('black')
    state.penup()
    state.goto(x, y)
    state.hideturtle()
    state.write(f"{state_name}", False, "center", "arial", 12, "normal")



screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_list = pandas.read_csv("50_states.csv")
all_states = states_list.state.to_list()
guessed_states = []

while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = states_list[states_list.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

for state in guessed_states:
    remove_state = all_states.index(state)
    all_states.pop(remove_state)


missed_states = pandas.DataFrame(
    {
        "state": all_states
    }
)

missed_states.to_csv("missed_states.csv")

screen.exitonclick()
