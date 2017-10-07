# -*- coding:utf-8 -*-

class Lamp:
    LAMP = ['''
              .
         .    |    ,
          \   '   /
           ` ,-. '
        --- (   ) ---
             \ /
            _|=|_
           |_____|
        ''',
        '''
             ,-.
            (   )
             \ /
            _|=|_
           |_____|

    ''']
    def __init__(self):
        self.init = False
    def turn_on(self):
        self.init = True
        print self.LAMP[0]
    def turn_off(self):
        self.init = False
        print self.LAMP[1]
        
def run():
    lamp = Lamp()
    while True:
        command = str(raw_input('''
        ¿Qué deseas hacer?
            [p]render
            [a]pagar
            [s]alir
        '''))
        if command == "p":
            lamp.turn_on()
        elif command == "a":
            lamp.turn_off()
        else:
            break

if __name__=='__main__':
    run()
