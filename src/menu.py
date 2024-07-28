import pygame, sys

pygame.init()

clock = pygame.time.Clock()

def main_menu(menu_title: str):
    screen_width = 800
    screen_height = 800
    screen = pygame.display.set_mode((screen_width, screen_height))

    # Load your image here
    image_name = "images/rec.png"  # Insert your image name here
    image = pygame.image.load(image_name)
    run =  True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    run = False
                    return True

                if event.key == pygame.K_m:
                    run = False
                    return False

        # Fill the screen with purple
        screen.fill((183,41,219))
        grass_color = (187,57,219)

        for row in range(20):
            if row % 2 == 0:
                for column in range(20):
                    if column %2 == 0:
                        grass_rect = pygame.Rect(column * 40, row*40,40,40)
                        pygame.draw.rect(screen, grass_color, grass_rect)
            else:
                for col in range(20):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col * 40, row*40,40,40)
                        pygame.draw.rect(screen, grass_color, grass_rect)

        # Draw a header at the top of the screen
        font_header = pygame.font.Font(None, 100)
        text_surface_header = font_header.render(menu_title, True, (255,255,255))
        text_rect_header = text_surface_header.get_rect(center=(screen_width // 2, 50))
        screen.blit(text_surface_header, text_rect_header)

        # Draw image instead of rectangles
        image_rect = image.get_rect(center=(screen_width // 2, screen_height // 4))
        screen.blit(image, image_rect)

        # Render text "1v1" on top of the image
        font = pygame.font.Font(None, 36)
        text_surface = font.render("Press space for 1v1", True, (0, 0, 255))
        text_rect = text_surface.get_rect(center=image_rect.center)
        screen.blit(text_surface, text_rect)

        image_rect1 = image.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(image, image_rect1)

        # Render text "Dragon classic" on top of the image
        font1 = pygame.font.Font(None, 36)
        text_surface1 = font1.render("Press m for classic", True, (0, 0, 255))
        text_rect1 = text_surface1.get_rect(center=image_rect1.center)
        screen.blit(text_surface1, text_rect1)

        # Update the display
        pygame.display.update()
        clock.tick(60)


