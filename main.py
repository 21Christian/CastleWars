from sys import exit
from Swordsman1 import *
from Swordsman2 import *
from Worker1 import *
from Worker2 import *
from Archer1 import *
from Archer2 import *
from ArcherArrow1 import *
from ArcherArrow2 import *
from TowerArrow1 import *
from TowerArrow2 import *
from Mine import *
from Barrack import *
from Wall import *
from Tower import *


def menu_display():
    game_title_surf = title_font.render('CastleWars', False, 'Black')
    game_title_rect = game_title_surf.get_rect(center=(500, 50))
    screen.blit(game_title_surf, game_title_rect)

    start_surf = screen_font.render('To start the game press "enter" ...', False, 'Black')
    start_rect = start_surf.get_rect(center=(500, 200))
    screen.blit(start_surf, start_rect)


def workers_collision(workers1_army, workers2_army, mines1_building, mines2_building, walls1_building, walls2_building):
    for worker in workers1_army:
        if pygame.sprite.spritecollideany(worker, mines1_building): worker.dig = True
        if pygame.sprite.spritecollideany(worker, walls1_building): worker.repair = True

    for worker in workers2_army:
        if pygame.sprite.spritecollideany(worker, mines2_building): worker.dig = True
        if pygame.sprite.spritecollideany(worker, walls2_building): worker.repair = True


def archer_to_soldier(archers1_army, archers2_army, swordsmen1_army, swordsmen2_army, archer_arrows1, archer_arrows2):
    # Archer1 attacking enemy armies
    for archer1 in archers1_army:
        if archer1.rect.x >= WALL_POS:

            if len(swordsmen2_army) == 0 and len(archers2_army) == 0:
                archer1.shoot = False
                archer1.unleash = True
            else:
                # Archer1 attacking Swordmen2 army
                for soldier in swordsmen2_army:
                    archer1_range = abs(soldier.rect.x - archer1.rect.x)
                    if archer1_range <= ARCHER_RANGE:
                        archer1.shoot = True
                        archer1.unleash = False
                        if archer1.index == 1 and archer1.shootFlag == False:
                            archer1.shootFlag = True
                            archer_arrows1.add(ArcherArrow1(a_arrow1, archer1.rect.x))
                        break
                    else:
                        archer1.shoot = False
                        archer1.unleash = True
    for arrow in archer_arrows1:
        enemy_swordman_collision = pygame.sprite.spritecollideany(arrow, swordsmen2_army)
        if enemy_swordman_collision:
            enemy_swordman_collision.health -= ARCHER_HIT
            arrow.kill()

    # Archer2 colliding with the enemy armies
    for archer2 in archers2_army:
        if archer2.rect.x <= 1000 - WALL_POS:
            if len(swordsmen1_army) == 0 and len(archers1_army) == 0:
                archer2.shoot = False
                archer2.unleash = True
            else:
                # Archer2 attacking Soldier1
                for soldier in swordsmen1_army:
                    archer2_range = abs(archer2.rect.x - soldier.rect.x)
                    if archer2_range <= ARCHER_RANGE:
                        archer2.shoot = True
                        archer2.unleash = False
                        if archer2.index == 1 and archer2.shootFlag == False:
                            archer2.shootFlag = True
                            archer_arrows2.add(ArcherArrow2(a_arrow2, archer2.rect.x))
                        break
                    else:
                        archer2.shoot = False
                        archer2.unleash = True

    for arrow in archer_arrows2:
        enemy_swordman_collision = pygame.sprite.spritecollideany(arrow, swordsmen1_army)
        if enemy_swordman_collision:
            enemy_swordman_collision.health -= ARCHER_HIT
            arrow.kill()


def archer_to_archer(archers1_army, archers2_army, archer_arrows1, archer_arrows2):
    # Archer1 to Archer2
    for archer1 in archers1_army:
        if archer1.rect.x >= WALL_POS:
            if len(archers2_army) == 0 and len(swordsmen2_army) == 0:
                archer1.shoot = False
                archer1.unleash = True
            else:
                # Archer1 attacking Archer2
                for archer2 in archers2_army:
                    archer1_range = abs(archer2.rect.x - archer1.rect.x)
                    if archer1_range <= ARCHER_RANGE and archer1.rect.x <= archer2.rect.x:
                        archer1.shoot = True
                        archer1.unleash = False
                        if archer1.index == 1 and archer1.shootFlag == False:
                            archer1.shootFlag = True
                            archer_arrows1.add(ArcherArrow1(a_arrow1, archer1.rect.x))
                        break
                    else:
                        archer1.shoot = False
                        archer1.unleash = True

    for arrow in archer_arrows1:
        enemy_archer_collision = pygame.sprite.spritecollideany(arrow, archers2_army)
        if enemy_archer_collision:
            enemy_archer_collision.health -= ARCHER_HIT
            arrow.kill()

    for archer2 in archers2_army:
        if archer2.rect.x <= 1000 - WALL_POS:
            if len(archers1_army) == 0 and len(swordsmen1_army) == 0:
                archer2.shoot = False
                archer2.unleash = True
            else:
                for archer1 in archers1_army:
                    archer2_range = abs(archer2.rect.x - archer1.rect.x)
                    if archer2_range <= ARCHER_RANGE and archer2.rect.x >= archer1.rect.x:
                        archer2.shoot = True
                        archer2.unleash = False
                        if archer2.index == 1 and archer2.shootFlag == False:
                            archer2.shootFlag = True
                            archer_arrows2.add(ArcherArrow2(a_arrow2, archer2.rect.x))
                        break
                    else:
                        archer2.shoot = False
                        archer2.unleash = True

    for arrow in archer_arrows2:
        enemy_archer_collision = pygame.sprite.spritecollideany(arrow, archers1_army)
        if enemy_archer_collision:
            enemy_archer_collision.health -= ARCHER_HIT
            arrow.kill()


def archer_to_wall(archers1_army, archers2_army, walls1_building, walls2_building):
    for archer1 in archers1_army:
        for wall2 in walls2_building:
            if archer1.rect.x >= 1000 - WALL_POS - ARCHER_RANGE:
                archer1.unleash = False
                archer1.shoot = True
                if archer1.index == 1 and archer1.shootFlag == False:
                    archer1.shootFlag = True
                    archer_arrows1.add(ArcherArrow1(a_arrow1, archer1.rect.x))
                break

    for arrow in archer_arrows1:
        enemy_archer_collision = pygame.sprite.spritecollideany(arrow, walls2_building)
        if enemy_archer_collision:
            data['p2_wallhealth'] -= ARCHER_HIT
            arrow.kill()

    for archer2 in archers2_army:
        for wall1 in walls1_building:
            if archer2.rect.x <= WALL_POS + ARCHER_RANGE:
                archer2.unleash = False
                archer2.shoot = True
                if archer2.index == 1 and archer2.shootFlag == False:
                    archer2.shootFlag = True
                    archer_arrows2.add(ArcherArrow2(a_arrow2, archer2.rect.x))
                break

    for arrow in archer_arrows2:
        enemy_archer_collision = pygame.sprite.spritecollideany(arrow, walls1_building)
        if enemy_archer_collision:
            data['p1_wallhealth'] -= ARCHER_HIT
            arrow.kill()


def swordsmen_collision(swordsmen1_army, swordsmen2_army, walls1_building, walls2_building, archers1_army,
                        archers2_army):
    # Player 1
    for swordman in swordsmen1_army:
        # Swordsman1 attackin Swordsman2
        colliding_sword2 = pygame.sprite.spritecollideany(swordman, swordsmen2_army)
        if colliding_sword2:
            swordman.attacking = True
            swordman.unleash = False
            if swordman.index == 3:
                colliding_sword2.health -= SWORD_HIT
        # Swordsman1 attacking Archer2
        colliding_arch2 = pygame.sprite.spritecollideany(swordman, archers2_army)
        if colliding_arch2:
            swordman.attacking = True
            swordman.unleash = False
            if swordman.index == 3:
                colliding_arch2.health -= SWORD_HIT
        # Swordsman1 attackin Wall2
        colliding_wall2 = pygame.sprite.spritecollideany(swordman, walls2_building)
        if colliding_wall2:
            swordman.attacking = True
            swordman.unleash = False
            if swordman.index == 3:
                data['p2_wallhealth'] -= SWORD_HIT
        # Restriction for running
        if not colliding_sword2 and not colliding_arch2 and not colliding_wall2 and swordman.rect.x >= WALL_POS:
            swordman.attack = False
            swordman.unleash = True
    # Player2
    for swordman in swordsmen2_army:
        # Swordsman2 attackin Swordsman1
        colliding_sword1 = pygame.sprite.spritecollideany(swordman, swordsmen1_army)
        if colliding_sword1:
            swordman.attacking = True
            swordman.unleash = False
            if swordman.index == 3:
                colliding_sword1.health -= SWORD_HIT
        # Swordsman2 attacking Archer1
        colliding_arch1 = pygame.sprite.spritecollideany(swordman, archers1_army)
        if colliding_arch1:
            swordman.attacking = True
            swordman.unleash = False
            if swordman.index == 3:
                colliding_arch1.health -= SWORD_HIT
        # Swordsman2 attackin Wall1
        colliding_wall1 = pygame.sprite.spritecollideany(swordman, walls1_building)
        if colliding_wall1:
            swordman.attacking = True
            swordman.unleash = False
            if swordman.index == 3:
                data['p1_wallhealth'] -= SWORD_HIT
        # Restriction for running
        if not colliding_sword1 and not colliding_arch1 and not colliding_wall1 and swordman.rect.x <= 1000 - WALL_POS:
            swordman.attack = False
            swordman.unleash = True


def tower_shooting(towers1_building, towers2_building, tower_arrows1, tower_arrows2, swordsmen1_army, sowrdsmen2_army,
                   archers1_army, archers2_army):
    # Tower1 Archer2
    for tower in towers1_building:
        for archer in archers2_army:
            if archer.rect.x in range(370, 385):
                if tower.Spara == False:
                    tower.Spara = True
                    tower_arrows1.add(TowerArrow1(t_arrow1))
                break
    for arrow in tower_arrows1:
        tower1_arrow_collision = pygame.sprite.spritecollideany(arrow, archers2_army)
        if tower1_arrow_collision:
            tower1_arrow_collision.health -= TOWER_HIT
            arrow.kill()

    # Tower1 Swordman2
    for tower in towers1_building:
        for swordsman in swordsmen2_army:
            if swordsman.rect.x in range(430, 450):
                if tower.Spara == False:
                    tower.Spara = True
                    tower_arrows1.add(TowerArrow1(t_arrow1))
                break
    for arrow in tower_arrows1:
        tower1_arrow_collision = pygame.sprite.spritecollideany(arrow, swordsmen2_army)
        if tower1_arrow_collision:
            tower1_arrow_collision.health -= TOWER_HIT
            arrow.kill()

    # Tower2 Archer1
    for tower2 in towers2_building:
        for archer in archers1_army:
            if archer.rect.x in range(615, 625):
                if tower2.Spara == False:
                    tower2.Spara = True
                    tower_arrows2.add(TowerArrow2(t_arrow2))
                break

    for arrow in tower_arrows2:
        tower2_arrow_collision = pygame.sprite.spritecollideany(arrow, archers1_army)
        if tower2_arrow_collision:
            tower2_arrow_collision.health -= TOWER_HIT
            arrow.kill()

    # Tower2 Swordman1
    for tower in towers2_building:
        for swordsman in swordsmen1_army:
            if swordsman.rect.x in range(540, 550):
                if tower.Spara == False:
                    tower.Spara = True
                    tower_arrows2.add(TowerArrow2(t_arrow2))
                break

    for arrow in tower_arrows2:
        tower2_arrow_collision = pygame.sprite.spritecollideany(arrow, swordsmen1_army)
        if tower2_arrow_collision:
            tower2_arrow_collision.health -= TOWER_HIT
            arrow.kill()


def group_display_update():
    towers1_building.update()
    towers1_building.draw(screen)
    walls1_building.update()
    walls1_building.draw(screen)
    barracks1_building.update()
    barracks1_building.draw(screen)
    mines1_building.update()
    mines1_building.draw(screen)
    archer_arrows1.update()
    archer_arrows1.draw(screen)
    tower_arrows1.update()
    tower_arrows1.draw(screen)
    # Display P1 Army
    swordsmen1_army.update()
    swordsmen1_army.draw(screen)
    archers1_army.update()
    archers1_army.draw(screen)
    workers1_army.update()
    workers1_army.draw(screen)
    # Display P2 Buildings
    towers2_building.update()
    towers2_building.draw(screen)
    walls2_building.update()
    walls2_building.draw(screen)
    barracks2_building.update()
    barracks2_building.draw(screen)
    mines2_building.update()
    mines2_building.draw(screen)
    # Display P2 Army
    swordsmen2_army.update()
    swordsmen2_army.draw(screen)
    archers2_army.update()
    archers2_army.draw(screen)
    workers2_army.update()
    workers2_army.draw(screen)
    archer_arrows2.update()
    archer_arrows2.draw(screen)
    tower_arrows2.update()
    tower_arrows2.draw(screen)


def text(data, swordsmen1_army, swordsman2_text, worker1_army, worker2_army, archer1_army, archer2_army):
    swordsman1_text = small_test_font.render('Swordsmen: ' + str(len(swordsmen1_army)), False, 'WHITE')
    swordsman1_rect = swordsman1_text.get_rect(topleft=(10, 10))

    swordsman2_text = small_test_font.render('Swordsmen: ' + str(len(swordsmen2_army)), False, 'WHITE')
    swordsman2_rect = swordsman1_text.get_rect(topright=(960, 10))

    archer1_text = small_test_font.render('Archers: ' + str(len(archer1_army)), False, 'WHITE')
    archer1_rect = archer1_text.get_rect(topleft=(10, 25))

    archer2_text = small_test_font.render('Archers: ' + str(len(archer2_army)), False, 'WHITE')
    archer2_rect = archer2_text.get_rect(topright=(960, 25))

    worker1_text = small_test_font.render('Workers: ' + str(len(worker1_army)), False, 'WHITE')
    worker1_rect = worker1_text.get_rect(topleft=(10, 40))

    worker2_text = small_test_font.render('Workers: ' + str(len(worker2_army)), False, 'WHITE')
    worker2_rect = worker2_text.get_rect(topright=(960, 40))

    wall1_text = small_test_font.render(f'WALL HEALTH: {data["p1_wallhealth"]}', False, 'WHITE')
    wall1_rect = wall1_text.get_rect(topleft=(10, 55))

    wall2_text = small_test_font.render(f'WALL HEALTH: {data["p2_wallhealth"]}', False, 'WHITE')
    wall2_rect = wall2_text.get_rect(topright=(960, 55))

    p1_rescource_text = small_test_font.render(f'RESOURCES: {data["p1_resources"]}', False, 'Pink')
    p1_rescource_rect = p1_rescource_text.get_rect(topleft=(10, 70))

    p2_rescource_text = small_test_font.render(f'RESOURCES: {data["p2_resources"]}', False, 'Pink')
    p2_rescource_rect = p2_rescource_text.get_rect(topright=(960, 70))

    screen.blit(swordsman1_text, swordsman1_rect)
    screen.blit(swordsman2_text, swordsman2_rect)

    screen.blit(archer1_text, archer1_rect)
    screen.blit(archer2_text, archer2_rect)

    screen.blit(worker1_text, worker1_rect)
    screen.blit(worker2_text, worker2_rect)

    screen.blit(wall1_text, wall1_rect)
    screen.blit(wall2_text, wall2_rect)

    screen.blit(p1_rescource_text, p1_rescource_rect)
    screen.blit(p2_rescource_text, p2_rescource_rect)


def resume():
    playagain_surf = screen_font.render('To resume the game press "space" ...', False, 'Black')
    playagain_rect = playagain_surf.get_rect(center=(500, 125))
    screen.blit(playagain_surf, playagain_rect)
    pygame.display.update()
    resume = True
    while resume:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    resume = False
                    pygame.mixer.music.play(-1)
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
menu_screen = pygame.transform.scale(pygame.image.load('background/cool.png'), (1000, 250))
pygame.display.set_caption('CastleWars')

title_font = pygame.font.Font('font/Pixeltype.ttf', 75)
screen_font = pygame.font.Font('font/Pixeltype.ttf', 40)
small_test_font = pygame.font.Font('font/Pixeltype.ttf', 25)

clock = pygame.time.Clock()

background = pygame.transform.scale(pygame.image.load('background/cool.png'), (1000, 250))
ground = pygame.transform.scale(pygame.image.load('background/supermario.jpeg'), (1000, 250))
ground = pygame.image.load('background/good_ground.png')

# Groups
swordsmen1_army = pygame.sprite.Group()
swordsmen2_army = pygame.sprite.Group()
archers1_army = pygame.sprite.Group()
archers2_army = pygame.sprite.Group()
workers1_army = pygame.sprite.Group()
workers2_army = pygame.sprite.Group()

archer_arrows1 = pygame.sprite.Group()
archer_arrows2 = pygame.sprite.Group()
tower_arrows1 = pygame.sprite.Group()
tower_arrows2 = pygame.sprite.Group()

# Adding buildings
mine1 = Mine(1)
mine2 = Mine(2)
barr1 = Barrack(1)
barr2 = Barrack(2)
wall1 = Wall(1)
wall2 = Wall(2)
tower1 = Tower(1)
tower2 = Tower(2)

mines1_building = pygame.sprite.Group(mine1)
mines2_building = pygame.sprite.Group(mine2)
barracks1_building = pygame.sprite.Group(barr1)
barracks2_building = pygame.sprite.Group(barr2)
walls1_building = pygame.sprite.Group(wall1)
walls2_building = pygame.sprite.Group(wall2)
towers1_building = pygame.sprite.Group(tower1)
towers2_building = pygame.sprite.Group(tower2)

# data
data = {'p1_resources': INIT_RESOURCES, 'p2_resources': INIT_RESOURCES, 'p1_wallhealth': WALL_HEALTH,
        'p2_wallhealth': WALL_HEALTH}
p1_resource_counter = 0
p2_resource_counter = 0
p1_wallhealth_counter = 0
p2_wallhealth_counter = 0
pygame.mixer.music.load(__file__[:-len('main.py')] + 'background.ogg')
pygame.mixer.music.play(-1)
# Main loop
game_active = False
while True:

    if game_active == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                # Stop and resume
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.stop()
                    resume()
                # Spawning P1 Units
                if event.key == pygame.K_w and data['p1_resources'] >= SWORD_COST and len(swordsmen1_army) < 30:
                    swordsman1 = Swordsman1(swordsman1_ready, swordsman1_run, swordsman1_attack, swordsmasn1_dead)
                    swordsmen1_army.add(swordsman1)
                    data['p1_resources'] -= SWORD_COST

                if event.key == pygame.K_q and data['p1_resources'] >= WORKER_COST:
                    worker1 = Worker1(worker1_ready, worker1_run_left, worker1_run_right, worker1_dig, worker1_repair)
                    workers1_army.add(worker1)
                    data['p1_resources'] -= WORKER_COST

                if event.key == pygame.K_e and data['p1_resources'] >= ARCHER_COST and len(archers1_army) < 30:
                    archer1 = Archer1(archer1_ready, archer1_run, archer1_shoot, archer1_dead)
                    archers1_army.add(archer1)
                    data['p1_resources'] -= ARCHER_COST

                # Unleash P1 Units separately
                if event.key == pygame.K_d:
                    for swordsman in swordsmen1_army: swordsman.unleash = True

                if event.key == pygame.K_f:
                    for archer in archers1_army: archer.unleash = True

                # Unleash P1 Units together
                if event.key == pygame.K_z:
                    for swordsman in swordsmen1_army: swordsman.unleash = True
                    for archer in archers1_army: archer.unleash = True

                # Worker movement
                if event.key == pygame.K_a:
                    for worker1 in workers1_army:
                        if worker1.run_right == False: worker1.run_left = True

                if event.key == pygame.K_s:
                    for worker1 in workers1_army:
                        if worker1.run_left == False: worker1.run_right = True

                # Spawning P2 Units
                if event.key == pygame.K_o and data['p2_resources'] >= SWORD_COST and len(swordsmen2_army) < 30:
                    swordsman2 = Swordsman2(swordsman2_ready, swordsman2_run, swordsman2_attack, swordsmasn2_dead)
                    swordsmen2_army.add(swordsman2)
                    data['p2_resources'] -= SWORD_COST

                if event.key == pygame.K_p and data['p2_resources'] >= WORKER_COST:
                    worker2 = Worker2(worker2_ready, worker2_run_left, worker2_run_right, worker2_dig, worker2_repair)
                    workers2_army.add(worker2)
                    data['p2_resources'] -= WORKER_COST

                if event.key == pygame.K_i and data['p2_resources'] >= ARCHER_COST and len(archers2_army) < 30:
                    archer2 = Archer2(archer2_ready, archer2_run, archer2_shoot, archer2_dead)
                    archers2_army.add(archer2)
                    data['p2_resources'] -= ARCHER_COST

                # Unleash P1 Units separately
                if event.key == pygame.K_j:
                    for swordsman in swordsmen2_army: swordsman.unleash = True

                if event.key == pygame.K_h:
                    for archer in archers2_army: archer.unleash = True

                # Unleash P1 Units togheter
                if event.key == pygame.K_m:
                    for swordsman in swordsmen2_army: swordsman.unleash = True
                    for archer in archers2_army: archer.unleash = True

                # Worker movement
                if event.key == pygame.K_k:
                    for worker2 in workers2_army:
                        if worker2.run_right == False: worker2.run_left = True

                if event.key == pygame.K_l:
                    for worker2 in workers2_army:
                        if worker2.run_left == False: worker2.run_right = True

        if data['p1_wallhealth'] <= 0 or data['p2_wallhealth'] <= 0:
            pygame.mixer.music.stop()
            game_active = False

        # Worker1 production and repairing of the wall
        for worker1 in workers1_army:
            # Mining
            if worker1.dig == True:
                p1_resource_counter += 1
                if p1_resource_counter == 100:
                    p1_resource_counter = 0
                    data['p1_resources'] += WORKER_PROD
            # Repairing
            if worker1.repair == True:
                p1_wallhealth_counter += 1
                if p1_wallhealth_counter == 100:
                    p1_wallhealth_counter = 0
                    data['p1_wallhealth'] += WORKER_REPAIR
                    if data['p1_wallhealth'] >= WALL_HEALTH:
                        data['p1_wallhealth'] = WALL_HEALTH

        # Worker2 production and repairing of the wall
        for worker2 in workers2_army:
            # Mining
            if worker2.dig == True:
                p2_resource_counter += 1
                if p2_resource_counter == 100:
                    p2_resource_counter = 0
                    data['p2_resources'] += WORKER_PROD
            # Repairing
            if worker2.repair == True:
                p2_wallhealth_counter += 1
                if p2_wallhealth_counter == 100:
                    p2_wallhealth_counter = 0
                    data['p2_wallhealth'] += WORKER_REPAIR
                    if data['p2_wallhealth'] >= WALL_HEALTH:
                        data['p2_wallhealth'] = WALL_HEALTH

        swordsmen_collision(swordsmen1_army, swordsmen2_army, walls1_building, walls2_building, archers1_army,
                            archers2_army)
        archer_to_soldier(archers1_army, archers2_army, swordsmen1_army, swordsmen2_army, archer_arrows1,
                          archer_arrows2)
        archer_to_archer(archers1_army, archers2_army, archer_arrows1, archer_arrows2)
        archer_to_wall(archers1_army, archers2_army, walls1_building, walls2_building)
        tower_shooting(towers1_building, towers2_building, tower_arrows1, tower_arrows2, swordsmen1_army,
                       swordsmen2_army, archers1_army, archers2_army)
        workers_collision(workers1_army, workers2_army, mines1_building, mines2_building, walls1_building,
                          walls2_building)
        # Background
        screen.blit(background, (0, 0))
        screen.blit(ground, (0, 250 - GROUND_HEIGHT))
        text(data, swordsmen1_army, swordsmen2_army, workers1_army, workers2_army, archers1_army, archers2_army)
        # Groups draw and update
        group_display_update()


    elif game_active == False:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_active = True
                    pygame.mixer.music.play(-1)
                    data = {'p1_resources': INIT_RESOURCES, 'p2_resources': INIT_RESOURCES,
                            'p1_wallhealth': WALL_HEALTH, 'p2_wallhealth': WALL_HEALTH}
                    workers1_army.empty()
                    workers2_army.empty()
                    archers1_army.empty()
                    archers2_army.empty()
                    swordsmen1_army.empty()
                    swordsmen2_army.empty()
                    archer_arrows1.empty()
                    archer_arrows2.empty()
                    tower_arrows1.empty()
                    tower_arrows2.empty()
        screen.blit(menu_screen, (0, 0))
        menu_display()
        if data["p1_wallhealth"] <= 0:
            blue_surf = screen_font.render("BLUE WINS!!!", False, "Blue")
            blue_rect = blue_surf.get_rect(center=(500, 125))
            screen.blit(blue_surf, blue_rect)
        if data["p2_wallhealth"] <= 0:
            red_surf = screen_font.render("RED WINS!!!", False, "Red")
            red_rect = red_surf.get_rect(center=(500, 125))
            screen.blit(red_surf, red_rect)
    pygame.display.update()
    clock.tick(60)
