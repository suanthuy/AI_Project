import pygame
from random import randint
import math
from sklearn.cluster import KMeans

def distance(p1,p2):
    return math.sqrt((p1[0] - p2[0]) * (p1[0] - p2[0]) +(p1[1] - p2[1]) * (p1[1] - p2[1]) )

pygame.init()

screen = pygame.display.set_mode((1000,500))

pygame.display.set_caption("kmeans visualization")

running = True

clock = pygame.time.Clock()

BACKGROUND = (214,214,214)
BLACK = (0,0,0)
BACKGROUND_PANEL = (249,255,230)    # yellow
WHITE = (255,255,255)

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (147,153,35)
PURPLE = (255,0,255)
SKY = (0,255,255)
ORANGE = (255,125,25)
GRAPE = (100,25,125)
GRASS = (55,155,65)

COLORS = [RED, GREEN, BLUE, YELLOW, PURPLE, SKY, ORANGE, GRAPE, GRASS]

font = pygame.font.SysFont('sans',40)
font_small = pygame.font.SysFont("sans",20)
text_plus = font.render('+',True,WHITE)
text_minus = font.render('-',True,WHITE)
text_run = font.render('Run',True,WHITE)
text_random = font.render('Random',True,WHITE)
text_algorithm = font.render('Algorithm',True,WHITE)
text_reset = font.render('Reset',True,WHITE)

K = 0
error = 0
points = []
clusters = []        #cac cum, center point
labels = []


while running:
    clock.tick(60)
    screen.fill(BACKGROUND)

    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Draw interface
    # Draw panel
    pygame.draw.rect(screen,BLACK,(50,50,550,400))
    pygame.draw.rect(screen,BACKGROUND_PANEL,(55,55,540,390))
    # K button +
    pygame.draw.rect(screen,BLACK,(650,50,50,50))
    screen.blit(text_plus,(665,50))
    # K button -
    pygame.draw.rect(screen,BLACK,(750,50,50,50))
    screen.blit(text_minus,(770,50))
    # K value
    text_K = font.render("K = " + str(K),True, BLACK)
    screen.blit(text_K,(850,50))
    # Run button
    pygame.draw.rect(screen,BLACK,(650,120,150,50))
    screen.blit(text_run,(697,122))
    # Random button
    pygame.draw.rect(screen,BLACK,(650,200,150,50))
    screen.blit(text_random,(655,200))
    # Error value
    # if labels == [] and clusters == []:
    #     text_error = font.render("Error = " + str(error),True,BLACK)
    #     screen.blit(text_error,(650,250))
    # Algorithm button
    pygame.draw.rect(screen,BLACK,(650,300,150,50))
    screen.blit(text_algorithm,(655,300))
    # Reset button
    pygame.draw.rect(screen,BLACK,(650,370,150,50))
    screen.blit(text_reset,(655,370))
    # draw mouse position when mouse is in panel
    if 55 < mouse_x < 595 and 55 < mouse_y < 445:
        text_mouse = font_small.render("(" + str(mouse_x - 55) + "," + str(mouse_y - 55) + ")",True, BLACK)
        screen.blit(text_mouse,(mouse_x + 10,mouse_y))
    # End draw interface

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # create point in panel 
            if 55 < mouse_x < 595 and 55 < mouse_y < 445:
                labels = []
                point = [mouse_x - 55, mouse_y - 55]
                points.append(point)
                print("in panel")
            # K button
            if 650 < mouse_x < 700 and 50 < mouse_y < 100 and K < 9:
                K += 1
            if 750 < mouse_x < 800 and 50 < mouse_y < 100 and K > 0:
                K -= 1
            # Run button
            if 650 < mouse_x < 800 and 120 < mouse_y < 170:
                labels = []
                if clusters == []:
                    continue
                # Assign points to closet cluster
                for p in points:
                    distances_to_cluster = []
                    for c in clusters:
                        dis = distance(p,c)
                        distances_to_cluster.append(dis)
                    min_distance = min(distances_to_cluster)
                    label = distances_to_cluster.index(min_distance)
                    labels.append(label)

                # Update cluster
                for i in range(K):
                    sum_x = 0
                    sum_y = 0
                    count = 0
                    for j in range(len(points)):
                        if labels[j] == i:
                            sum_x += points[j][0]
                            sum_y += points[j][1]
                            count += 1
                    if count != 0:
                        new_cluster_x = sum_x/count
                        new_cluster_y = sum_y/count
                        clusters[i] = [new_cluster_x, new_cluster_y]
                print("Run")
            # Random button
            if 650 < mouse_x < 800 and 200 < mouse_y < 250:
                clusters = []
                labels = []
                for i in range(K):
                    random_point = [randint(0,540),randint(0,390)]
                    clusters.append(random_point)
                print("Random")
            # Algorithm button
            if 650 < mouse_x < 800 and 300 < mouse_y < 350:
                if K != 0:
                    kmeans = KMeans(n_clusters = K).fit(points)
                    print(kmeans.cluster_centers_)
                    labels = kmeans.predict(points)
                    clusters = kmeans.cluster_centers_
                print("Algorithm")
            # Reset button
            if 650 < mouse_x < 800 and 370 < mouse_y < 420:
                K = 0
                error = 0
                points = []
                clusters = []
                labels = []
                print("Reset")
    # draw clusters
    for i in range(len(clusters)):
        pygame.draw.circle(screen, COLORS[i], (int(clusters[i][0]) + 50, int(clusters[i][1]) + 50),10)
    # draw points 
    for i in range(len(points)):
        pygame.draw.circle(screen, BLACK, (points[i][0] + 50, points[i][1] + 50), 5)
        if labels == []:
            pygame.draw.circle(screen, WHITE, (points[i][0] + 50, points[i][1] + 50), 3)
        else:
            pygame.draw.circle(screen, COLORS[labels[i]], (points[i][0] + 50, points[i][1] + 50), 3)
    # Calculate and draw error
    error = 0
    for i in range(len(points)):
        if labels != [] and clusters != []:
            error += distance(points[i], clusters[labels[i]])

    text_error = font.render("Error = " + str(int(error)),True,BLACK)
    screen.blit(text_error,(650,250))

    pygame.display.flip()

pygame.quit()