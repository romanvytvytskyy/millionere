import pygame
import qestion_list as ql

bg = pygame.transform.scale(pygame.image.load("bg1.jpg"), (1200, 600))
back = ((0, 0, 0))
pygame.init()
mw = pygame.display.set_mode((1200, 600))
pygame.display.set_caption("Millionere")
icon = pygame.image.load("logo.png")
pygame.display.set_icon(icon)


pygame.mixer.init()
intro = pygame.mixer.Sound("music/main_theme.ogg")


class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = back
        if color:
            self.fill_color = color

    def color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

    def colliderect(self, rect):
        return self.rect.colliderect(rect)


class Picture(Area):
    def __init__(self, filename, x=0, y=0, width=10, height=10):
        Area.__init__(self, x=x, y=y, width=width, height=height, color=None)
        self.image = pygame.image.load(filename)

    def draw(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))


q = ql.Show_Quesion(ql.lewel_1, ql.lewel_2, ql.lewel_3)
print(q.set_question())
print(q.setcash())

game = True
finish = False

pygame.mixer.Sound.play(intro)
mw.fill((back))
mw.blit(icon, (325, 75))
pygame.display.update()
pygame.time.delay(17000)
pygame.mixer.music.load("music/theme.ogg")
pygame.mixer.music.play()

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        mw.blit(bg, (0, 0))
    pygame.display.update()
    pygame.time.delay(50)
