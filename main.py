from recursos import MENU
from recursos import resources
from time import sleep


def load_resources():
    """Carga los recursos iniciales del archivo resources"""
    starting_resources = {}
    for key in resources:
        starting_resources[key] = resources[key]
    return starting_resources


def report():
    """Genera reporte de los insumos disponibles"""
    for key in quantities:
        if key == 'money':
            print(f'{key} : {quantities[key]} pesos')
        else:
            print(f'{key} : {quantities[key]} ml')
    print()


def check_other_option(an_option):
    if an_option == 'espresso' or an_option == 'cappuccino' or an_option == 'latte':
        return True
    else:
        print('Invalid option, please choose one of the following: espresso, latte or cappuccino')
        print()
        return False



def check_quantities(an_option):
    """Verifica si hay los insumos suficientes para el producto"""
    for ingredient in MENU[an_option]['ingredients']:
        if MENU[an_option]['ingredients'][ingredient] > quantities[ingredient]:
            print(f'Sorry, there is not enough {ingredient}')
            return False
    else:
        return True


def check_money(an_option):
    """Verifica si el dinero es suficiente e indica el cambio a devolver"""
    users_money = float(input(f'Deposit {MENU[an_option]["cost"]} pesos :  '))
    if users_money < MENU[an_option]["cost"]:
        print('Sorry, that is not enough money, money refunded')
        return {'flag' : False, 'change': 0}
    else:
        return {'flag' : True, 'change':  users_money - MENU[an_option]["cost"]}


def update_quantities(an_option):
    """actualiza los insumos y el dinero"""
    for ingredient in MENU[an_option]['ingredients']:
        quantities[ingredient] = quantities[ingredient] - MENU[an_option]['ingredients'][ingredient]

    quantities['money'] = quantities['money'] + MENU[an_option]['cost']


def prepare_product(an_option):
    print(f'preparing the {an_option}, wait a moment...')
    sleep(2.5)
    print(f'Here is your {an_option}, enjoy')


if __name__ == '__main__':
    quantities = load_resources()
    off_key = False
    while not off_key:
        user_change = {'change' : 0}
        option = input('What would you like? (espresso/latte/capuccino) : ')
        if option == 'off':
            off_key = True
        elif option == 'report':
            report()
        elif check_other_option(option):
            if check_quantities(option):
                user_change = check_money(option)
                if user_change['flag']:
                    update_quantities(option)
                    prepare_product(option)
        if user_change['change'] > 0:
            print(f'your change is {user_change["change"]}\n')


