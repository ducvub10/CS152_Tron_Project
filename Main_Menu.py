import pygame

class MainMenu:
    def __init__(self, gameObj):
        self.game = gameObj

        self.font = pygame.font.Font(None, 34)

        self.menuList = ['Two Player', 'Solo', 'Endless']
        self.menu_rects = []  # Rect objects for menu items
        self.activeItem = 0
        self.activeColour = (30, 140, 255)
        self.inactiveColour = (255, 255, 255)
        self.menu_height = len(self.menuList) * 50  # Height of menu items

        self.calculate_menu_positions()

    def calculate_menu_positions(self):
        menu_width, _ = self.font.size(max(self.menuList, key=len))  # Get the width of the longest menu item

        # Calculate positions of menu items
        for i, item in enumerate(self.menuList):
            left = (self.game.scr_x - menu_width) // 2
            top = (self.game.scr_y - self.menu_height) // 2 + i * 50
            width, height = self.font.size(item)
            self.menu_rects.append(pygame.Rect(left, top, width, height))

    def eventTick(self, event):
        if event.type == pygame.KEYUP:  # Change the active menu entry
            prevActive = self.activeItem

            if event.key == pygame.K_UP:
                self.activeItem = (self.activeItem - 1) % len(self.menuList)
            elif event.key == pygame.K_DOWN:
                self.activeItem = (self.activeItem + 1) % len(self.menuList)

            if prevActive != self.activeItem:
                self.draw_menu()

            if event.key == pygame.K_RETURN:
                self.game.startMatch(self.activeItem)

    def draw_menu(self):
        self.game.screen.fill((0, 0, 0))  # Clear the screen

        # Build and draw title text
        title_font = pygame.font.Font(None, 80)
        title = title_font.render("PyTron", True, (255, 255, 255))
        title_rect = title.get_rect(center=(self.game.scr_x // 2, 80))
        self.game.screen.blit(title, title_rect)

        # Draw selectable menu options
        for i, item in enumerate(self.menuList):
            color = self.activeColour if i == self.activeItem else self.inactiveColour
            text_surface = self.font.render(item, True, color)
            text_rect = text_surface.get_rect(center=self.menu_rects[i].center)
            self.game.screen.blit(text_surface, text_rect)

    def draw(self):
        self.draw_menu()
