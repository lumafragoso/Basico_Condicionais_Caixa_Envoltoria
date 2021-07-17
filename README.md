# Basico_Condicionais_Caixa_Envoltoria
Assessment activity of the 1º period of IT Bachelor on Basic and Conditionals in Python / Atividade avaliativa do 1º periodo do Bacharelado em TI sobre Básico e Condicionais em Python

## Condicionais Caixa Envoltória

### Goal / Objetivo
Many digital games perform collision tests between game elements, such as characters, bullets, walls, targets, among others. To simplify the calculations in crash tests, many games consider the existence of a box that surrounds the character (hence the name "wrapping box", from English bounding box). If there is an intersection between the boxes of two game elements, it means that one collided with the other. The figure below illustrates the case of two characters, with their respective envelope boxes, and the collision area in orange. Even if their images don't overlap, the boxes do and, therefore, the game considers it as a collision.
Develop a simple crash test, involving just one envelope box and one dot. Write a program that initially reads four values ​​from the user. The first two are the coordinates of the upper left corner of the wrapping box (XLeft,Ytop) and the next two are the width and height of the box, respectively. Then read from the user two more values ​​corresponding to the coordinates of the point (x,y) you want to test.
If the point (x,y) is inside the box, inform that the point collides with the box, otherwise it does not collide. To visually verify that your test is correct, draw a user-supplied box and dot as shown in the figure below. 

Muitos jogos digitais realizam testes de colisão entre elementos do jogos, tais como personagens, balas, muros, alvos, entre outros. Para simplicar os cálculos nos testes de colisão, vários jogos consideram a existência de uma caixa que envolve o personagem (daí o nome "caixa envoltória", do inglês bounding box). Se houver interseção entre as caixas de dois elementos do jogo, significa que um colidiu com o outro. A figura abaixo ilustra o caso de dois personagens, com suas respectivas caixas envoltórias, e a área de colisão em laranja. Mesmo que as imagens deles não se sobreponham, as caixas sim e, por isso, o jogo considera como uma colisão.
Desenvolva um teste de colisão simples, envolvendo apenas uma caixa envoltória e um ponto. Escreva um programa que lê inicialmente do usuário quatro valores. Os dois primeiros são as coordenadas do canto superior esquerdo da caixa envoltória (Xesquerda,Ytopo) e os dois seguintes são a largura e altura da caixa, respectivamente. Em seguida, leia do usuário mais dois valores correspondentes às coordenadas do ponto (x,y) que você quer testar.
Se o ponto (x,y) estiver dentro da caixa, informe que o ponto colide com a caixa, caso contrário que não colide. Para verificar visualmente se seu teste está correto, desenhe uma caixa e o ponto fornecidos pelo usuário, como exemplificado na figura abaixo.
1. Example / Exemplo
```py

esquerda: 0
topo: 50
largura: 150
altura: 50
x: 100
y: 40
=> Colide!

esquerda: 40
topo: 40
largura: 50
altura: 50
x: 10
y: 10
=> Não colide!

esquerda: -20
topo: 10
largura: 80
altura: 20
x: 0
y: 0
=> Colide!

esquerda: -50
topo: -30
largura: 10
altura: 10
x: -10
y: 20
=> Não colide!
```
