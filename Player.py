import pygame

class Player:
    def __init__(self, x, y, direction, color):
        self.x = x
        self.y = y
        self.direction = direction
        self.color = color
        self.trail = [(x, y)]

    def move(self):
        if self.direction == 'up':
            self.y -= 10
        elif self.direction == 'down':
            self.y += 10
        elif self.direction == 'left':
            self.x -= 10
        elif self.direction == 'right':
            self.x += 10
        self.trail.append((self.x, self.y))
        print(f"Moved player to ({self.x}, {self.y})")

    def draw(self, screen):
        for position in self.trail:
            pygame.draw.rect(screen, self.color, pygame.Rect(position[0], position[1], 10, 10))