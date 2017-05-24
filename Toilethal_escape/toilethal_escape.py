#Gra polegająca na ucieczce przed zabójczym papierem toaletowym

from livewires import games, color
import random

games.init(screen_width = 900, screen_height = 600, fps = 50)

class Koles(games.Sprite):
         #unikajacy zderzen sprzatacz
         image = games.load_image("Pics/koles.jpg")
         score = games.Text(value = 0, size = 75, color = color.pink,
                                          top = 5, right = games.screen.width - 20)
         def __init__(self):
                  super(Koles, self).__init__(image = Koles.image,
                                              x = games.mouse.x,
                                              bottom = games.screen.height)
                  games.screen.add(self.score)
         def update(self):
                  #zmien pozycje na wyznaczona przez wspolrzedna x myszy.
                  self.x = games.mouse.x
                  if self.left < 0:
                           self.left = 0
                  if self.right > games.screen.width:
                           self.right = games.screen.width
                  self.check_crash()

         def check_crash(self):
                  #sprawdz, czy nie doszlo do kolizjii z papierem toaletowym
                  for paper in self.overlapping_sprites:
                           Papier.handle_crash(Papier)

class Papier(games.Sprite):
         #papier, ktory spada na ziemie
         image = games.load_image("Pics/papier.jpg")
         speed = 1

         def __init__(self, x, y = 50):
                  super(Papier, self).__init__(image = Papier.image,
                                               x = x, y = y,
                                               dy = Papier.speed)

         def update(self):
                  #sprawdz, czy dolny brzeg papieru dotknal dolu ekranu
                  if self.bottom > games.screen.height:
                           Koles.score.value += 10
                           self.destroy()

         def handle_crash(self):
                  #co sie stanie kiedy papier zetknie sie z kolesiem
                  self.end_game(Koles)
                  games.screen.quit()

         def end_game(self):
                  #zakoncz gre
                  end_msg = games.Message(value = "Przegrana!",
                                          size = 120,
                                          color = color.black,
                                          x = games.screen.width/2,
                                          y = games.screen.height/2,
                                          lifetime = 5 * games.screen.fps,
                                          after_death = games.screen.quit)
                  games.screen.add(end_msg)

class Przeciwnik(games.Sprite):
         #przeciwnik, rzucajacy papierem na oslep!
         image = games. load_image("Pics/zly_czlowiek.png")
         def __init__(self, y = 65, speed = 2, odds_change = 150):
                  super(Przeciwnik, self).__init__(image = Przeciwnik.image,
                                                   x = games.screen.width/2,
                                                   y = y,
                                                   dx = speed)
                  self.odds_change = odds_change
                  self.time_till_drop = 0

         def update(self):
                  if self.left < 0 or self.right > games.screen.width:
                           self.dx = -self.dx
                  elif random.randrange(self.odds_change) == 0:
                           self.dx = -self.dx

                  self.check_drop()

         def check_drop(self):
                  #zmniejsz licznik odliczajacy czas lub rzuc papierem i zresetuj odliczanie
                  if self.time_till_drop > 0:
                           self.time_till_drop -= 1
                  else:
                           new_paper = Papier(x = self.x) #spadnie na wysokosci przeciwnika
                           games.screen.add(new_paper)
                           self.time_till_drop = int(new_paper.height * 1.5 / Papier.speed) + 1
                           


def main():
         tlo = games.load_image("Pics/lazienka.jpg", transparent = False)
         games.screen.background = tlo
         koles = Koles()
         games.screen.add(koles)
         przeciwnik = Przeciwnik()
         games.screen.add(przeciwnik)
         games.mouse.is_visible = False
         games.screen.event_grab = True
         games.screen.mainloop()

main()
