print('''
             _                              
            | |                             
 _ __   ___ | | _____ _ __ ___   ___  _ __  
| '_ \ / _ \| |/ / _ \ '_ ` _ \ / _ \| '_ \ 
| |_) | (_) |   <  __/ | | | | | (_) | | | |
| .__/ \___/|_|\_\___|_| |_| |_|\___/|_| |_|
| |                                         
|_|
''')
print("Welcome to Ula'ula Island.")
print("I am Ash Ketchum here to Guide you to select your pokemon type.Answer the condition to know your type..") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
a = input('Youre at a cross road. Where do you want to go? Type "left" or "right"')
b = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type swim to swim across.")
c = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?")
if a == "left":
  print("Hm...nice choice go on")
if b == 'wait':
      print("You have patience ....")
if c == "red" or c=="RED":
  print('''
          Your pokemon is ...
                 ."-,.__
                 `.     `.  ,
              .--'  .._,'"-' `.
             .    .'         `'
             `.   /          ,'
               `  '--.   ,-"'
                `"`   |  \
                   -. \, |
                    `--Y.'      ___.
                         \     L._, \
               _.,        `.   <  <\                _
             ,' '           `, `.   | \            ( `
          ../, `.            `  |    .\`.           \ \_
         ,' ,..  .           _.,'    ||\l            )  '".
        , ,'   \           ,'.-.`-._,'  |           .  _._`.
      ,' /      \ \        `' ' `--/   | \          / /   ..\
    .'  /        \ .         |\__ - _ ,'` `        / /     `.`.
    |  '          ..         `-...-"  |  `-'      / /        . `.
    | /           |L__           |    |          / /          `. `.
   , /            .   .          |    |         / /             ` `
  / /          ,. ,`._ `-_       |    |  _   ,-' /               ` \
 / .           \"`_/. `-_ \_,.  ,'    +-' `-'  _,        ..,-.    \`.
  '         .-f    ,'   `    '.       \__.---'     _   .'   '     \ \
' /          `.'    l     .' /          \..      ,_|/   `.  ,'`     L`
|'      _.-""` `.    \ _,'  `            \ `.___`.'"`-.  , |   |    | \
||    ,'      `. `.   '       _,...._        `  |    `/ '  |   '     .|
||  ,'          `. ;.,.---' ,'       `.   `.. `-'  .-' /_ .'    ;_   ||
|| '              V      / /           `   | `   ,'   ,' '.    !  `. ||
||/            _,-------7 '              . |  `-'    l         /    `||
 |          ,' .-   ,' ||               | .-.        `.      .'     ||
 `'        ,'    `".'    |               |    `.        '. -.'       `'
          /      ,'      |               |,'    \-.._,.'/'
          .     /        .               .       \    .''
        .`.    |         `.             /         :_,'.'
          \ `...\   _     ,'-.        .'         /_.-'
           `-.__ `,  `'   .  _.>----''.  _  __  /
                .'        /"'          |  "'   '_
               /_|.-'\ ,".             '.'`__'-( \
                 / ,"'"\,'               `/  `-.|" mh







          ''')
elif c =="blue" or c =="BLUE":
  print('''
          Your pokemon is ...
                             ,-'"-.
             __...| .".  |
        ,--+"     ' |   ,'
       | .'   ..--,  `-' `.
       |/    |  ,' |       :
       |\...-+-".._|       |
     ,"            `--.     `.     _..-'+"/__
    /   .              |      :,-"'     `" |_'
 ..| .    _,....___,'  |    ,'            /\
.\'.__.-'  /V     |   '                ,'""
`. |  `:  \.       |  .               ,'         ,.-.
  `:       |       |  '             .^.        ,' ,"`.
    `.     |       | /               _.\.---..'  /   |     ,-,.
      `._  A      / j              ."       /   /    |   .',' |
         `. `...-' ,'             /        /._ /     | ,' /   |
           |"-----'             ,'        /   /-.__  |'  /    |
           | _.--'"'""`.       .         /   /     `"^-.,     |
           |"       ____\     j             j            `"--.|
           |  _.-""'     \    |             |                j
         _,+."_           \   |             |                |
        '    . `.     _.-"'.     ,          |                '
       |_    | `.`. ,'      `.   |          |               .
       | `-. |  ,'.\         .\   \         |              /
       |\   ;+-'   "\      ,'  `.  \        |             /
       '\\."         \ _.-'     ,`. \       '            /
        \\\           :       .'   `.`._     \          / `-..-.
         ``.          |    _." _...,:.._`.    `._     ,'   -. \'
          `.`.        |`".'__.'           `,...__"--`/  |   / |
            `.`.     _'    \|             ,'       ,'_  `..'  |..__,.
              `._`--".'     \`._      _,-'       ,' `-'  /    | .  ,'
                 `""'        `. `"'""'   ,-" _,-'    _ .'     '  `' `.
                               `-.._____:  |"       _," ."  ,'__,.."'
                                         `.|-...,.<'    `,_""'`./
                                             `.'   `"--'"''')
else:
  print('''
          Your pokemon is ...
          :::,
 '::::'._
   '.    '.                        __.,,.
     '.    '.                _..-'''':::
       \     \,.--""""--.,-''      _:'
   /\   \  .               .    .-'
  /  \   \                   ':'
 /    \  :                     :
/      \:                       :
\       :                       :
 \      :      ,--,         ,-,  :
  \    :      |(_):|       |():| :
   \   :     __'--'   __    '-'_  :
    \  :    /  \      \/      / \ :
     \  :  (    )             \_/ :
  .-'' . :  \__/   '--''--'      :
  \  . .-:'.                   .:
   \' :| :  '-.__      ___...-' :
    \::|:        ''''''          '.
  .,:::':  :                       '.
   \::\:   :                         '._
    \::    :     /             '-._     '.
     \:    :    /              .   :-._ :-'
      :    :   /               :   :  ''
      :   .'   )'.             :   :
       :  :  .'   '.          :   :
        : '..'      :      _.' _.:
         '._        :..---'\'''  _)
            '':---''_)      '-'-'
               '-'-' '''
       ''')

  else:
  print("To much risk😔....")
else :
 print("I hate right path ... No pokemon for you😒")
