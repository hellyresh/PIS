# Нарисовать рамочку шириной w символов и высотой h символов.
def paint(w, h):
    print(w * "*")
    for i in range(2, h):
        print("*" + (w - 2) * " " + "*")
    print(w * "*")


paint(5, 3)


# Пускай символ, которым рисуется рамочка – тоже входной параметр.
def paint1(w, h, s):
    print(w * s)
    for i in range(2, h):
        print(s + (w - 2) * " " + s)
    print(w * s)


print()
paint1(10, 4, "o")


# Нарисовать рамочку шириной w символов и высотой h символов, и толщиной f символов. (оформить в виде функции)
def paint2(w, h, f, s):
    for i in range(f):
        print(w * s)
    for i in range(0, h - f * 2):
        print(f * s + (w - 2 * f) * " " + f * s)
    for i in range(0, f):
        print(w * s)


print()
paint2(15, 6, 2, "x")
