# Scenery: Front poarch, First Lobby, Second Lobby, Kitchen, Dungeon, Graveyard

player_Items = {}

import time

manor_front_view = ''' 
  *         .              *            _.---._      
                             ___   .            ___.'       '.   *
        .              _____[LLL]______________[LLL]_____     \\
                      /     [LLL]              [LLL]     \     |
                     /____________________________________\    |    .
                      )==================================(    /
     .      *         '|I .-. I .-. I .--. I .-. I .-. I|'  .'
                  *    |I |+| I |+| I |. | I |+| I |+| I|-'`       *
                       |I_|+|_I_|+|_I_|__|_I_|+|_I_|+|_I|      .
              .       /_I_____I_____I______I_____I_____I_\\
                       )================================(   *
       *         _     |I .-. I .-. I .--. I .-. I .-. I|          *
                |u|  __|I |+| I |+| I |<>| I |+| I |+| I|    _         .
           __   |u|_|uu|I |+| I |+| I |~ | I |+| I |+| I| _ |U|     _
       .  |uu|__|u|u|u,|I_|+|_I_|+|_I_|__|_I_|+|_I_|+|_I||n|| |____|u|
          |uu|uu|_,.-' /I_____I_____I______I_____I_____I\`'-. |uu u|u|__
          |uu.-'`      #############(______)#############    `'-. u|u|uu|
         _.'`              ~"^"~   (________)   ~"^"^~           `'-.|uu|
      ,''          .'    _                             _ `'-.        `'-.
  ~"^"~    _,'~"^"~    _( )_                         _( )_   `'-.        ~"^"~
      _  .'            |___|                         |___|      ~"^"~     _
    _( )_              |_|_|          () ()          |_|_|              _( )_
    |___|/\/\/\/\/\/\/\|___|/\/\/\/\/\|| ||/\/\/\/\/\|___|/\/\/\/\/\/\/\|___|
    |_|_|\/\/\/\/\/\/\/|_|_|\/\/\/\/\/|| ||\/\/\/\/\/|_|_|\/\/\/\/\/\/\/|_|_|
    |___|/\/\/\/\/\/\/\|___|/\/\/\/\/\|| ||/\/\/\/\/\|___|/\/\/\/\/\/\/\|___|
    |_|_|\/\/\/\/\/\/\/|_|_|\/\/\/\/\/[===]\/\/\/\/\/|_|_|\/\/\/\/\/\/\/|_|_|
    |___|/\/\/\/\/\/\/\|___|/\/\/\/\/\|| ||/\/\/\/\/\|___|/\/\/\/\/\/\/\|___|
    |_|_|\/\/\/\/\/\/\/|_|_|\/\/\/\/\/|| ||\/\/\/\/\/|_|_|\/\/\/\/\/\/\/|_|_|
    |___|/\/\/\/\/\/\/\|___|/\/\/\/\/\|| ||/\/\/\/\/\|___|/\/\/\/\/\/\/\|___|
~""~|_|_|\/\/\/\/\/\/\/|_|_|\/\/\/\/\/|| ||\/\/\/\/\/|_|_|\/\/\/\/\/\/\/|_lc|~""~
   [_____]            [_____]                       [_____]            [_____]
'''

Locked_Dungeon_Door = '''

      ______
   ,-' ;  ! `-.
  / :  !  :  . \\
 |_ ;   __:  ;  |
 )| .  :)(.  !  |
 |"    (##)  _  |
 |  :  ;`'  (_) (
 |  :  :  .     |
 )_ !  ,  ;  ;  |
 || .  .  :  :  |
 |" .  |  :  .  |
 |mt-2_;----.___|
'''

# Boolean values:

In_Lobby = False

In_Kitchen = False

In_SecondLobby = False

In_Graveyard = False

In_Dungeon = False

Has_Key = False

# Functions for entering scenes:

def Enter_Manor():
    global In_Lobby
    global In_Kitchen
    global In_SecondLobby
    global In_Graveyard
    global In_Dungeon
    time.sleep(0.5)
    print("Entering manor...")
    time.sleep(1.5)
    print(

        '''


                  ~@< >@~     
                            ~@@@@~|~@@@@~  
                                ..|..      
    .                          {II\III}                         . 
  . I .                         `UUU`                         . I . 
  I~@~I                           O                           I~@~I 
   ;U;                  ..                                     ;U; 
                       .II.                           . 
                      .I;;I.                        . I .             . 
          .           I~@@~I           .            I~@~I           . I . 
        . I .         ;(;;);         . I .          ;(_);_          I~@~I 
      __I~@~I__       `;)(;`       __I~@~I__        |\    \_________;(_);__ 
_____/  ;(_);  \________)(________/  ;(_);  \_______| \____________________\__ 
(__ /___________\ __)  (__)  (__ /___________\ __)  | |                    | 
{__}    (   )    {__}        {__}    (   )    {__}  | |  ~@~         ~@~   | 
 )(     _) (_     )(          )(     _) (_     )(   | |                    | 
                                                     \|____________________| 
                                                                 . 
          .                             .                      . I . 
        . I .                         . I .                  __I~@~I__ 
      __I~@~I__                     __I~@~I__               /  ;(_);  \ 
     /  ;(_);  \                   /  ;(_);  \         (__ /___________\ __) 
(__ /___________\ __)         (__ /___________\ __)    {__}    (   )    {__} 
{__}    (   )    {__}         {__}    (   )    {__}     )(     _) (_     )( 
 )(     _) (_     )(           )(     _) (_     )(  

'''
    )
    In_Lobby = True
    In_Kitchen = False
    In_SecondLobby = False
    In_Graveyard = False
    In_Dungeon = False

def Enter_Kitchen():
    global In_Lobby
    global In_Kitchen
    global In_SecondLobby
    global In_Graveyard
    global In_Dungeon
    time.sleep(0.5)
    print("Entering kitchen...")
    time.sleep(1.5)
    In_Kitchen = True
    print("Value of 'In Kitchen' =", In_Kitchen)
    In_SecondLobby = False
    In_Graveyard = False
    In_Dungeon = False
    In_Lobby = False
    print(

      '''
  __________________________________________________________________________    
 /|    |__I__I__I__I__I__I__I__I__I_|       _-       /        %         |
  | _- |_I__I__I__I__I__I__I__I__I__|-_              .        %     _-  | 
  |    |__I__I__I__I__I__I__I__I__I_|                /        %         |
  |  - |_I__I__I__I__I__I__I__I__I__|               ,j,      %w ,      |
  | -  |__I__I__I__I__I__I__I__I__I_|  -_ -        / ) \    /%mMmMm.   |
  |    |_I__I__I__I__I__I__I__I__I__|             //|  |   ;  `.,,'    |
  |-_- /                            \             w |  |   `.,;`       |
  |   /                              \    -_       / ( |    ||         |
  |  /                                \           //\_'/    (.\    -_  |
  | /__________________________________\          w  \/   -  ``'       |
  | |__________________________________|                               |
  |    |   _______________________   |     _-            -             |
  |_-  |  |                       |  |                        _-       |
  |    |  |                     _ |  |  T  T  T  T  T                  |
  | _-_|  |    __.'`'`'`''`;__ /  |  |  |  |  |  |  |        _-     -  |
  |    |  | _/U  `'.'.,.,".'  U   |  |  | (_) |  |  |                  |
  |    |  |   |               |   |  | / \    @ [_]d b    _@_     |    |   
  |    |  |   |      `', `,   |   |  | |_|   ____         [ ]     |    |
  |_-  |  |   |   `') ( )'    |   |  | ______\__/_________[_]__   |    | 
  |    |  |   |____(,`)(,(____|   |  |/________________________\  |    |
  |    |  |  /|   `@@(@@)@)'  |\  |  | ||            _____   ||   |    |
  |    |  | //!\  @@)@@)@@@( /!\\ |  | ||   _--      \   /   ||  /|\   |
  |__lc|__|/_____________________\|__|_||____________/###\___||_|||||__|
 / -_  _ -      _ -   _-_    -  _ - _ -|| -_    _  - \___/_- || |||||-_ \ 
      '''
    )

    time.sleep(1)

    print("Hmmm... this kitchen looks very dirty")

    time.sleep(1)

    player_Kitchen_Choice = input("Should I search this area (S), or go back to the Lobby (L)").upper()

    if player_Kitchen_Choice == "L":
      Enter_Manor()
    elif player_Kitchen_Choice == "S":
      Search_Scenery()

def Enter_SecondLobby():
    global In_Lobby
    global In_Kitchen
    global In_SecondLobby
    global In_Graveyard
    global In_Dungeon
    time.sleep(0.5)
    print("Entering Second lobby...")
    time.sleep(1.5)
    In_Lobby = False
    In_Kitchen = False
    In_SecondLobby = True
    In_Graveyard = False
    In_Dungeon = False
    print(

      '''
      |    ~@~      ~@~                                          ~@~      ~@~    |
|\__/\__/\__/\__/\__/\__/\__/\__/\__/\__/\__/\__/\__/\__/\__/\__/\__/\__/\__/\__/ 
|. . . . . . . . . . .[___|___|___|___|___|__]. . . . . . . . . . . . . . . .|
| . . . . . . . . . . [_|___|___|___|___|___|] . . . . . . . . . . . . . . . |
|. . . . . . . . . . .[___|___|___|___|___|__]. . . . . . . . . . . . . . . .|
| . . . .  _  . . . . [_|___|___|___|___|___|] . .  _  . . . . . . .  _  . . |
|. . . .  /_\  . . . .[__|___|___|___|___|___]. .  /_\  . . . . . .  /_\  . .|
| . . . . =|= . . . . [_|___/          \___|_] . . =|= . . . . . . . =|= . . |
|. . . . . . . . . . .[|___| ~ LOUNGE ~ |___|]. . . . . . . . . . . . . . . .|
|=====================[__|__\__________/_|___]================____===========|
|                     [___|___|___|___|___|__]               | |  \          |
|           ,         [_|___|___|___|___|___|]               | |   \_______  |
|          ,I,    ,;,/________________________\,;,          _|_|___________) |
|/|   ____;(;);__;(;);                        ;(;); /|     /   | ,.________) |
|||__ !!!!!;;;!!!!=;============================;=  ||__  /____|/ .________| |
||/_/|!!!!!!;!!!!!![_|_|_]================[_|_|_]___|/_/|_|______/_______)(__lc
/|' |'  |'     '|  [__|__]       `(       [__|__]   |' |'[|)(            ()   \
 '  '   '       '  [_|_|_] o     ) (    o [_|_|_]   '  '   ()                   
                   [__|__] |    ( ) )   | [__|__]                      ,
                   [_|_|_] |---@@@@@@---| [_|_|_]           /|        ,I,       |\   
                   [__|__]/!\ @@@@@@@@ /!\[__|__]           ||   ____;(;);____  ||
                  /______________________________\          ||__ !!!!!;;;!!!!!__||
   ,             |________________________________|         |/_/|!!!!!!;!!!!!!\_\|
  ,I,       |\   `================================`         || ||  ||     || || ||
_;(;);____  ||  `==================================`        |  |   |       |  |  |
!!;;;!!!!!__|| `====================================`
!!!;!!!!!!\_\|
====================================================================================
      '''
    )

def Enter_Graveyard():
    global In_Lobby
    global In_Kitchen
    global In_SecondLobby
    global In_Graveyard
    global In_Dungeon
    time.sleep(0.5)
    print("Entering graveyard...")
    time.sleep(1.5)
    In_Lobby = False
    In_Kitchen = False
    In_SecondLobby = False
    In_Graveyard = True
    In_Dungeon = False  
    print(

      '''
      
   *        *          __ *      ,    .     *         . 
                ,__   /     _ /' *        .          *
   .    *          \\/---./  \\    `/_          *     
               *  .'\\, // './\\  //    *          
                 / --\\//    \ \\//   ___       .    *  .
    *    .      :     \#\     :/ /  //--``        
                '  __/ \ (_/  ( (  //       *       .   *
 .            *  \  _\  \ \/ / \ \//  .   _  
      *           _( )_  ) )'_//\  \    _( )_ .   * 
   _       .      |___|\/#(.--'_/"\ \  /|___|        .   * _ 
 _( )_            |_|_|\ ,/        \ \//|_|_|            _( )_
 |___|/\/\/\/\/\/\|___|/#(,%.-----.%\  (|___|/\/\/\/\/\/\|___|
 |_|_|\/\/\/\/\/\/|_|_|  /% |R.I.P| %\  |_|_|\/\/\/\/\/\/|_|_|
 |___|/\/\/\/\/\/\|___| /%  |_____|  %) |___|/\/\/\/\/\/\|___|
 |_|_|\/\/\/\/\/\/|_|_|(  [_________] ~"|_|_|\/\/\/\/\/\/|_|_|
 |___|/\/\/\/\/\/\|___|~  ~~"^"^"^"~~   |___|/\/\/\/\/\/\|___|
 |_|_|\/\/\/\/\/\/|_|_|     _-      _-  |_|_|\/\/\/\/\/\/|_|_|
 |___|/\/\/\/\/\/\|___| _-      _-      |___|/\/\/\/\/\/\|___|
 |_lc|\/\/\/\/\/\/|_|_|   _-         _- |_|_|\/\/\/\/\/\/|_|_|
[_____]~~"^""^"~~[_____]         _-    [_____]~~"^""^"~~[_____]
~~"^"~~          ~~"^"~~      _-       ~~"^"~~          ~~"^"~~                           

~.:.~.:.~.:.~.:.~.:.~.:.~.:.~.:.~.:.~.:.~.:.<>.:.~.:.~.:.~.:.~.:.~.:.~.:.~.:.~.:.~.:.~.:.~

~.:.~.:.~.:.~.:.~.:.~.:.~.:.~.:.~.:.~.:.~.:.<>.:.~.:.~.:.~.:.~.:.~.:.~.:.~.:.~.:.~.:.~.:.~
      '''
    )

def Enter_Dungeon():
    global In_Lobby
    global In_Kitchen
    global In_SecondLobby
    global In_Graveyard
    global In_Dungeon
    time.sleep(0.5)
    print("Entering dungeon...")
    time.sleep(1.5)
    In_Lobby = False
    In_Kitchen = False
    In_SecondLobby = False
    In_Graveyard = False
    In_Dungeon = True

    print(
      '''
         _________________________________________________________
 /|     -_-                                             _-  |\l
/ |_-_- _                                         -_- _-   -| \   
  |                            _-  _--                      | 
  |                            ,                            |
  |      .-'````````'.        '(`        .-'```````'-.      |
  |    .` |           `.      `)'      .` |           `.    |          
  |   /   |   ()        \      U      /   |    ()       \   |
  |  |    |    ;         | o   T   o |    |    ;         |  |
  |  |    |     ;        |  .  |  .  |    |    ;         |  |
  |  |    |     ;        |   . | .   |    |    ;         |  |
  |  |    |     ;        |    .|.    |    |    ;         |  |
  |  |    |____;_________|     |     |    |____;_________|  |  
  |  |   /  __ ;   -     |     !     |   /     `'() _ -  |  |
  |  |  / __  ()        -|        -  |  /  __--      -   |  |
  |  | /        __-- _   |   _- _ -  | /        __--_    |  |
  |__|/__________________|___________|/__________________|__|
 /                                             _ -        lc \\
/   -_- _ -             _- _---                       -_-  -_ \\
 
      '''
    )

def Search_Scenery():
    
    global Has_Key
    
    print("Value of 'In Kitchen' =", In_Kitchen)

    if In_Kitchen == True:
      print("You have recieved the key!")
      Has_Key = True
      Enter_Manor
    else:
      print("Theres nothing here")

# Welcome statement

print("Welcome to the Spooky Manor. Your objective is to find the special item and escape with it.")

time.sleep(1)

print(manor_front_view)

player_Enter_Game = input("Type 'ok' when ready: ").lower()

if player_Enter_Game == "ok":

  Enter_Manor()
    
  print("This seems like the Lobby...")

  time.sleep(1)

  player_Lobby_Choice = input("Should I search this area (S), Enter the Kitchcen (K), Enter the Second Lobby (2), or Leave this place (L)?").upper()

if player_Lobby_Choice == "K":
  
  Enter_Kitchen()


elif player_Lobby_Choice == "2":
  Enter_SecondLobby()

  time.sleep(1)

  print("Boring- I should move on.")

  time.sleep(1)

  player_SecondLobby_Choice = input("Should I searcg this earch (S), or go back to the Lobby (L)").upper()

elif player_Lobby_Choice == "S":
  Search_Scenery()

   