inventory = []

def game_start():
  print("...Вы просыпаетесь в грязной, едва освященной комнате. Событие предыдущего дня для вас тайна."
        "\nПозади вас окно, а по бокам, друг напротив друга, 2 двери, одна значительно меньше другой. Что вы будете делать?")
  print("   1. подойти к окну")
  print("   2. подойти к большой двери")
  print("   3. подойти к маленькой двери")
  print("   4. обыскать комнату")

  choice = input("   Введите номер вашего выбора: ")

  if choice == "1":
    window()
  elif choice == "2":
    big_door()
  elif choice == "3":
    small_door()
  elif choice == "4":
    search_room()
  else:
    print("Неверный выбор. Попробуйте снова.")
    game_start()

def game_start_2():
  print("Вы возвращаетесь в центр комнаты.")
  print("   1. подойти к окну")
  print("   2. подойти к большой двери")
  print("   3. подойти к маленькой двери")
  print("   4. обыскать комнату")

  choice = input("   Введите номер вашего выбора: ")

  if choice == "1":
    window()
  elif choice == "2":
    big_door()
  elif choice == "3":
    small_door()
  elif choice == "4":
    search_room()
  else:
    print("Неверный выбор. Попробуйте снова.")
    game_start_2()

def window():
  print("Вы подходите к окну - единственному источнику света в этой комнате, но при этом за ним… ничего нет?"
        "\nБеспросветная тьма. Это очень странно…")
  print("   1. присмотреться лучше")
  print("   2. отойти от окна")

  choice = input("   Введите номер вашего выбора: ")

  if choice == "1":
    print("Черный туман окутал этот мир и раглядеть в нем что-то просто невозможно.")
    game_start_2()
  elif choice == "2":
    game_start_2()
  else:
    print("Неверный выбор. Попробуйте снова.")
    window()

def big_door():
  print("Вы подходите к большой дверь и понимаете что она закрыта. Вам нужен ключ.")
  print("   1. попробовать открыть дверь")

  choice = input("   Введите номер вашего выбора: ")

  if choice == "1":
    if "Ключ2" in inventory:
      print("Вы открываете дверь. Вас можно поздравить - вы покинули место своего заточение и теперь вы свободны. "
            "\nОднако, стоит вам выйти за порог и вы чувствуете поток нахлынувших воспоминаний. Их так много, что ваша голова начинает раскалываться. "
            "\nВ определенный момент до вас доходит откровение: вы теряете сознание. В следующее мгновение вы летите на пол, а потом...")
      inventory.remove("Ключ2")
      game_start()
    else:
      print("У вас нет ключа.")
      game_start_2()
  else:
    print("Неверный выбор. Попробуйте снова.")
    big_door()
def small_door():
  print("Вы подходите к маленькой двери. Она оказывается открытой и вы можете в неё войти, "
        "\nправда для этого вам придется опустится на четвереньки, не очень то и удобно. "
        "\nДля кого вообще поставили эту дверь?")
  print("   1. войти в маленькую дверь")
  print("   2. остаться в комнате")

  choice = input("   Введите номер вашего выбора: ")

  if choice == "1":
    small_room()
  elif choice == "2":
    game_start_2()
  else:
    print("Неверный выбор. Попробуйте снова.")
    small_door()

def search_room():
  print("Вы рыщете по всем углам этой маленькой комнаты и в куче старых газет находите странного вида ключ. ")
  print("   1. взять ключ")
  print("   2. оставить ключ")

  choice = input("   Введите номер вашего выбора: ")

  if choice == "1":
    print("Вы кладете ключ себе в карман")
    inventory.append("Ключ")
    game_start_2()
  elif choice == "2":
    game_start_2()
  else:
    print("Неверный выбор. Попробуйте снова.")
    search_room()

def small_room():
  print("В новой комнате уже нет окна, поэтому источником света служит мерцающая лампочка на потолке."
        "\nЗато на стене висят несколько картин. Может, за одной из них что-то скрывается?")
  print("   1. осмотреть все картины")
  print("   2. вернуться в предыдущую комнату")

  choice = input("   Введите номер вашего выбора: ")

  if choice == "1":
    paint()
  elif choice == "2":
    game_start_2()
  else:
    print("Неверный выбор. Попробуйте снова.")
    small_room_2()

def small_room_2():
  print("Вы стоите перед картинами. Что вы собираетесь сделать?")
  print("   1. осмотреть все картины")
  print("   2. вернуться в предыдущую комнату")

  choice = input("   Введите номер вашего выбора: ")

  if choice == "1":
    paint()
  elif choice == "2":
    game_start_2()
  else:
    print("Неверный выбор. Попробуйте снова.")
    small_room()

def paint():
  print("За одной из картин вы находите скрытый сейф. Он закрыт и чтобы его открыть вам, очевидно, понадобится ключ.")
  print("   1. вставить ключ")
  print("   2. осмотреть картины")

  choice = input("   Введите номер вашего выбора: ")

  if choice == "2":
    small_room_2()
  elif choice == "1":
    if "Ключ" in inventory:
      print("Внутри сейфа находится еще один ключ. Судя по виду, он наверняка от какой-нибудь двери."
            "\nВы кладете его себе в карман")
      inventory.append("Ключ2")
      inventory.remove("Ключ")
      small_room_2()
    else:
      print("У вас нет ключа.")
      paint()
  else:
    print("Неверный выбор. Попробуйте снова.")
    paint()

if __name__ == "__main__":
 game_start()


 def paint_2():
   print("За одной из картин по прежнему находится сейф. Открыть вы его не можете, так как у вас нет нужного ключа.")
   print("   1. вставить ключ")
   print("   2. вернуться в предыдущую комнату")

   choice = input("   Введите номер вашего выбора: ")

   if choice == "2":
     small_room()
   elif choice == "1":
     if "Ключ" in inventory:
       print("Внутри сейфа находится еще один ключ. Судя по виду, он наверняка от какой-нибудь двери."
             "\nВы кладете его себе в карман")
       inventory.append("Ключ2")
       small_room_2()
     else:
       print("У вас нет ключа.")
       paint_2()
   else:
     print("Неверный выбор. Попробуйте снова.")
     paint_2()


 if __name__ == "__main__":
   game_start()