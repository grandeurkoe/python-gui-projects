import turtle
import pandas

guessed_correct_counter = 0
guessed_list = []
missing_list = []
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.setup(width=800, height=550)

states_data = pandas.read_csv("50_states.csv")
screen.tracer(0)
is_game_on = True

while is_game_on:
    state_counter = 0
    guessed_state = turtle.textinput(title=f"{guessed_correct_counter}/50 States Correct", prompt="What's another "
                                                                                                  "state name?").title()
    for each_state in states_data.state:
        if each_state == guessed_state:
            turtle.goto(states_data.x[state_counter], states_data.y[state_counter])
            turtle.write(each_state)
            guessed_list.append(each_state)
            turtle.home()
            guessed_correct_counter += 1
        state_counter += 1
    screen.update()

    if guessed_state == "Exit" or guessed_correct_counter == 50:
        is_game_on = False

# for each_state in states_data.state:
#     if each_state not in guessed_list:
#         missing_list.append(each_state)
# OR
missing_list = [each_state for each_state in states_data.state if each_state not in guessed_list]

missing_states = pandas.DataFrame(missing_list)
missing_states.to_csv("states_to_learn.csv")
