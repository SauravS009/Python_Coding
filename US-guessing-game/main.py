import turtle
import pandas as pd
FONT=("Arial",30)

image = "blank_states_img.gif"
screen = turtle.Screen()
screen.addshape(image)
guessed = []
turtle1 = turtle.Turtle()
turtle1.shape(image)
guess_num=0
data = pd.read_csv("50_states.csv")
states = data.state.to_list()
is_game_on = True
score=0
scorecard=turtle.Turtle()
scorecard.penup()
scorecard.hideturtle()
scorecard.goto(176,290)
while is_game_on:
    answer = screen.textinput(title=f"Guess the state  {guess_num} / 50", prompt="Guess another state's name").title()
    guess_num+=1
    if answer == "Exit":
        missing_states=[]
        for st in states:
            if st not in guessed:
                missing_states.append(st)
        break
    if answer in states:
        guessed.append(answer)
        score+=1
        obs = data[data.state == answer]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(obs.x), int(obs.y))
        t.write(answer)
        scorecard.clear()
        scorecard.write(f"Score: {score}/50",font=("Arial",25))

    if guess_num == 50:
        scorecard.goto(0,0)
        scorecard.write(f"Game Over, you scored {score}/50",align="center",font=FONT)
        is_game_on = False

df = pd.DataFrame(missing_states)
df.to_csv("learn.csv")



