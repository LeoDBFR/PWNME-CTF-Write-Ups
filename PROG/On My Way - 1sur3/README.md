# 1/3 - On My Way

Énoncé : "For this challenge, you'll have to find the exit point, from a start position, in a 3D map.

Map representation
Example for a map, with a size of n=2

Server will send you this:

0E
00
-
00
S0
-
Explanations:

layer z0    layer z1
^         ^
|  0E     | 00
|  00     | S0
y         y
 x---->    x---->
E => (E)ntrée

S => (S)ortie

coords(E) : x=1 y=1 z=0

coords(S) : x=0 y=0 z=1

The shortest path that solve this map is wrote like:

x-;y-;z+

x- => Go from x1 to x0

y- => Go from y1 to y0

z+ => Go from z0 to z1

For this challenge, you just have to send the number of minimal moves to go from the (E) to the (S)

In this example, answer will be 3"

Format du flag : "PWNME{[A-Za-z0-9_]}"

Auteur : "Eteck#3426"

Nombre final de points : 108

Serveur : nc prog.pwnme.fr 7000

Voir OnMyWay.py
