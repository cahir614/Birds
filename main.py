import sys
import pygame
from bird import Bird
from healthbar import Healthbar
from food import Food
from heart import Heart

pygame.init()
pygame.mixer.init()
bird_sound = pygame.mixer.Sound('sounds/birdsound.mp3')
daylight_sound = pygame.mixer.Sound('sounds/daylight.mp3')
bite_sound = pygame.mixer.Sound('sounds/bite.mp3')

screen = pygame.display.set_mode((1920, 1024))
pygame.display.set_caption("Birds")
all_sprites_list = pygame.sprite.Group()
birds = pygame.sprite.Group()
foods = pygame.sprite.Group()
player0 = Bird((255, 0, 0), 64, 64)
player0.rect.x = 1500
player0.rect.y = 700
player1 = Bird((0, 0, 255), 64, 64)
player1.rect.x = 500
player1.rect.y = 700

bar = Healthbar()
heart = Heart(0, 0)

clock = pygame.time.Clock()

pygame.mixer.Channel(0).play(bird_sound, loops=-1)
pygame.mixer.Channel(1).play(daylight_sound, loops=-1)
pygame.mixer.Channel(0).set_volume(0.9)
pygame.mixer.Channel(1).set_volume(0.9)
pygame.mixer.Channel(2).set_volume(0.7)


def control0(player, speed):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.moveLeft(speed)
    if keys[pygame.K_RIGHT]:
        player.moveRight(speed)
    if keys[pygame.K_UP]:
        player.moveUp(speed)
    if keys[pygame.K_DOWN]:
        player.moveDown(speed)


def control1(player, speed):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player.moveLeft(speed)
    if keys[pygame.K_d]:
        player.moveRight(speed)
    if keys[pygame.K_w]:
        player.moveUp(speed)
    if keys[pygame.K_s]:
        player.moveDown(speed)


birds.add(player0)
birds.add(player1)
all_sprites_list.add(player0)
all_sprites_list.add(player1)


for i in range(6):
    m = Food()
    foods.add(m)
    Food.add(m)
    all_sprites_list.add(m)


def newFood():
    m = Food()
    foods.add(m)
    Food.add(m)
    all_sprites_list.add(m)


fontL = pygame.font.Font("font/slkscre.ttf", 100)
fontM = pygame.font.Font("font/slkscre.ttf", 50)
fontS = pygame.font.Font("font/slkscre.ttf", 20)
start_time = pygame.time.get_ticks()


def spe(x):
    return (6-0.0077*x)


def main():
    gameOver = False
    carryOn = True
    image = pygame.image.load('images/bg.webp')

    health = 0
    count = 0

    while carryOn:
        count += 1/60
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carryOn = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    carryOn = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
                pygame.display.toggle_fullscreen()
        if not gameOver:
            control0(player0, spe(health))
            control1(player1, spe(health))
            all_sprites_list.update()
            screen.blit(image, (0, 0))
            for sprite in all_sprites_list:
                if isinstance(sprite, Food):
                    sprite.gravity()
                elif isinstance(sprite, Bird):
                    sprite.gravity()
                sprite.draw(screen)
            bar.draw(screen, health)
            collisions = pygame.sprite.groupcollide(birds, foods, False, False)
            for bird, foods_hit in collisions.items():
                for food in foods_hit:
                    if not hasattr(food, 'collided') or not food.collided:
                        pygame.mixer.Channel(2).play(bite_sound)
                        health -= 5
                        newFood()
                        all_sprites_list.remove(food)
                        food.collided = True
            bird_collisions = pygame.sprite.groupcollide(birds, birds, False, False)
            for bird1, birds_hit in bird_collisions.items():
                for bird2 in birds_hit:
                    if bird1 != bird2:
                        p0 = player0.rect.centerx
                        p1 = player1.rect.centerx
                        if p0 < p1:
                            xpos = p0+(p1-p0)/2
                        else:
                            xpos = p1+(p0-p1)/2
                        keys = pygame.key.get_pressed()
                        if keys[pygame.K_h] and keys[pygame.K_k]:
                            heart.draw(screen, xpos, player0.rect.centery-80)

            img0 = fontM.render('Health: '+str(round(780-health)), True, (0, 0, 0))
            img1 = fontM.render('Speed: '+str(round(spe(health)*10))+'km/h', True, (0, 0, 0))
            img2 = fontS.render(str(round(count))+' sec.', True, (0, 0, 0))
            screen.blit(img0, (20+896, 75))
            screen.blit(img1, (500+896, 75))
            screen.blit(img2, (900+896, 25))
            pygame.display.update()
            clock.tick(60)
            if health < 780:
                health += 0.2
            if health > 779:
                start_time = pygame.time.get_ticks()
                gameOver = True
                score = round(count)

        else:
            current_time = pygame.time.get_ticks()
            if current_time - start_time < 20000:
                screen.fill((0, 0, 0))
                img0 = fontL.render('Game Over', True, (255, 255, 255))
                img1 = fontL.render('Birds', True, (255, 255, 255))
                img2 = fontS.render('by Philipp Schrauth', True, (255, 255, 255))
                img3 = fontM.render('Highscore: '+str(score), True, (255, 255, 255))
                screen.blit(img0, ((screen.get_width() - img0.get_width()) // 2, 100))
                screen.blit(img3, ((screen.get_width() - img3.get_width()) // 2, 300))
                screen.blit(img1, ((screen.get_width() - img1.get_width()) // 2, 500))
                screen.blit(img2, ((screen.get_width() - img2.get_width()) // 2, 600))
                pygame.display.update()
            else:
                carryOn = False


if __name__ == '__main__':
    main()
    pygame.quit()
    sys.exit()
