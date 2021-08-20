import turtle
import pandas

screen = turtle.Screen()
# screen.screensize(600, 600)
screen.title("India States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("36_states_ut.csv")
states = data["state"]

# x = data["x"]
# y = data["y"]
# print(states)
states_list = states.to_list()
print(states_list)

pen = turtle.Turtle()
pen.penup()
pen.hideturtle()

game_is_on = True
guess = 0
already_guessed = []

while guess < 36:
    answer_state = screen.textinput(title=f"Guessed {guess}/36 States/UT", prompt="Guess a state!!!!").title()
    if answer_state in states_list:
        if answer_state not in already_guessed:
            already_guessed.append(answer_state)
            state_data = data[data["state"] == answer_state]
            pen.goto(int(state_data.x), int(state_data.y))
            pen.write(answer_state)
            guess += 1
    if guess == 36 or answer_state == "Exit":
        # pen.write("GAME OVER!!!!!")
        missed_out_states = []
        for state in states_list:
            if state not in already_guessed:
                missed_out_states.append(state)
        missed_out_dict = {
            "States": missed_out_states
        }
        df = pandas.DataFrame(missed_out_dict)
        df.to_csv("states_to_learn.csv")
        break


turtle.mainloop()
