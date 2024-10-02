import random
def roll_dice():
    dice_value = random.randint(1, 6)
    if dice_value in [5, 6]:
        print("Вы победили")
    elif dice_value in [3, 4]:
        return roll_dice()
    else:
        print("Вы проиграли")

    print("Значение на кубике: ", dice_value)

if __name__ == '__main__':
    roll_dice()