import pygame
import math
from datetime import datetime

pygame.init()

screen = pygame.display.set_mode((700, 700))
startPoint = (350, 350)
lineLength = 300

while True:
    currentTime = datetime.now()
    h = currentTime.hour
    m = currentTime.minute
    s = currentTime.second
    ms = currentTime.microsecond / 1000
    
    screen.fill((0, 0, 0))

    # sæt minut/sekundmarkeringer
    angle = 0
    for i in range(60):
        endX = startPoint[0] + lineLength * math.cos(math.radians(angle))
        endY = startPoint[1] + lineLength * math.sin(math.radians(angle))
        endPoint = (endX, endY)
        pygame.draw.line(screen, (255, 255, 255), startPoint, endPoint, 3)
        angle += 6
    pygame.draw.circle(screen, (0, 0, 0), startPoint, 290)

    # sæt timemarkering
    angle = 0
    for i in range(12):
        endX = startPoint[0] + lineLength * math.cos(math.radians(angle))
        endY = startPoint[1] + lineLength * math.sin(math.radians(angle))
        endPoint = (endX, endY)
        pygame.draw.line(screen, (255, 255, 255), startPoint, endPoint, 5)
        angle += 30
    pygame.draw.circle(screen, (0, 0, 0) , startPoint, 270)

    # udregn timeviserens vinkel og tegn
    hourAngle = ((360 / 12) * (h % 12 + m / 60)) - 90       # h == currentTime.hour
    endOffset = [250 * math.cos(math.radians(hourAngle)), 250 * math.sin(math.radians(hourAngle))]
    endPosition = (startPoint[0] + endOffset[0], startPoint[1] + endOffset[1])
    pygame.draw.line(screen, (210, 40, 40), startPoint, endPosition, 10)

    # udregn minutviserens vinkel og tegn
    minuteAngle = ((360 / 60) * (m % 60 + s / 60)) - 90     # m == currentTime.minute, s == currentTime.second
    endOffset = [250 * math.cos(math.radians(minuteAngle)), 250 * math.sin(math.radians(minuteAngle))]
    endPosition = (startPoint[0] + endOffset[0], startPoint[1] + endOffset[1])
    pygame.draw.line(screen, (210, 40, 40), startPoint, endPosition, 4)

    # udregn sekundviserens vinkel og tegn
    secondAngle = ((360 / 60) * (s + ms / 1000)) - 90
    endOffset = [250 * math.cos(math.radians(secondAngle)), 250 * math.sin(math.radians(secondAngle))]
    endPosition = (startPoint[0] + endOffset[0], startPoint[1] + endOffset[1])
    pygame.draw.line(screen, (255, 255, 255), startPoint, endPosition, 2)

    # gem startpunkterne bag en cirkel
    pygame.draw.circle(screen, (210, 40, 40), startPoint, 10)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()