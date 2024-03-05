import pygame
import player
import block
import bullet
import random

class Game():

    def __init__(self):
        self.name = "Block Shooter"
        self.win_size = [800, 600]
        
    def run(self, screen):
        #-- Set Values -- 
        run = True
        alive = True

        clock = pygame.time.Clock()

        all_sprite_list = pygame.sprite.Group()
        enemy_sprite_list = pygame.sprite.Group()
        bullet_list = pygame.sprite.Group()

        score = 0
        score_font = pygame.font.Font(None, 60)

        guy = player.Player([0,0,255], 400, 560, 20, 20)

        for i in range(50):
            bl = block.Block(random.randint(0,785), random.randint(-600, 0))
            enemy_sprite_list.add(bl)
            all_sprite_list.add(bl)


        all_sprite_list.add(guy)




        #-- Game Loop --

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    return -1
                #-- Check Key Commands --
                if event.type == pygame.KEYDOWN and alive:
                    if event.key == pygame.K_LEFT:
                        guy.change_x = -4
                    elif event.key == pygame.K_RIGHT:
                        guy.change_x = 4
                    elif event.key == pygame.K_SPACE:
                        bul = bullet.Bullet(guy.rect.x+7, guy.rect.y)
                        bullet_list.add(bul)
                        all_sprite_list.add(bul)

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        guy.change_x = 0
                    elif event.key == pygame.K_RIGHT:
                        guy.change_x = 0
                    elif event.key == pygame.K_m:
                        run = False
                        return 0
                    
            #-- Check if all enemies cleared --
            if not enemy_sprite_list:
                return True
            # -- Game Logic --
            screen.fill([255, 255, 255])
            if alive:
                all_sprite_list.update()
            
            #-- check if blocks have gone off screen --
            for b in enemy_sprite_list:
                if b.rect.y > 815:
                    b.rect.y = random.randint(-100, 0)
                    b.rect.x = random.randint(0, 785)

            #-- Collision Checks --
            player_hit_list = pygame.sprite.spritecollide(guy, enemy_sprite_list, False)
            for i in player_hit_list:
                alive = False
                print("DEAD")
                return 2


            
            block_hit_list = pygame.sprite.groupcollide(bullet_list, enemy_sprite_list, True, True)
            for b in block_hit_list:
                score += 1

            # -- Draw the Shit --
            
           
            screen.blit( score_font.render("Score: " + str(score), False, [123,0,123]), [610, 50])
            all_sprite_list.draw(screen)
                    
            #-- Invert What was Drawn --
            pygame.display.flip()

            #-- Set Frame Rate --
            clock.tick(60)