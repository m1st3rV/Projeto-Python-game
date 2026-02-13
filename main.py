import pygame

print(f'Setup Start')

pygame.init()
window = pygame.display.set_mode(size=(400, 300))
print(f'Setup End')

print('setup start')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #Close window
            print('setup end')
            quit() #Close program