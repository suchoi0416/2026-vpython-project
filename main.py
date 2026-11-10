Web VPython 3.2

box(texture = "https://i.postimg.cc/htvNFVyX/ttttttt.png", size = vec(1, 1, 0.0001))
boxes = []
for i in range(3) : 
    for j in range(3) : 
        boxes.append(box(pos = vec((i-1)*0.3,(j-1)*0.3,0), size = vec(0.1,0.1,0.1)))

while True :
    rate(100)
    k = keysdown()
    if '1' in k :
        boxes[0].color = color.red
    if 'q' in k :
        boxes[0].color = color.blue
    if '4' in k :
        boxes[3].color = color.red
    if 'q' in k :
        boxes[0].color = color.blue
    if '7' in k :
        boxes[6].color = color.red
    if boxes[0].color == color.red and boxes[3].color == color.red and  boxes[6].color == color.red :
        print('red team win')











box(texture = "https://i.postimg.cc/vm93GQ03/ttt.png", size = vec(1,1,0.001))
while True :
    rate(100)
    k = keysdown()
    if '1' in k : 
       box(pos = vec(-0.27, 0.28, 0), size = vec(0.1, 0.1, 0.1), color = color.red)
    if '2' in k : 
       box(pos = vec(0, 0.28, 0), size = vec(0.1, 0.1, 0.1), color = color.red)
    if '3' in k : 
       box(pos = vec(0.27, 0.28, 0), size = vec(0.1, 0.1, 0.1), color = color.red)
    if '4' in k : 
       box(pos = vec(-0.27, 0, 0), size = vec(0.1, 0.1, 0.1), color = color.red)
    if '5' in k : 
       box(pos = vec(0, 0, 0), size = vec(0.1, 0.1, 0.1), color = color.red)
    if '6' in k : 
       box(pos = vec(0.27, 0, 0), size = vec(0.1, 0.1, 0.1), color = color.red)
    if '7' in k : 
       box(pos = vec(-0.27, -0.28, 0), size = vec(0.1, 0.1, 0.1), color = color.red)
    if '8' in k : 
       box(pos = vec(0, -0.28, 0), size = vec(0.1, 0.1, 0.1), color = color.red)
    if '9' in k : 
       box(pos = vec(0.27, -0.28, 0), size = vec(0.1, 0.1, 0.1), color = color.red)
  
  
    if 'q' in k : 
       box(pos = vec(-0.27, 0.28, 0), size = vec(0.1, 0.1, 0.1), color = color.blue)
    if 'w' in k : 
       box(pos = vec(0, 0.28, 0), size = vec(0.1, 0.1, 0.1), color = color.blue)
    if 'e' in k : 
       box(pos = vec(0.27, 0.28, 0), size = vec(0.1, 0.1, 0.1), color = color.blue)
    if 'r' in k : 
       box(pos = vec(-0.27, 0, 0), size = vec(0.1, 0.1, 0.1), color = color.blue)
    if 't' in k : 
       box(pos = vec(0, 0, 0), size = vec(0.1, 0.1, 0.1), color = color.blue)
    if 'y' in k : 
       box(pos = vec(0.27, 0, 0), size = vec(0.1, 0.1, 0.1), color = color.blue)
    if 'u' in k : 
       box(pos = vec(-0.27, -0.28, 0), size = vec(0.1, 0.1, 0.1), color = color.blue)
    if 'i' in k : 
       box(pos = vec(0, -0.28, 0), size = vec(0.1, 0.1, 0.1), color = color.blue)
    if 'o' in k : 
       box(pos = vec(0.27, -0.28, 0), size = vec(0.1, 0.1, 0.1), color = color.blue)
