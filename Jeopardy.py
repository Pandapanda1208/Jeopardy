import os
import json
import pygame

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

with open('Jeopardy_data.json', 'r') as f:
    data = json.load(f)

clear()

#print(data["category_one"][0]["questions"][0]["question"])     #1-100 - question
#print(data["category_two"][0]["questions"][1]["answer"])       #2-200 - answer
#print(data["category_three"][0]["questions"][4]["points"])     #3-500 - points
#print(data["category_four"][0]["questions"][3]["color"])       #4-400 - color
#print(data["category_five"][0]["name"])                        #5 - category name

pygame.init()
pygame.mixer.init()


flags = pygame.FULLSCREEN | pygame.SCALED | pygame.DOUBLEBUF
logical_size = (1366, 768)

screen = pygame.display.set_mode(logical_size, flags)

pygame.mixer.music.load('Jeopardy Theme.wav')
pygame.mixer.music.play(-1)

font = pygame.font.SysFont(None, 36)

non_board_bg = pygame.Rect(0, 0, 1366, 768)

colum_one = pygame.Rect(271, 0, 4, 1366)
colum_two = pygame.Rect(545, 0, 4, 1366)
colum_three = pygame.Rect(819, 0, 4, 1366)
colum_four = pygame.Rect(1093, 0, 4, 1366)

row_one = pygame.Rect (0, 128, 1366, 2)
row_two = pygame.Rect (0, 256, 1366, 2)
row_three = pygame.Rect (0, 384, 1366, 2)
row_four = pygame.Rect (0, 512, 1366, 2)
row_five = pygame.Rect (0, 640, 1366, 2)


cat_one_sub = pygame.Rect(0, 0, 271, 128)
cat_one_one = pygame.Rect(0, 130, 271, 127)
cat_one_two = pygame.Rect(0, 258, 271, 127)
cat_one_three = pygame.Rect(0, 386, 271, 127)
cat_one_four = pygame.Rect(0, 514, 271, 127)
cat_one_five = pygame.Rect(0, 642, 271, 127)

cat_two_sub = pygame.Rect(271, 0, 274, 128)
cat_two_one = pygame.Rect(271, 130, 274, 127)
cat_two_two = pygame.Rect(271, 258, 274, 127)
cat_two_three = pygame.Rect(271, 386, 274, 127)
cat_two_four = pygame.Rect(271, 514, 274, 127)
cat_two_five = pygame.Rect(271, 642, 274, 127)

cat_three_sub = pygame.Rect(545, 0, 274, 128)
cat_three_one = pygame.Rect(545, 130, 274, 127)
cat_three_two = pygame.Rect(545, 258, 274, 127)
cat_three_three = pygame.Rect(545, 386, 274, 127)
cat_three_four = pygame.Rect(545, 514, 274, 127)
cat_three_five = pygame.Rect(545, 642, 274, 127)

cat_four_sub = pygame.Rect(819, 0, 274, 128)
cat_four_one = pygame.Rect(819, 130, 274, 127)
cat_four_two = pygame.Rect(819, 258, 274, 127)
cat_four_three = pygame.Rect(819, 386, 274, 127)
cat_four_four = pygame.Rect(819, 514, 274, 127)
cat_four_five = pygame.Rect(819, 642, 274, 127)

cat_five_sub = pygame.Rect(1093, 0, 273, 128)
cat_five_one = pygame.Rect(1093, 130, 273, 127)
cat_five_two = pygame.Rect(1093, 258, 273, 127)
cat_five_three = pygame.Rect(1093, 386, 273, 127)
cat_five_four = pygame.Rect(1093, 514, 273, 127)
cat_five_five = pygame.Rect(1093, 642, 273, 127)


cat_six_sub = pygame.Rect(0, 0, 271, 128)
cat_six_one = pygame.Rect(0, 130, 271, 127)
cat_six_two = pygame.Rect(0, 258, 271, 127)
cat_six_three = pygame.Rect(0, 386, 271, 127)
cat_six_four = pygame.Rect(0, 514, 271, 127)
cat_six_five = pygame.Rect(0, 642, 271, 127)

cat_seven_sub = pygame.Rect(271, 0, 274, 128)
cat_seven_one = pygame.Rect(271, 130, 274, 127)
cat_seven_two = pygame.Rect(271, 258, 274, 127)
cat_seven_three = pygame.Rect(271, 386, 274, 127)
cat_seven_four = pygame.Rect(271, 514, 274, 127)
cat_seven_five = pygame.Rect(271, 642, 274, 127)

cat_eight_sub = pygame.Rect(545, 0, 274, 128)
cat_eight_one = pygame.Rect(545, 130, 274, 127)
cat_eight_two = pygame.Rect(545, 258, 274, 127)
cat_eight_three = pygame.Rect(545, 386, 274, 127)
cat_eight_four = pygame.Rect(545, 514, 274, 127)
cat_eight_five = pygame.Rect(545, 642, 274, 127)

cat_nine_sub = pygame.Rect(819, 0, 274, 128)
cat_nine_one = pygame.Rect(819, 130, 274, 127)
cat_nine_two = pygame.Rect(819, 258, 274, 127)
cat_nine_three = pygame.Rect(819, 386, 274, 127)
cat_nine_four = pygame.Rect(819, 514, 274, 127)
cat_nine_five = pygame.Rect(819, 642, 274, 127)

cat_ten_sub = pygame.Rect(1093, 0, 273, 128)
cat_ten_one = pygame.Rect(1093, 130, 273, 127)
cat_ten_two = pygame.Rect(1093, 258, 273, 127)
cat_ten_three = pygame.Rect(1093, 386, 273, 127)
cat_ten_four = pygame.Rect(1093, 514, 273, 127)
cat_ten_five = pygame.Rect(1093, 642, 273, 127)

phase = "board_one"
stage = "category"


run = True
while run:
    screen.fill((255, 0, 0))

    if data["final"][0]["ready"] == "aaaaaaaaaaaaaaaaaaaaaaaaa":
        if data['second_board_start'] == False:
            data['second_board_start'] = True
            phase = "board_two"
            data['final'][0]['ready'] = "qwertyuiopsdfghjklzxcvbnm"
        else:
            phase = "final"

    if phase == "final":
        if stage == "category":
            pygame.draw.rect(screen, (0, 0, 255), non_board_bg)
            text = font.render(data["final"][0]["name"], True, (255, 255, 0))
            non_board_bg_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, non_board_bg_t)
        elif stage == "question":
            pygame.draw.rect(screen, (0, 0, 255), non_board_bg)
            text = font.render(data["final"][0]["question"]['3'], True, (255, 255, 0))
            non_board_bg_t = text.get_rect(center=pygame.Vector2(non_board_bg.center) + (0, 30))
            screen.blit(text, non_board_bg_t)
            text = font.render(data["final"][0]["question"]['2'], True, (255, 255, 0))
            non_board_bg_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, non_board_bg_t)
            text = font.render(data["final"][0]["question"]['1'], True, (255, 255, 0))
            non_board_bg_t = text.get_rect(center=pygame.Vector2(non_board_bg.center) - (0, 30))
            screen.blit(text, non_board_bg_t)
        elif stage == "answer":
            pygame.draw.rect(screen, (0, 0, 255), non_board_bg)
            text = font.render(data["final"][0]["answer"], True, (255, 255, 0))
            non_board_bg_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, non_board_bg_t)
        elif stage == "end":
            pygame.draw.rect(screen, (0, 0, 255), non_board_bg)
            text = font.render("The End!", True, (255, 255, 0))
            non_board_bg_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, non_board_bg_t)

    if phase == "board_one":
        pygame.draw.rect(screen, (0, 0, 255), cat_one_sub)
        text = font.render(data["category_one"][0]["name"], True, (255, 255, 0))
        cat_one_sub_t = text.get_rect(center=cat_one_sub.center)
        screen.blit(text, cat_one_sub_t)
        pygame.draw.rect(screen, (0, 0, 255), cat_one_one)
        if data["category_one"][0]["questions"][0]["color"] == "yellow":
            text = font.render(data["category_one"][0]["questions"][0]["points"], True, (255, 255, 0))
        elif data["category_one"][0]["questions"][0]["color"] == "red":
            text = font.render(data["category_one"][0]["questions"][0]["points"], True, (255, 0, 0))
        else:
            text = font.render(data["category_one"][0]["questions"][0]["points"], True, (169, 169, 169))
        cat_one_one_t = text.get_rect(center=cat_one_one.center)
        screen.blit(text, cat_one_one_t)
        pygame.draw.rect(screen, (0, 0, 255), cat_one_two)
        if data["category_one"][0]["questions"][1]["color"] == "yellow":
            text = font.render(data["category_one"][0]["questions"][1]["points"], True, (255, 255, 0))
        elif data["category_one"][0]["questions"][1]["color"] == "red":
            text = font.render(data["category_one"][0]["questions"][1]["points"], True, (255, 0, 0))
        else:
            text = font.render(data["category_one"][0]["questions"][1]["points"], True, (169, 169, 169))
        cat_one_two_t = text.get_rect(center=cat_one_two.center)
        screen.blit(text, cat_one_two_t)
        pygame.draw.rect(screen, (0, 0, 255), cat_one_three)
        if data["category_one"][0]["questions"][2]["color"] == "yellow":
            text = font.render(data["category_one"][0]["questions"][2]["points"], True, (255, 255, 0))
        elif data["category_one"][0]["questions"][2]["color"] == "red":
            text = font.render(data["category_one"][0]["questions"][2]["points"], True, (255, 0, 0))
        else:
            text = font.render(data["category_one"][0]["questions"][2]["points"], True, (169, 169, 169))
        cat_one_three_t = text.get_rect(center=cat_one_three.center)
        screen.blit(text, cat_one_three_t)
        pygame.draw.rect(screen, (0, 0, 255), cat_one_four)
        if data["category_one"][0]["questions"][3]["color"] == "yellow":
            text = font.render(data["category_one"][0]["questions"][3]["points"], True, (255, 255, 0))
        elif data["category_one"][0]["questions"][3]["color"] == "red":
            text = font.render(data["category_one"][0]["questions"][3]["points"], True, (255, 0, 0))
        else:
            text = font.render(data["category_one"][0]["questions"][3]["points"], True, (169, 169, 169))
        cat_one_four_t = text.get_rect(center=cat_one_four.center)
        screen.blit(text, cat_one_four_t)
        pygame.draw.rect(screen, (0, 0, 255), cat_one_five)
        if data["category_one"][0]["questions"][4]["color"] == "yellow":
            text = font.render(data["category_one"][0]["questions"][4]["points"], True, (255, 255, 0))
        elif data["category_one"][0]["questions"][4]["color"] == "red":
            text = font.render(data["category_one"][0]["questions"][4]["points"], True, (255, 0, 0))
        else:
            text = font.render(data["category_one"][0]["questions"][4]["points"], True, (169, 169, 169))
        cat_one_five_t = text.get_rect(center=cat_one_five.center)
        screen.blit(text, cat_one_five_t)

        pygame.draw.rect(screen, (0, 0, 255), cat_two_sub)
        text = font.render(data["category_two"][0]["name"], True, (255, 255, 0))
        cat_two_sub_t = text.get_rect(center=cat_two_sub.center)
        screen.blit(text, cat_two_sub_t)
        pygame.draw.rect(screen, (0, 0, 255), cat_two_one)
        if data["category_two"][0]["questions"][0]["color"] == "yellow":
            text = font.render(data["category_two"][0]["questions"][0]["points"], True, (255, 255, 0))
        elif data["category_two"][0]["questions"][0]["color"] == "red":
            text = font.render(data["category_two"][0]["questions"][0]["points"], True, (255, 0, 0))
        else:
            text = font.render(data["category_two"][0]["questions"][0]["points"], True, (169, 169, 169))
        cat_two_one_t = text.get_rect(center=cat_two_one.center)
        screen.blit(text, cat_two_one_t)
        pygame.draw.rect(screen, (0, 0, 255), cat_two_two)
        if data["category_two"][0]["questions"][1]["color"] == "yellow":
            text = font.render(data["category_two"][0]["questions"][1]["points"], True, (255, 255, 0))
        elif data["category_two"][0]["questions"][1]["color"] == "red":
            text = font.render(data["category_two"][0]["questions"][1]["points"], True, (255, 0, 0))
        else:
            text = font.render(data["category_two"][0]["questions"][1]["points"], True, (169, 169, 169))
        cat_two_two_t = text.get_rect(center=cat_two_two.center)
        screen.blit(text, cat_two_two_t)
        pygame.draw.rect(screen, (0, 0, 255), cat_two_three)
        if data["category_two"][0]["questions"][2]["color"] == "yellow":
            text = font.render(data["category_two"][0]["questions"][2]["points"], True, (255, 255, 0))
        elif data["category_two"][0]["questions"][2]["color"] == "red":
            text = font.render(data["category_two"][0]["questions"][2]["points"], True, (255, 0, 0))
        else:
            text = font.render(data["category_two"][0]["questions"][2]["points"], True, (169, 169, 169))
        cat_two_three_t = text.get_rect(center=cat_two_three.center)
        screen.blit(text, cat_two_three_t)
        pygame.draw.rect(screen, (0, 0, 255), cat_two_four)
        if data["category_two"][0]["questions"][3]["color"] == "yellow":
            text = font.render(data["category_two"][0]["questions"][3]["points"], True, (255, 255, 0))
        elif data["category_two"][0]["questions"][3]["color"] == "red":
            text = font.render(data["category_two"][0]["questions"][3]["points"], True, (255, 0, 0))
        else:
            text = font.render(data["category_two"][0]["questions"][3]["points"], True, (169, 169, 169))
        cat_two_four_t = text.get_rect(center=cat_two_four.center)
        screen.blit(text, cat_two_four_t)
        pygame.draw.rect(screen, (0, 0, 255), cat_two_five)
        if data["category_two"][0]["questions"][4]["color"] == "yellow":
            text = font.render(data["category_two"][0]["questions"][4]["points"], True, (255, 255, 0))
        elif data["category_two"][0]["questions"][4]["color"] == "red":
            text = font.render(data["category_two"][0]["questions"][4]["points"], True, (255, 0, 0))
        else:
            text = font.render(data["category_two"][0]["questions"][4]["points"], True, (169, 169, 169))
        cat_two_five_t = text.get_rect(center=cat_two_five.center)
        screen.blit(text, cat_two_five_t)

        pygame.draw.rect(screen, (0, 0, 255), cat_three_sub)
        text = font.render(data["category_three"][0]["name"], True, (255, 255, 0))
        cat_three_sub_t = text.get_rect(center=cat_three_sub.center)
        screen.blit(text, cat_three_sub_t)
        pygame.draw.rect(screen, (0, 0, 255), cat_three_one)
        if data["category_three"][0]["questions"][0]["color"] == "yellow":
            text = font.render(data["category_three"][0]["questions"][0]["points"], True, (255, 255, 0))
        elif data["category_three"][0]["questions"][0]["color"] == "red":
            text = font.render(data["category_three"][0]["questions"][0]["points"], True, (255, 0, 0))
        else:
            text = font.render(data["category_three"][0]["questions"][0]["points"], True, (169, 169, 169))
        cat_three_one_t = text.get_rect(center=cat_three_one.center)
        screen.blit(text, cat_three_one_t)
        pygame.draw.rect(screen, (0, 0, 255), cat_three_two)
        if data["category_three"][0]["questions"][1]["color"] == "yellow":
            text = font.render(data["category_three"][0]["questions"][1]["points"], True, (255, 255, 0))
        elif data["category_three"][0]["questions"][1]["color"] == "red":
            text = font.render(data["category_three"][0]["questions"][1]["points"], True, (255, 0, 0))  
        else:
            text = font.render(data["category_three"][0]["questions"][1]["points"], True, (169, 169, 169))
        cat_three_two_t = text.get_rect(center=cat_three_two.center)
        screen.blit(text, cat_three_two_t)
        pygame.draw.rect(screen, (0, 0, 255), cat_three_three)
        if data["category_three"][0]["questions"][2]["color"] == "yellow":
            text = font.render(data["category_three"][0]["questions"][2]["points"], True, (255, 255, 0))
        elif data["category_three"][0]["questions"][2]["color"] == "red":
            text = font.render(data["category_three"][0]["questions"][2]["points"], True, (255, 0, 0))
        else:
            text = font.render(data["category_three"][0]["questions"][2]["points"], True, (169, 169, 169))
        cat_three_three_t = text.get_rect(center=cat_three_three.center)
        screen.blit(text, cat_three_three_t)
        pygame.draw.rect(screen, (0, 0, 255), cat_three_four)
        if data["category_three"][0]["questions"][3]["color"] == "yellow":
            text = font.render(data["category_three"][0]["questions"][3]["points"], True, (255, 255, 0))
        elif data["category_three"][0]["questions"][3]["color"] == "red":
            text = font.render(data["category_three"][0]["questions"][3]["points"], True, (255, 0, 0))
        else:
            text = font.render(data["category_three"][0]["questions"][3]["points"], True, (169, 169, 169))
        cat_three_four_t = text.get_rect(center=cat_three_four.center)
        screen.blit(text, cat_three_four_t)
        pygame.draw.rect(screen, (0, 0, 255), cat_three_five)
        if data["category_three"][0]["questions"][4]["color"] == "yellow":
            text = font.render(data["category_three"][0]["questions"][4]["points"], True, (255, 255, 0))
        elif data["category_three"][0]["questions"][4]["color"] == "red":
            text = font.render(data["category_three"][0]["questions"][4]["points"], True, (255, 0, 0))
        else:
            text = font.render(data["category_three"][0]["questions"][4]["points"], True, (169, 169, 169))
        cat_three_five_t = text.get_rect(center=cat_three_five.center)
        screen.blit(text, cat_three_five_t)

        pygame.draw.rect(screen, (0, 0, 255), cat_four_sub)
        text = font.render(data["category_four"][0]["name"], True, (255, 255, 0))
        cat_four_sub_t = text.get_rect(center=cat_four_sub.center)
        screen.blit(text, cat_four_sub_t)
        pygame.draw.rect(screen, (0, 0, 255), cat_four_one)
        if data["category_four"][0]["questions"][0]["color"] == "yellow":
            text = font.render(data["category_four"][0]["questions"][0]["points"], True, (255, 255, 0))
        elif data["category_four"][0]["questions"][0]["color"] == "red":
            text = font.render(data["category_four"][0]["questions"][0]["points"], True, (255, 0, 0))
        else:
            text = font.render(data["category_four"][0]["questions"][0]["points"], True, (169, 169, 169))
        cat_four_one_t = text.get_rect(center=cat_four_one.center)
        screen.blit(text, cat_four_one_t)
        pygame.draw.rect(screen, (0, 0, 255), cat_four_two)
        if data["category_four"][0]["questions"][1]["color"] == "yellow":
            text = font.render(data["category_four"][0]["questions"][1]["points"], True, (255, 255, 0))
        elif data["category_four"][0]["questions"][1]["color"] == "red":
            text = font.render(data["category_four"][0]["questions"][1]["points"], True, (255, 0, 0))
        else:
            text = font.render(data["category_four"][0]["questions"][1]["points"], True, (169, 169, 169))
        cat_four_two_t = text.get_rect(center=cat_four_two.center)
        screen.blit(text, cat_four_two_t)
        pygame.draw.rect(screen, (0, 0, 255), cat_four_three)
        if data["category_four"][0]["questions"][2]["color"] == "yellow":
            text = font.render(data["category_four"][0]["questions"][2]["points"], True, (255, 255, 0))
        elif data["category_four"][0]["questions"][2]["color"] == "red":
            text = font.render(data["category_four"][0]["questions"][2]["points"], True, (255, 0, 0))
        else:
            text = font.render(data["category_four"][0]["questions"][2]["points"], True, (169, 169, 169))
        cat_four_three_t = text.get_rect(center=cat_four_three.center)
        screen.blit(text, cat_four_three_t)
        pygame.draw.rect(screen, (0, 0, 255), cat_four_four)
        if data["category_four"][0]["questions"][3]["color"] == "yellow":
            text = font.render(data["category_four"][0]["questions"][3]["points"], True, (255, 255, 0))
        elif data["category_four"][0]["questions"][3]["color"] == "red":
            text = font.render(data["category_four"][0]["questions"][3]["points"], True, (255, 0, 0))
        else:
            text = font.render(data["category_four"][0]["questions"][3]["points"], True, (169, 169, 169))
        cat_four_four_t = text.get_rect(center=cat_four_four.center)
        screen.blit(text, cat_four_four_t)
        pygame.draw.rect(screen, (0, 0, 255), cat_four_five)
        if data["category_four"][0]["questions"][4]["color"] == "yellow":
            text = font.render(data["category_four"][0]["questions"][4]["points"], True, (255, 255, 0))
        elif data["category_four"][0]["questions"][4]["color"] == "red":
            text = font.render(data["category_four"][0]["questions"][4]["points"], True, (255, 0, 0))
        else:
            text = font.render(data["category_four"][0]["questions"][4]["points"], True, (169, 169, 169))
        cat_four_five_t = text.get_rect(center=cat_four_five.center)
        screen.blit(text, cat_four_five_t)

        pygame.draw.rect(screen, (0, 0, 255), cat_five_sub)
        text = font.render(data["category_five"][0]["name"], True, (255, 255, 0))
        cat_five_sub_t = text.get_rect(center=cat_five_sub.center)
        screen.blit(text, cat_five_sub_t)
        pygame.draw.rect(screen, (0, 0, 255), cat_five_one)
        if data["category_five"][0]["questions"][0]["color"] == "yellow":
            text = font.render(data["category_five"][0]["questions"][0]["points"], True, (255, 255, 0))
        elif data["category_five"][0]["questions"][0]["color"] == "red":
            text = font.render(data["category_five"][0]["questions"][0]["points"], True, (255, 0, 0))
        else:
            text = font.render(data["category_five"][0]["questions"][0]["points"], True, (169, 169, 169))
        cat_five_one_t = text.get_rect(center=cat_five_one.center)
        screen.blit(text, cat_five_one_t)
        pygame.draw.rect(screen, (0, 0, 255), cat_five_two)
        if data["category_five"][0]["questions"][1]["color"] == "yellow":
            text = font.render(data["category_five"][0]["questions"][1]["points"], True, (255, 255, 0))
        elif data["category_five"][0]["questions"][1]["color"] == "red":
            text = font.render(data["category_five"][0]["questions"][1]["points"], True, (255, 0, 0))   
        else:
            text = font.render(data["category_five"][0]["questions"][1]["points"], True, (169, 169, 169))
        cat_five_two_t = text.get_rect(center=cat_five_two.center)
        screen.blit(text, cat_five_two_t)
        pygame.draw.rect(screen, (0, 0, 255), cat_five_three)
        if data["category_five"][0]["questions"][2]["color"] == "yellow":
            text = font.render(data["category_five"][0]["questions"][2]["points"], True, (255, 255, 0))
        elif data["category_five"][0]["questions"][2]["color"] == "red":
            text = font.render(data["category_five"][0]["questions"][2]["points"], True, (255, 0, 0))
        else:
            text = font.render(data["category_five"][0]["questions"][2]["points"], True, (169, 169, 169))
        cat_five_three_t = text.get_rect(center=cat_five_three.center)
        screen.blit(text, cat_five_three_t)
        pygame.draw.rect(screen, (0, 0, 255), cat_five_four)
        if data["category_five"][0]["questions"][3]["color"] == "yellow":
            text = font.render(data["category_five"][0]["questions"][3]["points"], True, (255, 255, 0))
        elif data["category_five"][0]["questions"][3]["color"] == "red":
            text = font.render(data["category_five"][0]["questions"][3]["points"], True, (255, 0, 0))
        else:
            text = font.render(data["category_five"][0]["questions"][3]["points"], True, (169, 169, 169))
        cat_five_four_t = text.get_rect(center=cat_five_four.center)
        screen.blit(text, cat_five_four_t)
        pygame.draw.rect(screen, (0, 0, 255), cat_five_five)
        if data["category_five"][0]["questions"][4]["color"] == "yellow":
            text = font.render(data["category_five"][0]["questions"][4]["points"], True, (255, 255, 0))
        elif data["category_five"][0]["questions"][4]["color"] == "red":
            text = font.render(data["category_five"][0]["questions"][4]["points"], True, (255, 0, 0))
        else:
            text = font.render(data["category_five"][0]["questions"][4]["points"], True, (169, 169, 169))
        cat_five_five_t = text.get_rect(center=cat_five_five.center)
        screen.blit(text, cat_five_five_t)


        pygame.draw.rect(screen, (0, 0, 0), colum_one)
        pygame.draw.rect(screen, (0, 0, 0), colum_two)
        pygame.draw.rect(screen, (0, 0, 0), colum_three)
        pygame.draw.rect(screen, (0, 0, 0), colum_four)

        pygame.draw.rect(screen, (0, 0, 0), row_one)
        pygame.draw.rect(screen, (0, 0, 0), row_two)
        pygame.draw.rect(screen, (0, 0, 0), row_three)
        pygame.draw.rect(screen, (0, 0, 0), row_four)
        pygame.draw.rect(screen, (0, 0, 0), row_five)

    if phase == "board_two":
        pygame.draw.rect(screen, (0, 0, 255), cat_six_sub)
        text = font.render(data["category_six"][0]["name"], True, (255, 255, 0))
        cat_six_sub_t = text.get_rect(center=cat_six_sub.center)
        screen.blit(text, cat_six_sub_t)
        pygame.draw.rect(screen, (0, 0, 255), cat_six_one)
        if data["category_six"][0]["questions"][0]["color"] == "yellow":
            text = font.render(data["category_six"][0]["questions"][0]["points"], True, (255, 255, 0))
        elif data["category_six"][0]["questions"][0]["color"] == "red":
            text = font.render(data["category_six"][0]["questions"][0]["points"], True, (255, 0, 0))
        else:
            text = font.render(data["category_six"][0]["questions"][0]["points"], True, (169, 169, 169))
        cat_six_one_t = text.get_rect(center=cat_six_one.center)
        screen.blit(text, cat_six_one_t)
        pygame.draw.rect(screen, (0, 0, 255), cat_six_two)
        if data["category_six"][0]["questions"][1]["color"] == "yellow":
            text = font.render(data["category_six"][0]["questions"][1]["points"], True, (255, 255, 0))
        elif data["category_six"][0]["questions"][1]["color"] == "red":
            text = font.render(data["category_six"][0]["questions"][1]["points"], True, (255, 0, 0))
        else:
            text = font.render(data["category_six"][0]["questions"][1]["points"], True, (169, 169, 169))
        cat_six_two_t = text.get_rect(center=cat_six_two.center)
        screen.blit(text, cat_six_two_t)
        pygame.draw.rect(screen, (0, 0, 255), cat_six_three)
        if data["category_six"][0]["questions"][2]["color"] == "yellow":
            text = font.render(data["category_six"][0]["questions"][2]["points"], True, (255, 255, 0))
        elif data["category_six"][0]["questions"][2]["color"] == "red":
            text = font.render(data["category_six"][0]["questions"][2]["points"], True, (255, 0, 0))
        else:
            text = font.render(data["category_six"][0]["questions"][2]["points"], True, (169, 169, 169))
        cat_six_three_t = text.get_rect(center=cat_six_three.center)
        screen.blit(text, cat_six_three_t)
        pygame.draw.rect(screen, (0, 0, 255), cat_six_four)
        if data["category_six"][0]["questions"][3]["color"] == "yellow":
            text = font.render(data["category_six"][0]["questions"][3]["points"], True, (255, 255, 0))
        elif data["category_six"][0]["questions"][3]["color"] == "red":
            text = font.render(data["category_six"][0]["questions"][3]["points"], True, (255, 0, 0))
        else:
            text = font.render(data["category_six"][0]["questions"][3]["points"], True, (169, 169, 169))
        cat_six_four_t = text.get_rect(center=cat_six_four.center)
        screen.blit(text, cat_six_four_t)
        pygame.draw.rect(screen, (0, 0, 255), cat_six_five)
        if data["category_six"][0]["questions"][4]["color"] == "yellow":
            text = font.render(data["category_six"][0]["questions"][4]["points"], True, (255, 255, 0))
        elif data["category_six"][0]["questions"][4]["color"] == "red":
            text = font.render(data["category_six"][0]["questions"][4]["points"], True, (255, 0, 0))
        else:
            text = font.render(data["category_six"][0]["questions"][4]["points"], True, (169, 169, 169))
        cat_six_five_t = text.get_rect(center=cat_six_five.center)
        screen.blit(text, cat_six_five_t)

        pygame.draw.rect(screen, (0, 0, 255), cat_seven_sub)
        text = font.render(data["category_seven"][0]["name"], True, (255, 255, 0))
        cat_seven_sub_t = text.get_rect(center=cat_seven_sub.center)
        screen.blit(text, cat_seven_sub_t)
        pygame.draw.rect(screen, (0, 0, 255), cat_seven_one)
        if data["category_seven"][0]["questions"][0]["color"] == "yellow":
            text = font.render(data["category_seven"][0]["questions"][0]["points"], True, (255, 255, 0))
        elif data["category_seven"][0]["questions"][0]["color"] == "red":
            text = font.render(data["category_seven"][0]["questions"][0]["points"], True, (255, 0, 0))
        else:
            text = font.render(data["category_seven"][0]["questions"][0]["points"], True, (169, 169, 169))
        cat_seven_one_t = text.get_rect(center=cat_seven_one.center)
        screen.blit(text, cat_seven_one_t)
        pygame.draw.rect(screen, (0, 0, 255), cat_seven_two)
        if data["category_seven"][0]["questions"][1]["color"] == "yellow":
            text = font.render(data["category_seven"][0]["questions"][1]["points"], True, (255, 255, 0))
        elif data["category_seven"][0]["questions"][1]["color"] == "red":
            text = font.render(data["category_seven"][0]["questions"][1]["points"], True, (255, 0, 0))
        else:
            text = font.render(data["category_seven"][0]["questions"][1]["points"], True, (169, 169, 169))
        cat_seven_two_t = text.get_rect(center=cat_seven_two.center)
        screen.blit(text, cat_seven_two_t)
        pygame.draw.rect(screen, (0, 0, 255), cat_seven_three)
        if data["category_seven"][0]["questions"][2]["color"] == "yellow":
            text = font.render(data["category_seven"][0]["questions"][2]["points"], True, (255, 255, 0))
        elif data["category_seven"][0]["questions"][2]["color"] == "red":
            text = font.render(data["category_seven"][0]["questions"][2]["points"], True, (255, 0, 0))
        else:
            text = font.render(data["category_seven"][0]["questions"][2]["points"], True, (169, 169, 169))
        cat_seven_three_t = text.get_rect(center=cat_seven_three.center)
        screen.blit(text, cat_seven_three_t)
        pygame.draw.rect(screen, (0, 0, 255), cat_seven_four)
        if data["category_seven"][0]["questions"][3]["color"] == "yellow":
            text = font.render(data["category_seven"][0]["questions"][3]["points"], True, (255, 255, 0))
        elif data["category_seven"][0]["questions"][3]["color"] == "red":
            text = font.render(data["category_seven"][0]["questions"][3]["points"], True, (255, 0, 0))
        else:
            text = font.render(data["category_seven"][0]["questions"][3]["points"], True, (169, 169, 169))
        cat_seven_four_t = text.get_rect(center=cat_seven_four.center)
        screen.blit(text, cat_seven_four_t)
        pygame.draw.rect(screen, (0, 0, 255), cat_seven_five)
        if data["category_seven"][0]["questions"][4]["color"] == "yellow":
            text = font.render(data["category_seven"][0]["questions"][4]["points"], True, (255, 255, 0))
        elif data["category_seven"][0]["questions"][4]["color"] == "red":
            text = font.render(data["category_seven"][0]["questions"][4]["points"], True, (255, 0, 0))
        else:
            text = font.render(data["category_seven"][0]["questions"][4]["points"], True, (169, 169, 169))
        cat_seven_five_t = text.get_rect(center=cat_seven_five.center)
        screen.blit(text, cat_seven_five_t)

        pygame.draw.rect(screen, (0, 0, 255), cat_eight_sub)
        text = font.render(data["category_eight"][0]["name"], True, (255, 255, 0))
        cat_eight_sub_t = text.get_rect(center=cat_eight_sub.center)
        screen.blit(text, cat_eight_sub_t)
        pygame.draw.rect(screen, (0, 0, 255), cat_eight_one)
        if data["category_eight"][0]["questions"][0]["color"] == "yellow":
            text = font.render(data["category_eight"][0]["questions"][0]["points"], True, (255, 255, 0))
        elif data["category_eight"][0]["questions"][0]["color"] == "red":
            text = font.render(data["category_eight"][0]["questions"][0]["points"], True, (255, 0, 0))
        else:
            text = font.render(data["category_eight"][0]["questions"][0]["points"], True, (169, 169, 169))
        cat_eight_one_t = text.get_rect(center=cat_eight_one.center)
        screen.blit(text, cat_eight_one_t)
        pygame.draw.rect(screen, (0, 0, 255), cat_eight_two)
        if data["category_eight"][0]["questions"][1]["color"] == "yellow":
            text = font.render(data["category_eight"][0]["questions"][1]["points"], True, (255, 255, 0))
        elif data["category_eight"][0]["questions"][1]["color"] == "red":
            text = font.render(data["category_eight"][0]["questions"][1]["points"], True, (255, 0, 0))  
        else:
            text = font.render(data["category_eight"][0]["questions"][1]["points"], True, (169, 169, 169))
        cat_eight_two_t = text.get_rect(center=cat_eight_two.center)
        screen.blit(text, cat_eight_two_t)
        pygame.draw.rect(screen, (0, 0, 255), cat_eight_three)
        if data["category_eight"][0]["questions"][2]["color"] == "yellow":
            text = font.render(data["category_eight"][0]["questions"][2]["points"], True, (255, 255, 0))
        elif data["category_eight"][0]["questions"][2]["color"] == "red":
            text = font.render(data["category_eight"][0]["questions"][2]["points"], True, (255, 0, 0))
        else:
            text = font.render(data["category_eight"][0]["questions"][2]["points"], True, (169, 169, 169))
        cat_eight_three_t = text.get_rect(center=cat_eight_three.center)
        screen.blit(text, cat_eight_three_t)
        pygame.draw.rect(screen, (0, 0, 255), cat_eight_four)
        if data["category_eight"][0]["questions"][3]["color"] == "yellow":
            text = font.render(data["category_eight"][0]["questions"][3]["points"], True, (255, 255, 0))
        elif data["category_eight"][0]["questions"][3]["color"] == "red":
            text = font.render(data["category_eight"][0]["questions"][3]["points"], True, (255, 0, 0))
        else:
            text = font.render(data["category_eight"][0]["questions"][3]["points"], True, (169, 169, 169))
        cat_eight_four_t = text.get_rect(center=cat_eight_four.center)
        screen.blit(text, cat_eight_four_t)
        pygame.draw.rect(screen, (0, 0, 255), cat_eight_five)
        if data["category_eight"][0]["questions"][4]["color"] == "yellow":
            text = font.render(data["category_eight"][0]["questions"][4]["points"], True, (255, 255, 0))
        elif data["category_eight"][0]["questions"][4]["color"] == "red":
            text = font.render(data["category_eight"][0]["questions"][4]["points"], True, (255, 0, 0))
        else:
            text = font.render(data["category_eight"][0]["questions"][4]["points"], True, (169, 169, 169))
        cat_eight_five_t = text.get_rect(center=cat_eight_five.center)
        screen.blit(text, cat_eight_five_t)

        pygame.draw.rect(screen, (0, 0, 255), cat_nine_sub)
        text = font.render(data["category_nine"][0]["name"], True, (255, 255, 0))
        cat_nine_sub_t = text.get_rect(center=cat_nine_sub.center)
        screen.blit(text, cat_nine_sub_t)
        pygame.draw.rect(screen, (0, 0, 255), cat_nine_one)
        if data["category_nine"][0]["questions"][0]["color"] == "yellow":
            text = font.render(data["category_nine"][0]["questions"][0]["points"], True, (255, 255, 0))
        elif data["category_nine"][0]["questions"][0]["color"] == "red":
            text = font.render(data["category_nine"][0]["questions"][0]["points"], True, (255, 0, 0))
        else:
            text = font.render(data["category_nine"][0]["questions"][0]["points"], True, (169, 169, 169))
        cat_nine_one_t = text.get_rect(center=cat_nine_one.center)
        screen.blit(text, cat_nine_one_t)
        pygame.draw.rect(screen, (0, 0, 255), cat_nine_two)
        if data["category_nine"][0]["questions"][1]["color"] == "yellow":
            text = font.render(data["category_nine"][0]["questions"][1]["points"], True, (255, 255, 0))
        elif data["category_nine"][0]["questions"][1]["color"] == "red":
            text = font.render(data["category_nine"][0]["questions"][1]["points"], True, (255, 0, 0))
        else:
            text = font.render(data["category_nine"][0]["questions"][1]["points"], True, (169, 169, 169))
        cat_nine_two_t = text.get_rect(center=cat_nine_two.center)
        screen.blit(text, cat_nine_two_t)
        pygame.draw.rect(screen, (0, 0, 255), cat_nine_three)
        if data["category_nine"][0]["questions"][2]["color"] == "yellow":
            text = font.render(data["category_nine"][0]["questions"][2]["points"], True, (255, 255, 0))
        elif data["category_nine"][0]["questions"][2]["color"] == "red":
            text = font.render(data["category_nine"][0]["questions"][2]["points"], True, (255, 0, 0))
        else:
            text = font.render(data["category_nine"][0]["questions"][2]["points"], True, (169, 169, 169))
        cat_nine_three_t = text.get_rect(center=cat_nine_three.center)
        screen.blit(text, cat_nine_three_t)
        pygame.draw.rect(screen, (0, 0, 255), cat_nine_four)
        if data["category_nine"][0]["questions"][3]["color"] == "yellow":
            text = font.render(data["category_nine"][0]["questions"][3]["points"], True, (255, 255, 0))
        elif data["category_nine"][0]["questions"][3]["color"] == "red":
            text = font.render(data["category_nine"][0]["questions"][3]["points"], True, (255, 0, 0))
        else:
            text = font.render(data["category_nine"][0]["questions"][3]["points"], True, (169, 169, 169))
        cat_nine_four_t = text.get_rect(center=cat_nine_four.center)
        screen.blit(text, cat_nine_four_t)
        pygame.draw.rect(screen, (0, 0, 255), cat_nine_five)
        if data["category_nine"][0]["questions"][4]["color"] == "yellow":
            text = font.render(data["category_nine"][0]["questions"][4]["points"], True, (255, 255, 0))
        elif data["category_nine"][0]["questions"][4]["color"] == "red":
            text = font.render(data["category_nine"][0]["questions"][4]["points"], True, (255, 0, 0))
        else:
            text = font.render(data["category_nine"][0]["questions"][4]["points"], True, (169, 169, 169))
        cat_nine_five_t = text.get_rect(center=cat_nine_five.center)
        screen.blit(text, cat_nine_five_t)

        pygame.draw.rect(screen, (0, 0, 255), cat_ten_sub)
        text = font.render(data["category_ten"][0]["name"], True, (255, 255, 0))
        cat_ten_sub_t = text.get_rect(center=cat_ten_sub.center)
        screen.blit(text, cat_ten_sub_t)
        pygame.draw.rect(screen, (0, 0, 255), cat_ten_one)
        if data["category_ten"][0]["questions"][0]["color"] == "yellow":
            text = font.render(data["category_ten"][0]["questions"][0]["points"], True, (255, 255, 0))
        elif data["category_ten"][0]["questions"][0]["color"] == "red":
            text = font.render(data["category_ten"][0]["questions"][0]["points"], True, (255, 0, 0))
        else:
            text = font.render(data["category_ten"][0]["questions"][0]["points"], True, (169, 169, 169))
        cat_ten_one_t = text.get_rect(center=cat_ten_one.center)
        screen.blit(text, cat_ten_one_t)
        pygame.draw.rect(screen, (0, 0, 255), cat_ten_two)
        if data["category_ten"][0]["questions"][1]["color"] == "yellow":
            text = font.render(data["category_ten"][0]["questions"][1]["points"], True, (255, 255, 0))
        elif data["category_ten"][0]["questions"][1]["color"] == "red":
            text = font.render(data["category_ten"][0]["questions"][1]["points"], True, (255, 0, 0))   
        else:
            text = font.render(data["category_ten"][0]["questions"][1]["points"], True, (169, 169, 169))
        cat_ten_two_t = text.get_rect(center=cat_ten_two.center)
        screen.blit(text, cat_ten_two_t)
        pygame.draw.rect(screen, (0, 0, 255), cat_ten_three)
        if data["category_ten"][0]["questions"][2]["color"] == "yellow":
            text = font.render(data["category_ten"][0]["questions"][2]["points"], True, (255, 255, 0))
        elif data["category_ten"][0]["questions"][2]["color"] == "red":
            text = font.render(data["category_ten"][0]["questions"][2]["points"], True, (255, 0, 0))
        else:
            text = font.render(data["category_ten"][0]["questions"][2]["points"], True, (169, 169, 169))
        cat_ten_three_t = text.get_rect(center=cat_ten_three.center)
        screen.blit(text, cat_ten_three_t)
        pygame.draw.rect(screen, (0, 0, 255), cat_ten_four)
        if data["category_ten"][0]["questions"][3]["color"] == "yellow":
            text = font.render(data["category_ten"][0]["questions"][3]["points"], True, (255, 255, 0))
        elif data["category_ten"][0]["questions"][3]["color"] == "red":
            text = font.render(data["category_ten"][0]["questions"][3]["points"], True, (255, 0, 0))
        else:
            text = font.render(data["category_ten"][0]["questions"][3]["points"], True, (169, 169, 169))
        cat_ten_four_t = text.get_rect(center=cat_ten_four.center)
        screen.blit(text, cat_ten_four_t)
        pygame.draw.rect(screen, (0, 0, 255), cat_ten_five)
        if data["category_ten"][0]["questions"][4]["color"] == "yellow":
            text = font.render(data["category_ten"][0]["questions"][4]["points"], True, (255, 255, 0))
        elif data["category_ten"][0]["questions"][4]["color"] == "red":
            text = font.render(data["category_ten"][0]["questions"][4]["points"], True, (255, 0, 0))
        else:
            text = font.render(data["category_ten"][0]["questions"][4]["points"], True, (169, 169, 169))
        cat_ten_five_t = text.get_rect(center=cat_ten_five.center)
        screen.blit(text, cat_ten_five_t)


        pygame.draw.rect(screen, (0, 0, 0), colum_one)
        pygame.draw.rect(screen, (0, 0, 0), colum_two)
        pygame.draw.rect(screen, (0, 0, 0), colum_three)
        pygame.draw.rect(screen, (0, 0, 0), colum_four)

        pygame.draw.rect(screen, (0, 0, 0), row_one)
        pygame.draw.rect(screen, (0, 0, 0), row_two)
        pygame.draw.rect(screen, (0, 0, 0), row_three)
        pygame.draw.rect(screen, (0, 0, 0), row_four)
        pygame.draw.rect(screen, (0, 0, 0), row_five)






    if phase == "question":
        pygame.draw.rect(screen, (0, 0, 255), non_board_bg)
        if q == "1-1":
            text = font.render(data["category_one"][0]["questions"][0]["question"], True, (255, 255, 0))
            question_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, question_t)
        elif q == "1-2":
            text = font.render(data["category_one"][0]["questions"][1]["question"], True, (255, 255, 0))
            question_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, question_t)
        elif q == "1-3":
            text = font.render(data["category_one"][0]["questions"][2]["question"], True, (255, 255, 0))
            question_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, question_t)
        elif q == "1-4":
            text = font.render(data["category_one"][0]["questions"][3]["question"], True, (255, 255, 0))
            question_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, question_t)
        elif q == "1-5":
            text = font.render(data["category_one"][0]["questions"][4]["question"], True, (255, 255, 0))
            question_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, question_t)
        elif q == "2-1":
            text = font.render(data["category_two"][0]["questions"][0]["question"], True, (255, 255, 0))
            question_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, question_t)
        elif q == "2-2":
            text = font.render(data["category_two"][0]["questions"][1]["question"], True, (255, 255, 0))
            question_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, question_t)
        elif q == "2-3":
            text = font.render(data["category_two"][0]["questions"][2]["question"], True, (255, 255, 0))
            question_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, question_t)
        elif q == "2-4":
            text = font.render(data["category_two"][0]["questions"][3]["question"], True, (255, 255, 0))
            question_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, question_t)
        elif q == "2-5":
            text = font.render(data["category_two"][0]["questions"][4]["question"], True, (255, 255, 0))
            question_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, question_t)
        elif q == "3-1":
            text = font.render(data["category_three"][0]["questions"][0]["question"], True, (255, 255, 0))
            question_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, question_t)
        elif q == "3-2":
            text = font.render(data["category_three"][0]["questions"][1]["question"], True, (255, 255, 0))
            question_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, question_t)
        elif q == "3-3":
            text = font.render(data["category_three"][0]["questions"][2]["question"], True, (255, 255, 0))
            question_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, question_t)
        elif q == "3-4":
            text = font.render(data["category_three"][0]["questions"][3]["question"], True, (255, 255, 0))
            question_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, question_t)
        elif q == "3-5":
            text = font.render(data["category_three"][0]["questions"][4]["question"], True, (255, 255, 0))
            question_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, question_t)
        elif q == "4-1":
            text = font.render(data["category_four"][0]["questions"][0]["question"], True, (255, 255, 0))
            question_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, question_t)
        elif q == "4-2":
            text = font.render(data["category_four"][0]["questions"][1]["question"], True, (255, 255, 0))
            question_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, question_t)
        elif q == "4-3":
            text = font.render(data["category_four"][0]["questions"][2]["question"], True, (255, 255, 0))
            question_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, question_t)
        elif q == "4-4":
            text = font.render(data["category_four"][0]["questions"][3]["question"], True, (255, 255, 0))
            question_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, question_t)
        elif q == "4-5":
            text = font.render(data["category_four"][0]["questions"][4]["question"], True, (255, 255, 0))
            question_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, question_t)
        elif q == "5-1":
            text = font.render(data["category_five"][0]["questions"][0]["question"], True, (255, 255, 0))
            question_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, question_t)
        elif q == "5-2":
            text = font.render(data["category_five"][0]["questions"][1]["question"], True, (255, 255, 0))
            question_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, question_t)
        elif q == "5-3":
            text = font.render(data["category_five"][0]["questions"][2]["question"], True, (255, 255, 0))
            question_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, question_t)
        elif q == "5-4":
            text = font.render(data["category_five"][0]["questions"][3]["question"], True, (255, 255, 0))
            question_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, question_t)
        elif q == "5-5":
            text = font.render(data["category_five"][0]["questions"][4]["question"], True, (255, 255, 0))
            question_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, question_t)
        elif q == "6-1":
            text = font.render(data["category_six"][0]["questions"][0]["question"], True, (255, 255, 0))
            question_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, question_t)
        elif q == "6-2":
            text = font.render(data["category_six"][0]["questions"][1]["question"], True, (255, 255, 0))
            question_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, question_t)
        elif q == "6-3":
            text = font.render(data["category_six"][0]["questions"][2]["question"], True, (255, 255, 0))
            question_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, question_t)
        elif q == "6-4":
            text = font.render(data["category_six"][0]["questions"][3]["question"], True, (255, 255, 0))
            question_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, question_t)
        elif q == "6-5":
            text = font.render(data["category_six"][0]["questions"][4]["question"], True, (255, 255, 0))
            question_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, question_t)
        elif q == "7-1":
            text = font.render(data["category_seven"][0]["questions"][0]["question"], True, (255, 255, 0))
            question_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, question_t)
        elif q == "7-2":
            text = font.render(data["category_seven"][0]["questions"][1]["question"], True, (255, 255, 0))
            question_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, question_t)
        elif q == "7-3":
            text = font.render(data["category_seven"][0]["questions"][2]["question"], True, (255, 255, 0))
            question_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, question_t)
        elif q == "7-4":
            text = font.render(data["category_seven"][0]["questions"][3]["question"], True, (255, 255, 0))
            question_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, question_t)
        elif q == "7-5":
            text = font.render(data["category_seven"][0]["questions"][4]["question"], True, (255, 255, 0))
            question_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, question_t)
        elif q == "8-1":
            text = font.render(data["category_eight"][0]["questions"][0]["question"], True, (255, 255, 0))
            question_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, question_t)
        elif q == "8-2":
            text = font.render(data["category_eight"][0]["questions"][1]["question"], True, (255, 255, 0))
            question_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, question_t)
        elif q == "8-3":
            text = font.render(data["category_eight"][0]["questions"][2]["question"], True, (255, 255, 0))
            question_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, question_t)
        elif q == "8-4":
            text = font.render(data["category_eight"][0]["questions"][3]["question"], True, (255, 255, 0))
            question_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, question_t)
        elif q == "8-5":
            text = font.render(data["category_eight"][0]["questions"][4]["question"], True, (255, 255, 0))
            question_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, question_t)
        elif q == "9-1":
            text = font.render(data["category_nine"][0]["questions"][0]["question"], True, (255, 255, 0))
            question_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, question_t)
        elif q == "9-2":
            text = font.render(data["category_nine"][0]["questions"][1]["question"], True, (255, 255, 0))
            question_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, question_t)
        elif q == "9-3":
            text = font.render(data["category_nine"][0]["questions"][2]["question"], True, (255, 255, 0))
            question_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, question_t)
        elif q == "9-4":
            text = font.render(data["category_nine"][0]["questions"][3]["question"], True, (255, 255, 0))
            question_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, question_t)
        elif q == "9-5":
            text = font.render(data["category_nine"][0]["questions"][4]["question"], True, (255, 255, 0))
            question_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, question_t)
        elif q == "10-1":
            text = font.render(data["category_ten"][0]["questions"][0]["question"], True, (255, 255, 0))
            question_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, question_t)
        elif q == "10-2":
            text = font.render(data["category_ten"][0]["questions"][1]["question"], True, (255, 255, 0))
            question_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, question_t)
        elif q == "10-3":
            text = font.render(data["category_ten"][0]["questions"][2]["question"], True, (255, 255, 0))
            question_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, question_t)
        elif q == "10-4":
            text = font.render(data["category_ten"][0]["questions"][3]["question"], True, (255, 255, 0))
            question_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, question_t)
        elif q == "10-5":
            text = font.render(data["category_ten"][0]["questions"][4]["question"], True, (255, 255, 0))
            question_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, question_t)


    if phase == "answer":
        pygame.draw.rect(screen, (0, 0, 255), non_board_bg)
        if q == "1-1":
            text = font.render(data["category_one"][0]["questions"][0]["answer"], True, (255, 255, 0))
            answer_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, answer_t)
        elif q == "1-2":
            text = font.render(data["category_one"][0]["questions"][1]["answer"], True, (255, 255, 0))
            answer_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, answer_t)
        elif q == "1-3":
            text = font.render(data["category_one"][0]["questions"][2]["answer"], True, (255, 255, 0))
            answer_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, answer_t)
        elif q == "1-4":
            text = font.render(data["category_one"][0]["questions"][3]["answer"], True, (255, 255, 0))
            answer_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, answer_t)
        elif q == "1-5":
            text = font.render(data["category_one"][0]["questions"][4]["answer"], True, (255, 255, 0))
            answer_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, answer_t)
        elif q == "2-1":
            text = font.render(data["category_two"][0]["questions"][0]["answer"], True, (255, 255, 0))
            answer_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, answer_t)
        elif q == "2-2":
            text = font.render(data["category_two"][0]["questions"][1]["answer"], True, (255, 255, 0))
            answer_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, answer_t)
        elif q == "2-3":
            text = font.render(data["category_two"][0]["questions"][2]["answer"], True, (255, 255, 0))
            answer_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, answer_t)
        elif q == "2-4":
            text = font.render(data["category_two"][0]["questions"][3]["answer"], True, (255, 255, 0))
            answer_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, answer_t)
        elif q == "2-5":
            text = font.render(data["category_two"][0]["questions"][4]["answer"], True, (255, 255, 0))
            answer_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, answer_t)
        elif q == "3-1":
            text = font.render(data["category_three"][0]["questions"][0]["answer"], True, (255, 255, 0))
            answer_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, answer_t)
        elif q == "3-2":
            text = font.render(data["category_three"][0]["questions"][1]["answer"], True, (255, 255, 0))
            answer_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, answer_t)
        elif q == "3-3":
            text = font.render(data["category_three"][0]["questions"][2]["answer"], True, (255, 255, 0))
            answer_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, answer_t)
        elif q == "3-4":
            text = font.render(data["category_three"][0]["questions"][3]["answer"], True, (255, 255, 0))
            answer_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, answer_t)
        elif q == "3-5":
            text = font.render(data["category_three"][0]["questions"][4]["answer"], True, (255, 255, 0))
            answer_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, answer_t)
        elif q == "4-1":
            text = font.render(data["category_four"][0]["questions"][0]["answer"], True, (255, 255, 0))
            answer_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, answer_t)
        elif q == "4-2":
            text = font.render(data["category_four"][0]["questions"][1]["answer"], True, (255, 255, 0))
            answer_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, answer_t)
        elif q == "4-3":
            text = font.render(data["category_four"][0]["questions"][2]["answer"], True, (255, 255, 0))
            answer_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, answer_t)
        elif q == "4-4":
            text = font.render(data["category_four"][0]["questions"][3]["answer"], True, (255, 255, 0))
            answer_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, answer_t)
        elif q == "4-5":
            text = font.render(data["category_four"][0]["questions"][4]["answer"], True, (255, 255, 0))
            answer_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, answer_t)
        elif q == "5-1":
            text = font.render(data["category_five"][0]["questions"][0]["answer"], True, (255, 255, 0))
            answer_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, answer_t)
        elif q == "5-2":
            text = font.render(data["category_five"][0]["questions"][1]["answer"], True, (255, 255, 0))
            answer_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, answer_t)
        elif q == "5-3":
            text = font.render(data["category_five"][0]["questions"][2]["answer"], True, (255, 255, 0))
            answer_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, answer_t)
        elif q == "5-4":
            text = font.render(data["category_five"][0]["questions"][3]["answer"], True, (255, 255, 0))
            answer_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, answer_t)
        elif q == "5-5":
            text = font.render(data["category_five"][0]["questions"][4]["answer"], True, (255, 255, 0))
            answer_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, answer_t)
        elif q == "6-1":
            text = font.render(data["category_six"][0]["questions"][0]["answer"], True, (255, 255, 0))
            answer_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, answer_t)
        elif q == "6-2":
            text = font.render(data["category_six"][0]["questions"][1]["answer"], True, (255, 255, 0))
            answer_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, answer_t)
        elif q == "6-3":
            text = font.render(data["category_six"][0]["questions"][2]["answer"], True, (255, 255, 0))
            answer_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, answer_t)
        elif q == "6-4":
            text = font.render(data["category_six"][0]["questions"][3]["answer"], True, (255, 255, 0))
            answer_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, answer_t)
        elif q == "6-5":
            text = font.render(data["category_six"][0]["questions"][4]["answer"], True, (255, 255, 0))
            answer_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, answer_t)
        elif q == "7-1":
            text = font.render(data["category_seven"][0]["questions"][0]["answer"], True, (255, 255, 0))
            answer_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, answer_t)
        elif q == "7-2":
            text = font.render(data["category_seven"][0]["questions"][1]["answer"], True, (255, 255, 0))
            answer_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, answer_t)
        elif q == "7-3":
            text = font.render(data["category_seven"][0]["questions"][2]["answer"], True, (255, 255, 0))
            answer_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, answer_t)
        elif q == "7-4":
            text = font.render(data["category_seven"][0]["questions"][3]["answer"], True, (255, 255, 0))
            answer_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, answer_t)
        elif q == "7-5":
            text = font.render(data["category_seven"][0]["questions"][4]["answer"], True, (255, 255, 0))
            answer_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, answer_t)
        elif q == "8-1":
            text = font.render(data["category_eight"][0]["questions"][0]["answer"], True, (255, 255, 0))
            answer_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, answer_t)
        elif q == "8-2":
            text = font.render(data["category_eight"][0]["questions"][1]["answer"], True, (255, 255, 0))
            answer_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, answer_t)
        elif q == "8-3":
            text = font.render(data["category_eight"][0]["questions"][2]["answer"], True, (255, 255, 0))
            answer_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, answer_t)
        elif q == "8-4":
            text = font.render(data["category_eight"][0]["questions"][3]["answer"], True, (255, 255, 0))
            answer_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, answer_t)
        elif q == "8-5":
            text = font.render(data["category_eight"][0]["questions"][4]["answer"], True, (255, 255, 0))
            answer_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, answer_t)
        elif q == "9-1":
            text = font.render(data["category_nine"][0]["questions"][0]["answer"], True, (255, 255, 0))
            answer_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, answer_t)
        elif q == "9-2":
            text = font.render(data["category_nine"][0]["questions"][1]["answer"], True, (255, 255, 0))
            answer_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, answer_t)
        elif q == "9-3":
            text = font.render(data["category_nine"][0]["questions"][2]["answer"], True, (255, 255, 0))
            answer_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, answer_t)
        elif q == "9-4":
            text = font.render(data["category_nine"][0]["questions"][3]["answer"], True, (255, 255, 0))
            answer_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, answer_t)
        elif q == "9-5":
            text = font.render(data["category_nine"][0]["questions"][4]["answer"], True, (255, 255, 0))
            answer_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, answer_t)
        elif q == "10-1":
            text = font.render(data["category_ten"][0]["questions"][0]["answer"], True, (255, 255, 0))
            answer_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, answer_t)
        elif q == "10-2":
            text = font.render(data["category_ten"][0]["questions"][1]["answer"], True, (255, 255, 0))
            answer_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, answer_t)
        elif q == "10-3":
            text = font.render(data["category_ten"][0]["questions"][2]["answer"], True, (255, 255, 0))
            answer_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, answer_t)
        elif q == "10-4":
            text = font.render(data["category_ten"][0]["questions"][3]["answer"], True, (255, 255, 0))
            answer_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, answer_t)
        elif q == "10-5":
            text = font.render(data["category_ten"][0]["questions"][4]["answer"], True, (255, 255, 0))
            answer_t = text.get_rect(center=non_board_bg.center)
            screen.blit(text, answer_t)

    if phase == "double":
        pygame.draw.rect(screen, (0, 0, 255), non_board_bg)
        text = font.render("Daily Double!", True, (255, 0, 0))
        answer_t = text.get_rect(center=non_board_bg.center)
        screen.blit(text, answer_t)

    
    key = pygame.key.get_pressed()
    if key[pygame.K_ESCAPE] == True:
        run = False


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:

            if phase == "final":
                if stage == 'category':
                    if non_board_bg.collidepoint(event.pos):
                        stage = "question"
                elif stage == 'question':
                    if non_board_bg.collidepoint(event.pos):
                        stage = "answer"
                elif stage == 'answer':
                    if non_board_bg.collidepoint(event.pos):
                        stage = "end"


            if phase == "answer":
                if non_board_bg.collidepoint(event.pos):
                    if data['second_board_start'] == True:
                        phase = "board_two"
                    else:
                        phase = "board_one"
                    if q == "1-1":
                        data['final'][0]['ready'] = data['final'][0]['ready'].replace("q", "a")
                    elif q == "1-2":
                        data['final'][0]['ready'] = data['final'][0]['ready'].replace("w", "a")
                    elif q == '1-3':
                        data['final'][0]['ready'] = data['final'][0]['ready'].replace("e", "a")
                    elif q == '1-4':
                        data['final'][0]['ready'] = data['final'][0]['ready'].replace("r", "a")
                    elif q == '1-5':
                        data['final'][0]['ready'] = data['final'][0]['ready'].replace("t", "a")
                    elif q == '2-1':
                        data['final'][0]['ready'] = data['final'][0]['ready'].replace("y", "a")
                    elif q == '2-2':
                        data['final'][0]['ready'] = data['final'][0]['ready'].replace("u", "a")
                    elif q == '2-3':
                        data['final'][0]['ready'] = data['final'][0]['ready'].replace("i", "a")
                    elif q == '2-4':
                        data['final'][0]['ready'] = data['final'][0]['ready'].replace("o", "a")
                    elif q == '2-5':
                        data['final'][0]['ready'] = data['final'][0]['ready'].replace("p", "a")
                    elif q == '3-1':
                        data['final'][0]['ready'] = data['final'][0]['ready'].replace("s", "a")
                    elif q == '3-2':
                        data['final'][0]['ready'] = data['final'][0]['ready'].replace("d", "a")
                    elif q == '3-3':
                        data['final'][0]['ready'] = data['final'][0]['ready'].replace("f", "a")
                    elif q == '3-4':
                        data['final'][0]['ready'] = data['final'][0]['ready'].replace("g", "a")
                    elif q == '3-5':
                        data['final'][0]['ready'] = data['final'][0]['ready'].replace("h", "a")
                    elif q == '4-1':
                        data['final'][0]['ready'] = data['final'][0]['ready'].replace("j", "a")
                    elif q == '4-2':
                        data['final'][0]['ready'] = data['final'][0]['ready'].replace("k", "a")
                    elif q == '4-3':
                        data['final'][0]['ready'] = data['final'][0]['ready'].replace("l", "a")
                    elif q == '4-4':
                        data['final'][0]['ready'] = data['final'][0]['ready'].replace("z", "a")
                    elif q == '4-5':
                        data['final'][0]['ready'] = data['final'][0]['ready'].replace("x", "a")
                    elif q == '5-1':
                        data['final'][0]['ready'] = data['final'][0]['ready'].replace("c", "a")
                    elif q == '5-2':
                        data['final'][0]['ready'] = data['final'][0]['ready'].replace("v", "a")
                    elif q == '5-3':
                        data['final'][0]['ready'] = data['final'][0]['ready'].replace("b", "a")
                    elif q == '5-4':
                        data['final'][0]['ready'] = data['final'][0]['ready'].replace("n", "a")
                    elif q == '5-5':
                        data['final'][0]['ready'] = data['final'][0]['ready'].replace("m", "a")
                    elif q == "6-1":
                        data['final'][0]['ready'] = data['final'][0]['ready'].replace("q", "a")
                    elif q == "6-2":
                        data['final'][0]['ready'] = data['final'][0]['ready'].replace("w", "a")
                    elif q == '6-3':
                        data['final'][0]['ready'] = data['final'][0]['ready'].replace("e", "a")
                    elif q == '6-4':
                        data['final'][0]['ready'] = data['final'][0]['ready'].replace("r", "a")
                    elif q == '6-5':
                        data['final'][0]['ready'] = data['final'][0]['ready'].replace("t", "a")
                    elif q == '7-1':
                        data['final'][0]['ready'] = data['final'][0]['ready'].replace("y", "a")
                    elif q == '7-2':
                        data['final'][0]['ready'] = data['final'][0]['ready'].replace("u", "a")
                    elif q == '7-3':
                        data['final'][0]['ready'] = data['final'][0]['ready'].replace("i", "a")
                    elif q == '7-4':
                        data['final'][0]['ready'] = data['final'][0]['ready'].replace("o", "a")
                    elif q == '7-5':
                        data['final'][0]['ready'] = data['final'][0]['ready'].replace("p", "a")
                    elif q == '8-1':
                        data['final'][0]['ready'] = data['final'][0]['ready'].replace("s", "a")
                    elif q == '8-2':
                        data['final'][0]['ready'] = data['final'][0]['ready'].replace("d", "a")
                    elif q == '8-3':
                        data['final'][0]['ready'] = data['final'][0]['ready'].replace("f", "a")
                    elif q == '8-4':
                        data['final'][0]['ready'] = data['final'][0]['ready'].replace("g", "a")
                    elif q == '8-5':
                        data['final'][0]['ready'] = data['final'][0]['ready'].replace("h", "a")
                    elif q == '9-1':
                        data['final'][0]['ready'] = data['final'][0]['ready'].replace("j", "a")
                    elif q == '9-2':
                        data['final'][0]['ready'] = data['final'][0]['ready'].replace("k", "a")
                    elif q == '9-3':
                        data['final'][0]['ready'] = data['final'][0]['ready'].replace("l", "a")
                    elif q == '9-4':
                        data['final'][0]['ready'] = data['final'][0]['ready'].replace("z", "a")
                    elif q == '9-5':
                        data['final'][0]['ready'] = data['final'][0]['ready'].replace("x", "a")
                    elif q == '10-1':
                        data['final'][0]['ready'] = data['final'][0]['ready'].replace("c", "a")
                    elif q == '10-2':
                        data['final'][0]['ready'] = data['final'][0]['ready'].replace("v", "a")
                    elif q == '10-3':
                        data['final'][0]['ready'] = data['final'][0]['ready'].replace("b", "a")
                    elif q == '10-4':
                        data['final'][0]['ready'] = data['final'][0]['ready'].replace("n", "a")
                    elif q == '10-5':
                        data['final'][0]['ready'] = data['final'][0]['ready'].replace("m", "a")
                continue


            if phase == "question":
                if non_board_bg.collidepoint(event.pos):
                    phase = "answer"
                continue

            if phase == "double":
                if non_board_bg.collidepoint(event.pos):
                    phase = "question"
                continue

            if phase == "board_one":
                if cat_one_one.collidepoint(event.pos):
                    phase = "question"
                    data["category_one"][0]["questions"][0]["color"] = "grey"
                    if data["category_one"][0]["questions"][0]["double"] == True:
                        phase = "double"
                        data["category_one"][0]["questions"][0]["color"] = "red"
                    q = "1-1"
                elif cat_one_two.collidepoint(event.pos):
                    phase = "question"
                    data["category_one"][0]["questions"][1]["color"] = "grey"
                    if data["category_one"][0]["questions"][1]["double"] == True:
                        phase = "double"
                        data["category_one"][0]["questions"][1]["color"] = "red"
                    q = "1-2"
                elif cat_one_three.collidepoint(event.pos):
                    phase = "question"
                    data["category_one"][0]["questions"][2]["color"] = "grey"
                    if data["category_one"][0]["questions"][2]["double"] == True:
                        phase = "double"
                        data["category_one"][0]["questions"][2]["color"] = "red"
                    q = "1-3"
                elif cat_one_four.collidepoint(event.pos):
                    phase = "question"
                    data["category_one"][0]["questions"][3]["color"] = "grey"
                    if data["category_one"][0]["questions"][3]["double"] == True:
                        phase = "double"
                        data["category_one"][0]["questions"][3]["color"] = "red"
                    q = "1-4"
                elif cat_one_five.collidepoint(event.pos):
                    phase = "question"
                    data["category_one"][0]["questions"][4]["color"] = "grey"
                    if data["category_one"][0]["questions"][4]["double"] == True:
                        phase = "double"
                        data["category_one"][0]["questions"][4]["color"] = "red"
                    q = "1-5"
                elif cat_two_one.collidepoint(event.pos):
                    phase = "question"
                    data["category_two"][0]["questions"][0]["color"] = "grey"
                    if data["category_two"][0]["questions"][0]["double"] == True:
                        phase = "double"
                        data["category_two"][0]["questions"][0]["color"] = "red"
                    q = "2-1"
                elif cat_two_two.collidepoint(event.pos):
                    phase = "question"
                    data["category_two"][0]["questions"][1]["color"] = "grey"
                    if data["category_two"][0]["questions"][1]["double"] == True:
                        phase = "double"
                        data["category_two"][0]["questions"][1]["color"] = "red"
                    q = "2-2"
                elif cat_two_three.collidepoint(event.pos):
                    phase = "question"
                    data["category_two"][0]["questions"][2]["color"] = "grey"
                    if data["category_two"][0]["questions"][2]["double"] == True:
                        phase = "double"
                        data["category_two"][0]["questions"][2]["color"] = "red"
                    q = "2-3"
                elif cat_two_four.collidepoint(event.pos):
                    phase = "question"
                    data["category_two"][0]["questions"][3]["color"] = "grey"
                    if data["category_two"][0]["questions"][3]["double"] == True:
                        phase = "double"
                        data["category_two"][0]["questions"][3]["color"] = "red"
                    q = "2-4"
                elif cat_two_five.collidepoint(event.pos):
                    phase = "question"
                    data["category_two"][0]["questions"][4]["color"] = "grey"
                    if data["category_two"][0]["questions"][4]["double"] == True:
                        phase = "double"
                        data["category_two"][0]["questions"][4]["color"] = "red"
                    q = "2-5"
                elif cat_three_one.collidepoint(event.pos):
                    phase = "question"
                    data["category_three"][0]["questions"][0]["color"] = "grey"
                    if data["category_three"][0]["questions"][0]["double"] == True:
                        phase = "double"
                        data["category_three"][0]["questions"][0]["color"] = "red"
                    q = "3-1"
                elif cat_three_two.collidepoint(event.pos):
                    phase = "question"
                    data["category_three"][0]["questions"][1]["color"] = "grey"
                    if data["category_three"][0]["questions"][1]["double"] == True:
                        phase = "double"
                        data["category_three"][0]["questions"][1]["color"] = "red"
                    q = "3-2"
                elif cat_three_three.collidepoint(event.pos):
                    phase = "question"
                    data["category_three"][0]["questions"][2]["color"] = "grey"
                    if data["category_three"][0]["questions"][2]["double"] == True:
                        phase = "double"
                        data["category_three"][0]["questions"][2]["color"] = "red"
                    q = "3-3"
                elif cat_three_four.collidepoint(event.pos):
                    phase = "question"
                    data["category_three"][0]["questions"][3]["color"] = "grey"
                    if data["category_three"][0]["questions"][3]["double"] == True:
                        phase = "double"
                        data["category_three"][0]["questions"][3]["color"] = "red"
                    q = "3-4"
                elif cat_three_five.collidepoint(event.pos):
                    phase = "question"
                    data["category_three"][0]["questions"][4]["color"] = "grey"
                    if data["category_three"][0]["questions"][4]["double"] == True:
                        phase = "double"
                        data["category_three"][0]["questions"][4]["color"] = "red"
                    q = "3-5"
                elif cat_four_one.collidepoint(event.pos):
                    phase = "question"
                    data["category_four"][0]["questions"][0]["color"] = "grey"
                    if data["category_four"][0]["questions"][0]["double"] == True:
                        phase = "double"
                        data["category_four"][0]["questions"][0]["color"] = "red"
                    q = "4-1"
                elif cat_four_two.collidepoint(event.pos):
                    phase = "question"
                    data["category_four"][0]["questions"][1]["color"] = "grey"
                    if data["category_four"][0]["questions"][1]["double"] == True:
                        phase = "double"
                        data["category_four"][0]["questions"][1]["color"] = "red"
                    q = "4-2"
                elif cat_four_three.collidepoint(event.pos):
                    phase = "question"
                    data["category_four"][0]["questions"][2]["color"] = "grey"
                    if data["category_four"][0]["questions"][2]["double"] == True:
                        phase = "double"
                        data["category_four"][0]["questions"][2]["color"] = "red"
                    q = "4-3"
                elif cat_four_four.collidepoint(event.pos):
                    phase = "question"
                    data["category_four"][0]["questions"][3]["color"] = "grey"
                    if data["category_four"][0]["questions"][3]["double"] == True:
                        phase = "double"
                        data["category_four"][0]["questions"][3]["color"] = "red"
                    q = "4-4"
                elif cat_four_five.collidepoint(event.pos):
                    phase = "question"
                    data["category_four"][0]["questions"][4]["color"] = "grey"
                    if data["category_four"][0]["questions"][4]["double"] == True:
                        phase = "double"
                        data["category_four"][0]["questions"][4]["color"] = "red"
                    q = "4-5"
                elif cat_five_one.collidepoint(event.pos):
                    phase = "question"
                    data["category_five"][0]["questions"][0]["color"] = "grey"
                    if data["category_five"][0]["questions"][0]["double"] == True:
                        phase = "double"
                        data["category_five"][0]["questions"][0]["color"] = "red"
                    q = "5-1"
                elif cat_five_two.collidepoint(event.pos):
                    phase = "question"
                    data["category_five"][0]["questions"][1]["color"] = "grey"
                    if data["category_five"][0]["questions"][1]["double"] == True:
                        phase = "double"
                        data["category_five"][0]["questions"][1]["color"] = "red"
                    q = "5-2"
                elif cat_five_three.collidepoint(event.pos):
                    phase = "question"
                    data["category_five"][0]["questions"][2]["color"] = "grey"
                    if data["category_five"][0]["questions"][2]["double"] == True:
                        phase = "double"
                        data["category_five"][0]["questions"][2]["color"] = "red"
                    q = "5-3"
                elif cat_five_four.collidepoint(event.pos):
                    phase = "question"
                    data["category_five"][0]["questions"][3]["color"] = "grey"
                    if data["category_five"][0]["questions"][3]["double"] == True:
                        phase = "double"
                        data["category_five"][0]["questions"][3]["color"] = "red"
                    q = "5-4"
                elif cat_five_five.collidepoint(event.pos):
                    phase = "question"
                    data["category_five"][0]["questions"][4]["color"] = "grey"
                    if data["category_five"][0]["questions"][4]["double"] == True:
                        phase = "double"
                        data["category_five"][0]["questions"][4]["color"] = "red"
                    q = "5-5"
            elif phase == "board_two":
                if cat_six_one.collidepoint(event.pos):
                    phase = "question"
                    data["category_six"][0]["questions"][0]["color"] = "grey"
                    if data["category_six"][0]["questions"][0]["double"] == True:
                        phase = "double"
                        data["category_six"][0]["questions"][0]["color"] = "red"
                    q = "6-1"
                elif cat_six_two.collidepoint(event.pos):
                    phase = "question"
                    data["category_six"][0]["questions"][1]["color"] = "grey"
                    if data["category_six"][0]["questions"][1]["double"] == True:
                        phase = "double"
                        data["category_six"][0]["questions"][1]["color"] = "red"
                    q = "6-2"
                elif cat_six_three.collidepoint(event.pos):
                    phase = "question"
                    data["category_six"][0]["questions"][2]["color"] = "grey"
                    if data["category_six"][0]["questions"][2]["double"] == True:
                        phase = "double"
                        data["category_six"][0]["questions"][2]["color"] = "red"
                    q = "6-3"
                elif cat_six_four.collidepoint(event.pos):
                    phase = "question"
                    data["category_six"][0]["questions"][3]["color"] = "grey"
                    if data["category_six"][0]["questions"][3]["double"] == True:
                        phase = "double"
                        data["category_six"][0]["questions"][3]["color"] = "red"
                    q = "6-4"
                elif cat_six_five.collidepoint(event.pos):
                    phase = "question"
                    data["category_six"][0]["questions"][4]["color"] = "grey"
                    if data["category_six"][0]["questions"][4]["double"] == True:
                        phase = "double"
                        data["category_six"][0]["questions"][4]["color"] = "red"
                    q = "6-5"
                elif cat_seven_one.collidepoint(event.pos):
                    phase = "question"
                    data["category_seven"][0]["questions"][0]["color"] = "grey"
                    if data["category_seven"][0]["questions"][0]["double"] == True:
                        phase = "double"
                        data["category_seven"][0]["questions"][0]["color"] = "red"
                    q = "7-1"
                elif cat_seven_two.collidepoint(event.pos):
                    phase = "question"
                    data["category_seven"][0]["questions"][1]["color"] = "grey"
                    if data["category_seven"][0]["questions"][1]["double"] == True:
                        phase = "double"
                        data["category_seven"][0]["questions"][1]["color"] = "red"
                    q = "7-2"
                elif cat_seven_three.collidepoint(event.pos):
                    phase = "question"
                    data["category_seven"][0]["questions"][2]["color"] = "grey"
                    if data["category_seven"][0]["questions"][2]["double"] == True:
                        phase = "double"
                        data["category_seven"][0]["questions"][2]["color"] = "red"
                    q = "7-3"
                elif cat_seven_four.collidepoint(event.pos):
                    phase = "question"
                    data["category_seven"][0]["questions"][3]["color"] = "grey"
                    if data["category_seven"][0]["questions"][3]["double"] == True:
                        phase = "double"
                        data["category_seven"][0]["questions"][3]["color"] = "red"
                    q = "7-4"
                elif cat_seven_five.collidepoint(event.pos):
                    phase = "question"
                    data["category_seven"][0]["questions"][4]["color"] = "grey"
                    if data["category_seven"][0]["questions"][4]["double"] == True:
                        phase = "double"
                        data["category_seven"][0]["questions"][4]["color"] = "red"
                    q = "7-5"
                elif cat_eight_one.collidepoint(event.pos):
                    phase = "question"
                    data["category_eight"][0]["questions"][0]["color"] = "grey"
                    if data["category_eight"][0]["questions"][0]["double"] == True:
                        phase = "double"
                        data["category_eight"][0]["questions"][0]["color"] = "red"
                    q = "8-1"
                elif cat_eight_two.collidepoint(event.pos):
                    phase = "question"
                    data["category_eight"][0]["questions"][1]["color"] = "grey"
                    if data["category_eight"][0]["questions"][1]["double"] == True:
                        phase = "double"
                        data["category_eight"][0]["questions"][1]["color"] = "red"
                    q = "8-2"
                elif cat_eight_three.collidepoint(event.pos):
                    phase = "question"
                    data["category_eight"][0]["questions"][2]["color"] = "grey"
                    if data["category_eight"][0]["questions"][2]["double"] == True:
                        phase = "double"
                        data["category_eight"][0]["questions"][2]["color"] = "red"
                    q = "8-3"
                elif cat_eight_four.collidepoint(event.pos):
                    phase = "question"
                    data["category_eight"][0]["questions"][3]["color"] = "grey"
                    if data["category_eight"][0]["questions"][3]["double"] == True:
                        phase = "double"
                        data["category_eight"][0]["questions"][3]["color"] = "red"
                    q = "8-4"
                elif cat_eight_five.collidepoint(event.pos):
                    phase = "question"
                    data["category_eight"][0]["questions"][4]["color"] = "grey"
                    if data["category_eight"][0]["questions"][4]["double"] == True:
                        phase = "double"
                        data["category_eight"][0]["questions"][4]["color"] = "red"
                    q = "8-5"
                elif cat_nine_one.collidepoint(event.pos):
                    phase = "question"
                    data["category_nine"][0]["questions"][0]["color"] = "grey"
                    if data["category_nine"][0]["questions"][0]["double"] == True:
                        phase = "double"
                        data["category_nine"][0]["questions"][0]["color"] = "red"
                    q = "9-1"
                elif cat_nine_two.collidepoint(event.pos):
                    phase = "question"
                    data["category_nine"][0]["questions"][1]["color"] = "grey"
                    if data["category_nine"][0]["questions"][1]["double"] == True:
                        phase = "double"
                        data["category_nine"][0]["questions"][1]["color"] = "red"
                    q = "9-2"
                elif cat_nine_three.collidepoint(event.pos):
                    phase = "question"
                    data["category_nine"][0]["questions"][2]["color"] = "grey"
                    if data["category_nine"][0]["questions"][2]["double"] == True:
                        phase = "double"
                        data["category_nine"][0]["questions"][2]["color"] = "red"
                    q = "9-3"
                elif cat_nine_four.collidepoint(event.pos):
                    phase = "question"
                    data["category_nine"][0]["questions"][3]["color"] = "grey"
                    if data["category_nine"][0]["questions"][3]["double"] == True:
                        phase = "double"
                        data["category_nine"][0]["questions"][3]["color"] = "red"
                    q = "9-4"
                elif cat_nine_five.collidepoint(event.pos):
                    phase = "question"
                    data["category_nine"][0]["questions"][4]["color"] = "grey"
                    if data["category_nine"][0]["questions"][4]["double"] == True:
                        phase = "double"
                        data["category_nine"][0]["questions"][4]["color"] = "red"
                    q = "9-5"
                elif cat_ten_one.collidepoint(event.pos):
                    phase = "question"
                    data["category_ten"][0]["questions"][0]["color"] = "grey"
                    if data["category_ten"][0]["questions"][0]["double"] == True:
                        phase = "double"
                        data["category_ten"][0]["questions"][0]["color"] = "red"
                    q = "10-1"
                elif cat_ten_two.collidepoint(event.pos):
                    phase = "question"
                    data["category_ten"][0]["questions"][1]["color"] = "grey"
                    if data["category_ten"][0]["questions"][1]["double"] == True:
                        phase = "double"
                        data["category_ten"][0]["questions"][1]["color"] = "red"
                    q = "10-2"
                elif cat_ten_three.collidepoint(event.pos):
                    phase = "question"
                    data["category_ten"][0]["questions"][2]["color"] = "grey"
                    if data["category_ten"][0]["questions"][2]["double"] == True:
                        phase = "double"
                        data["category_ten"][0]["questions"][2]["color"] = "red"
                    q = "10-3"
                elif cat_ten_four.collidepoint(event.pos):
                    phase = "question"
                    data["category_ten"][0]["questions"][3]["color"] = "grey"
                    if data["category_ten"][0]["questions"][3]["double"] == True:
                        phase = "double"
                        data["category_ten"][0]["questions"][3]["color"] = "red"
                    q = "10-4"
                elif cat_ten_five.collidepoint(event.pos):
                    phase = "question"
                    data["category_ten"][0]["questions"][4]["color"] = "grey"
                    if data["category_ten"][0]["questions"][4]["double"] == True:
                        phase = "double"
                        data["category_ten"][0]["questions"][4]["color"] = "red"
                    q = "10-5"
                continue

    pygame.display.update()


pygame.quit()