if(i<center[0]):
    posX = int(offsetX / scaleFactor) + center[0]
    posY = int(offsetY / scaleFactor) + center[1]
    if posX < 0 :
        posX = 0
    if posX > src.shape[1]:
        posX = src.shape[1]-1
    if posY < 0 :
        posY = 0
    if posY > src.shape[0]:
        posY = src.shape[0]-1
    #dst[j][i] = src[posY][posX]
    #dst[j][i] = src[posY][posX]
else:
    posX = int(offsetX * scaleFactor) + center[0]
    posY = int(offsetY * scaleFactor) + center[1]
    if posX < 0 :
        posX = 0
    if posX > src.shape[1]:
        posX = src.shape[1]-1
    if posY < 0 :
        posY = 0
    if posY > src.shape[0]:
        posY = src.shape[0]-1
    #dst[posY][posX] = src[j][i]
    dst[j][i] = src[posY][posX]                 
    #dst[posY][posX] = (255,255,255)