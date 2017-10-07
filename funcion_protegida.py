# -*- coding:utf-8 -*-
def protected(func):
    def wrapper(password):
        if password == "admin":
            return func()
        else:
            print("La contraseña es incorrecta")

    return wrapper

@protected
def protected_fun():
    print("tu contraseña es correcta.")

if __name__ == '__main__':
    pasword = str(raw_input("Ingresa tu contraseña: "))
    protected_fun(pasword)
