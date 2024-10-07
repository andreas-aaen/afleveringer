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
    ms = currentTime.microsecond / 1000     # konvertér microsekunder til millisekunder
    
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
    
    """

    h, m, s, ms == variabler defineret med datetime.now()
    (h % 12 + m / 60), (m + s / 60), osv. udglatter viserenes bevægelse
    % sikrer 'wrapping' af timeviseren fra kl. 13 til 24
    -90 sikrer at uret starter udregningerne fra kl. 12 og ikke kl. 3, da vinklerne starter fra 'øst'

    """

    # udregn timeviserens vinkel og tegn
    hourAngle = ((360 / 12) * (h % 12 + m / 60)) - 90
    endOffset = [250 * math.cos(math.radians(hourAngle)), 250 * math.sin(math.radians(hourAngle))]
    endPosition = (startPoint[0] + endOffset[0], startPoint[1] + endOffset[1])
    pygame.draw.line(screen, (210, 40, 40), startPoint, endPosition, 10)

    # udregn minutviserens vinkel og tegn
    minuteAngle = ((360 / 60) * (m + s / 60)) - 90
    endOffset = [250 * math.cos(math.radians(minuteAngle)), 250 * math.sin(math.radians(minuteAngle))]
    endPosition = (startPoint[0] + endOffset[0], startPoint[1] + endOffset[1])
    pygame.draw.line(screen, (210, 40, 40), startPoint, endPosition, 4)

    # udregn sekundviserens vinkel og tegn
    secondAngle = ((360 / 60) * (s + ms / 1000)) - 90
    endOffset = [250 * math.cos(math.radians(secondAngle)), 250 * math.sin(math.radians(secondAngle))]
    endPosition = (startPoint[0] + endOffset[0], startPoint[1] + endOffset[1])
    pygame.draw.line(screen, (255, 255, 255), startPoint, endPosition, 2)

    # gem visernes startpunkter bag en cirkel
    pygame.draw.circle(screen, (210, 40, 40), startPoint, 10)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()