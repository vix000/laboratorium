#Event Horizon
#Gra na projekt z informatyki
#Demonstruje uzycie pakietów livewires i pygame
#Obrazki, animacje - wlasne
#Muzyka - VHS Dreams = Vice Point
#Bartłomiej Pysiak
import math, random
from livewires import games, color
games.init(screen_width = 960, screen_height = 640, fps = 50)


class Zawiniecie(games.Sprite):
    """ Przenies Sprite'a na druga strone ekranu """
    def update(self):   
        if self.top > games.screen.height:
            self.bottom = 0

        if self.bottom < 0:
            self.top = games.screen.height

        if self.left > games.screen.width:
            self.right = 0
            
        if self.right < 0:
            self.left = games.screen.width

    def die(self):
        """ Zniszcz się. """
        self.destroy()


class Zderzenie(Zawiniecie):
    """ Obiekt klasy Zawiniecie, który może zderzyć się z innym obiektem. """
    def update(self):
        """ Sprawdz czy zachodzi zderzenie """
        super(Zderzenie, self).update()
        
        if self.overlapping_sprites:
            for sprite in self.overlapping_sprites:
                sprite.die()
            self.die()               

    def die(self):
        """ Zniszcz się i pozostaw po sobie eksplozję. """
        new_explosion = Explosion(x = self.x, y = self.y)
        games.screen.add(new_explosion)
        self.destroy()


class Invader(Zawiniecie):
    """ Invadera przelatująca przez ekran. """
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    images = {SMALL  : games.load_image("Pixels/Invader_S.png"),
              MEDIUM : games.load_image("Pixels/Invader_M.png"),
              LARGE  : games.load_image("Pixels/Invader_L.png") }

    SPEED = 2
    SPAWN = 2
    POINTS = 300
    
    total =  0
      
    def __init__(self, game, x, y, size):
        """ Inicjalizuj duszka Invadery. """
        Invader.total += 1
        
        super(Invader, self).__init__(
            image = Invader.images[size],
            x = x, y = y,
            dx = random.choice([1, -1]) * Invader.SPEED * random.random()/size, 
            dy = random.choice([1, -1]) * Invader.SPEED * random.random()/size)

        self.game = game
        self.size = size

    def die(self):
        """ Zniszcz najezdzce. """
        Invader.total -= 1

        self.game.score.value += int(Invader.POINTS / self.size)
        self.game.score.right = games.screen.width - 10   
        
        # jeśli nie jest to mała Invadera, zastąp ją dwoma mniejszymi
        if self.size != Invader.SMALL:
            for i in range(Invader.SPAWN):
                new_Invader = Invader(game = self.game,
                                        x = self.x,
                                        y = self.y,
                                        size = self.size - 1)
                games.screen.add(new_Invader)

        # jeśli wszystkie Invadery zostały zniszczone, przejdź do następnego poziomu    
        if Invader.total == 0:
            self.game.advance()

        super(Invader, self).die()


class Spaceship(Zderzenie):
    """ Statek kosmiczny gracza. """
    image = games.load_image("Pixels/ship.png")
    ROTACJA = 3
    V_STEP = .03
    V_MAX = 3
    OPOZNIENIE = 10

    def __init__(self, game, x, y):
        """ Inicjalizuj Sprite'a statku. """
        super(Spaceship, self).__init__(image = Spaceship.image, x = x, y = y)
        self.game = game
        self.missile_wait = 0

    def update(self):
        """ Obracaj statek, przyśpieszaj i wystrzeliwuj pociski, zależnie od naciśniętych klawiszy. """
        super(Spaceship, self).update()
        
        # obróć statek zależnie od naciśniętych klawiszy strzałek (w prawo lub w lewo)
        if games.keyboard.is_pressed(games.K_LEFT):
            self.angle -= Spaceship.ROTACJA
        if games.keyboard.is_pressed(games.K_RIGHT):
            self.angle += Spaceship.ROTACJA

        # zastosuj siłę ciągu przy naciśniętym klawiszu strzałki w górę        
        if games.keyboard.is_pressed(games.K_UP):
            
            # zmień składowe prędkości w zależności od kąta położenia statku
            angle = self.angle * math.pi / 180  # zamień na radiany
            self.dx += Spaceship.V_STEP * math.sin(angle)
            self.dy += Spaceship.V_STEP * -math.cos(angle)

            # ograniczenie predkosci
            self.dx = min(max(self.dx, -Spaceship.V_MAX), Spaceship.V_MAX)
            self.dy = min(max(self.dy, -Spaceship.V_MAX), Spaceship.V_MAX)

        if games.keyboard.is_pressed(games.K_DOWN):
            angle = self.angle * math.pi / 180
            self.dx -= Spaceship.V_STEP * math.sin(angle)
            self.dy -= Spaceship.V_STEP * -math.cos(angle)
            self.dx = min(max(self.dx, -Spaceship.V_MAX), Spaceship.V_MAX)
            self.dy = min(max(self.dy, -Spaceship.V_MAX), Spaceship.V_MAX)

            
        # jeśli czekasz, aż statek będzie mógł wystrzelić następny pocisk,
        # zmniejsz czas oczekiwania
        if self.missile_wait > 0:
            self.missile_wait -= 1
            
        if games.keyboard.is_pressed(games.K_SPACE) and self.missile_wait == 0:
            new_missile = Missile(self.x, self.y, self.angle)
            games.screen.add(new_missile)        
            self.missile_wait = Spaceship.OPOZNIENIE

    def die(self):
        """ Zniszcz statek i zakończ grę. """
        self.game.end()
        super(Spaceship, self).die()


class Missile(Zderzenie):
    """ Pocisk wystrzelony przez statek gracza. """
    image = games.load_image("Pixels/missile.png")
    gun_sound = games.load_sound("Audio/gun.mp3")
    BUFFER = 80
    VELOCITY_FACTOR = 6
    LIFETIME = 50

    def __init__(self, Spaceship_x, Spaceship_y, Spaceship_angle):
        """ Inicjalizuj duszka pocisku. """
        Missile.gun_sound.play(1)
        
        # zamień na radiany
        angle = Spaceship_angle * math.pi / 180  

        # pozycja poczatkowa
        buffer_x = Missile.BUFFER * math.sin(angle)
        buffer_y = Missile.BUFFER * -math.cos(angle)
        x = Spaceship_x + buffer_x
        y = Spaceship_y + buffer_y

        # oblicz składowe prędkości pocisku
        dx = Missile.VELOCITY_FACTOR * math.sin(angle)
        dy = Missile.VELOCITY_FACTOR * -math.cos(angle)

        # utwórz pocisk
        super(Missile, self).__init__(image = Missile.image,
                                      x = x, y = y,
                                      dx = dx, dy = dy)
        self.lifetime = Missile.LIFETIME

    def update(self):
        """ Obsługuj ruch pocisku. """
        super(Missile, self).update()
        
        # zniszcz pocisk jak za dlugo leci 
        self.lifetime -= 1
        if self.lifetime == 0:
            self.destroy()


class Explosion(games.Animation):
    """ Animacja eksplozji. """
    images = ["Pixels/explo.png",
              "Pixels/explo1.png",
              "Pixels/explo2.png",
              "Pixels/explo3.png",
              "Pixels/explo4.png",
              "Pixels/explo5.png",
              "Pixels/explo6.png",
              "Pixels/explo7.png"]

    def __init__(self, x, y):
        super(Explosion, self).__init__(images = Explosion.images,
                                        x = x, y = y,
                                        repeat_interval = 4, n_repeats = 1,
                                        is_collideable = False)


class Game(object):
    """ Gra """
    def __init__(self):
        """ Inicjalizacja gry """
        # ustaw poziom
        self.level = 0


        # punkty
        self.score = games.Text(value = 0,
                                size = 30,
                                color = color.white,
                                top = 5,
                                right = games.screen.width - 10,
                                is_collideable = False)
        games.screen.add(self.score)

        # gracz
        self.Spaceship = Spaceship(game = self, 
                         x = games.screen.width/2,
                         y = games.screen.height/2)
        games.screen.add(self.Spaceship)

    def play(self):
        """ Przeprowadź grę. """
        # muzyka w tle
        games.music.load("Audio/VHS_Dreams-Vice_Point.mp3")
        games.music.play(-1)

        # tło
        background_theme = games.load_image("Pixels/moon.jpg")
        games.screen.background = background_theme

        # rozpocznij poziom 1
        self.advance()

        # rozpocznij grę
        games.screen.mainloop()

    def advance(self):
        """ Przejdź do następnego poziomu gry. """
        self.level += 1
        
        # obszar ochronny
        BUFFER = 150
     
        # utwórz nowe Invadery 
        for i in range(self.level):
            # oblicz współrzędne x i y zapewniające minimum odległości od statku
            # określ minimalną odległość wzdłuż osi x oraz wzdłuż osi y
            x_min = random.randrange(BUFFER)
            y_min = BUFFER - x_min

            # wyznacz odległość wzdłuż osi x oraz wzdłuż osi y
            # z zachowaniem odległości minimalnej
            x_distance = random.randrange(x_min, games.screen.width - x_min)
            y_distance = random.randrange(y_min, games.screen.height - y_min)

            # oblicz położenie na podstawie odległości
            x = self.Spaceship.x + x_distance
            y = self.Spaceship.y + y_distance

            # przeskocz miedzy krawedziami ekranu dzieki operatorowi modulo
            x %= games.screen.width
            y %= games.screen.height
       
            # stwórz najezdzce
            new_Invader = Invader(game = self,
                                    x = x, y = y,
                                    size = Invader.LARGE)
            games.screen.add(new_Invader)

        # poziom
        level_message = games.Message(value = "LEVEL " + str(self.level),
                                      size = 40,
                                      color = color.pink,
                                      x = games.screen.width/2,
                                      y = games.screen.width/10,
                                      lifetime = 3 * games.screen.fps,
                                      is_collideable = False)
        games.screen.add(level_message)

    def end(self):
        """ Zakończ grę. """
        # Komunikat
        end_message = games.Message(value = "GAME OVER",
                                    size = 90,
                                    color = color.blue,
                                    x = games.screen.width/2,
                                    y = games.screen.height/2,
                                    lifetime = 5 * games.screen.fps,
                                    after_death = games.screen.quit,
                                    is_collideable = False)
        games.screen.add(end_message)


def main():
    astrocrash = Game()
    astrocrash.play()

main()
