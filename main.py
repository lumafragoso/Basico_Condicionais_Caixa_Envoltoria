import turtle
esquerda = int(input('Esquerda:'))
topo = int(input('Topo:'))
largura = int(input('Largura:'))
altura = int(input('Altura:'))
x = int(input('X:'))
y = int(input('Y:'))
if (x > esquerda) or x < esquerda and x < esquerda - largura:
    print('Não colide')
elif x >= esquerda - largura and x <= esquerda:
    print('Colide')
#retângulo
t = turtle.Turtle()
t.penup()
t.goto(esquerda,topo)
t.right(90)
t.pendown()
t.forward(altura)
t.right(90)
t.forward(largura)
t.right(90)
t.forward(altura)
t.right(90)
t.forward(largura)
#ponto
t.penup()
t.goto(x, y)
t.color('blue')
t.dot(size=5)
