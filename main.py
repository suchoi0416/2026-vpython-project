Web VPython 3.2
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
