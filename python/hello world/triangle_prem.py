import re
Vertex_A = input("point A;(answer format:x y):")
Vertex_B = input("point B;(answer format:x y):")
Vertex_C = input("point C (answer format:x y):")

decoder = r'\d\d*\d*'

def input_reader(vertex,vertex2):
    [x,y] = re.findall(decoder,vertex)
    [x2,y2] = re.findall(decoder,vertex2)
    return dist(x,y,x2,y2)

def dist(x,y,x2,y2):
    x = int(x)
    y =int(y)
    x2 = int(x2)
    y2 = int(y2)
    dist = ((x-x2)**2 + (y-y2)**2)**.5
    return dist

def perimeter():
    dist_AB = input_reader(Vertex_A,Vertex_B)
    dist_BC = input_reader(Vertex_B,Vertex_C)
    dist_AC = input_reader(Vertex_A,Vertex_C)
    triperimeter = dist_AB+dist_AC+dist_BC
    print("\nside AB:" + str(dist_AB) + "\nside AC:" + str(dist_AC) + "\nside BC:" + str(dist_BC) + "\ntriangle perimeter:" + str(triperimeter))

perimeter()