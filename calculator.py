WIDTH = 550
HEIGHT = 500
answer = 0
num0 = Actor("num0", bottomleft=(10, 490))

num1 = Actor("num1", bottomleft=(10,400))
num2 = Actor("num2", bottomleft=(120,400))
num3 = Actor("num3", bottomleft=(230,400))

num4 = Actor("num4", bottomleft=(10,310))
num5 = Actor("num5", bottomleft=(120,310))
num6 = Actor("num6", bottomleft=(230,310))

num7 = Actor("num7", bottomleft=(10,230))
num8 = Actor("num8", bottomleft=(120,230))
num9 = Actor("num9", bottomleft=(230,230))

x_button = Actor("x_button", bottomleft=(340, 310))
equal_button = Actor("equal_button", bottomleft=(230, 490))
divide_button = Actor("division_symbol", bottomleft=(340, 230))
minus_button = Actor("minus_button", bottomleft=(340, 400))
add_button = Actor("add_button", bottomleft=(340, 490))
decimal_button = Actor("dot", bottomleft=(120, 490))
delete_button = Actor("bin", bottomleft=(450, 490))

list1 = []
list_function = []
list2 = []
list3 = []

def draw():
    screen.fill((255, 255, 255))
    num1.draw()
    num2.draw()
    num3.draw()
    num4.draw()
    num5.draw()
    num6.draw()
    num7.draw()
    num8.draw()
    num9.draw()
    num0.draw()
    x_button.draw()
    equal_button.draw()
    divide_button.draw()
    minus_button.draw()
    add_button.draw()
    decimal_button.draw()
    delete_button.draw()
    if answer != 0:
        screen.draw.text(str(answer), midright=(WIDTH-10, 100), color=(0, 0, 0), fontsize=40)
    screen.draw.text("".join(list1), midright=(WIDTH-10, 50), color=(0, 0, 0), fontsize=50)

def on_mouse_down(pos):
    x, y = pos
    global answer
    global new_list2
    global new_list3
    global list1
    global list2
    global list3
    global list_function
    answer = 0

    if x_button.left < x < x_button.right and x_button.top < y < x_button.bottom:
        if "x" not in list_function:
            list1.append(" x ")
            list_function.append("x")

    if divide_button.left < x < divide_button.right and divide_button.top < y < divide_button .bottom:
        if "/" not in list_function:
            list1.append(" / ")
            list_function.append("/")

    if minus_button.left < x < minus_button.right and minus_button.top < y < minus_button.bottom:
        if "-" not in list_function:
            list1.append(" - ")
            list_function.append("-")

    if add_button.left < x < add_button.right and add_button.top < y < add_button.bottom:
        if "+" not in list_function:
            list1.append(" + ")
            list_function.append("+")

    if equal_button.left < x < equal_button.right and equal_button.top < y < equal_button.bottom:
        new_list2 = "".join(list2)
        new_list3 = "".join(list3)
        print(new_list3)
        print(new_list2)
        if "x" in list_function:
            answer = eval((new_list2) + "*" + (new_list3))
        if "/" in list_function:
            answer = eval((new_list3) + "/" + (new_list2))
        if "-" in list_function:
            answer = eval((new_list3) + "-" + (new_list2))
        if "+" in list_function:
            answer = eval((new_list3) + "+" + (new_list2))
    if num1.left < x < num1.right and num1.top < y < num1.bottom:
        if " = " not in list1:
            list1.append("1")
        if "x" in list_function or "/" in list_function or "-" in list_function or "+" in list_function:
            list2.append("1")
        if "x" not in list_function and "/" not in list_function and "-" not in list_function and "+" not in list_function:
            list3.append("1")

    if num2.left < x < num2.right and num2.top < y < num2.bottom:
        if " = " not in list1:
            list1.append("2")
        if "x" in list_function or "/" in list_function or "-" in list_function or "+" in list_function:
            list2.append("2")
        if "x" not in list_function and "/" not in list_function and "-" not in list_function and "+" not in list_function:
            list3.append("2")

    if num3.left < x < num3.right and num3.top < y < num3.bottom:
        if " = " not in list1:
            list1.append("3")
        if "x" in list_function or "/" in list_function or "-" in list_function or "+" in list_function:
            list2.append("3")
        if "x" not in list_function and "/" not in list_function and "-" not in list_function and "+" not in list_function:
            list3.append("3")

    if num4.left < x < num4.right and num4.top < y < num4.bottom:
        if " = " not in list1:
            list1.append("4")
        if "x" in list_function or "/" in list_function or "-" in list_function or "+" in list_function:
            list2.append("4")
        if "x" not in list_function and "/" not in list_function and "-" not in list_function and "+" not in list_function:
            list3.append("4")

    if num5.left < x < num5.right and num5.top < y < num5.bottom:
        if " = " not in list1:
            list1.append("5")
        if "x" in list_function or "/" in list_function or "/" in list_function or "+" in list_function:
            list2.append("5")
        if "x" not in list_function and "/" not in list_function and "-" not in list_function and "+" not in list_function:
            list3.append("5")

    if num6.left < x < num6.right and num6.top < y < num6.bottom:
        if " = " not in list1:
            list1.append("6")
        if "x" in list_function or "/" in list_function or "-" in list_function or "+" in list_function:
            list2.append("6")
        if "x" not in list_function and "/" not in list_function and "-" not in list_function and "+" not in list_function:
            list3.append("6")

    if num7.left < x < num7.right and num7.top < y < num7.bottom:
        if " = " not in list1:
            list1.append("7")
        if "x" in list_function or "/" in list_function or "-" in list_function or "+" in list_function:
            list2.append("7")
        if "x" not in list_function and "/" not in list_function and "-" not in list_function and "+" not in list_function:
            list3.append("7")

    if num8.left < x < num8.right and num8.top < y < num8.bottom:
        if " = " not in list1:
            list1.append("8")
        if "x" in list_function or "/" in list_function or "-" in list_function or "+" in list_function:
            list2.append("8")
        if "x" not in list_function and "/" not in list_function and "-" not in list_function and "+" not in list_function:
            list3.append("8")

    if num9.left < x < num9.right and num9.top < y < num9.bottom:
        if " = " not in list1:
            list1.append("9")
        if "x" in list_function or "/" in list_function or "-" in list_function or "+" in list_function:
            list2.append("9")
        if "x" not in list_function and "/" not in list_function and "-" not in list_function and "+" not in list_function:
            list3.append("9")

    if num0.left < x < num0.right and num0.top < y < num0.bottom:
        if " = " not in list1:
            list1.append("0")
        if "x" in list_function or "/" in list_function or "-" in list_function or "+" in list_function:
            list2.append("0")
        if "x" not in list_function and "/" not in list_function and "-" not in list_function and "+" not in list_function:
            list3.append("0")

    if decimal_button.left < x < decimal_button.right and decimal_button.top < y < decimal_button.bottom:
        if " = " not in list1:
            list1.append(".")
        if "x" in list_function or "/" in list_function or "-" in list_function or "+" in list_function:
            list2.append(".")
        if "x" not in list_function and "/" not in list_function and "-" not in list_function and "+" not in list_function:
            list3.append(".")

    if delete_button.left < x < delete_button.right and delete_button.top < y < delete_button.bottom:
        if len(list1) > 0:
            list1.clear()
            list2.clear()
            list3.clear()
            list_function.clear()
    print("List1:",list1)
    print("List2:",list2)
    print("List3:",list3)
    screen.clear()