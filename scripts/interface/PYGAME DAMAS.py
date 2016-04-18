import pygame
class Track_py(object):
    def __init__(self, sreen_size = None, fullscreen = False):
        self.starta = pygame.init()
        if fullscreen:
            self.screen = pygame.display.set_mode(sreen_size,pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode(sreen_size)
        self.event()
        
    def event(self):
        self.done = False
        while not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        self.done = True
            
            self.screen.fill((255,0,0))
            self.track([ ['1','o','1','o','1','o','1','o'],
                         ['o','1','o','1','o','1','o','1'],
                         ['1','o','1','o','1','o','1','o'],
                         ['|','1','|','1','|','1','|','1'],
                         ['1','|','1','|','1','|','1','|'],
                         ['o','1','o','1','o','1','o','1'],
                         ['1','o','1','o','1','o','1','o'],
                         ['o','1','o','1','o','1','o','1'] ])
            
            self.pecas([ ['1','o','1','o','1','o','1','o'],
                         ['o','1','o','1','o','1','o','1'],
                         ['1','o','1','o','1','o','1','o'],
                         ['|','1','|','1','|','1','|','1'],
                         ['1','|','1','|','1','|','1','|'],
                         ['o','1','o','1','o','1','o','1'],
                         ['1','o','1','o','1','o','1','o'],
                         ['o','1','o','1','o','1','o','1'] ])
            pygame.display.flip()
            
    def track(self, lista = None):
        self.color = [(0,0,0),(255,255,255)]
        self.position_x = -65
        self.position_y = -65
        self.x = 0
        self.y = -1

        for elemento in lista[self.y]:
            self.y += 1
            self.position_y += 75
            self.position_x = -65
            for elemento in lista[self.y]:            
                if elemento == '1':
                    self.position_x += 75
                    pygame.draw.rect(self.screen, self.color[1], pygame.Rect(self.position_x, self.position_y,75,75))

                if elemento == 'o' or elemento == "|":
                    self.position_x += 75
                    pygame.draw.rect(self.screen, self.color[0], pygame.Rect(self.position_x, self.position_y,75,75))
                self.x = self.x + 1    
                print elemento

    def pecas(self, lista = None):
        passo = 150
        y = 48
        i = 0
        while i < len(lista[0]):
            x = 48 if i % 2 != 0 else 123
            j = 0
            while j < len(lista[i]):
                if lista[i][j] == 'o':
                    pygame.draw.circle(self.screen,(255,0,0),(x, y),35)
                    x += passo
                j += 1
            y += passo/2
            i += 1
                    
tela = Track_py((620,620))
