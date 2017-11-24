# 31 Создать генератор паролей, который будет генерировать случайные неповторяющиеся пароли по следующим правилам:
# Пароль состоит из 8 символов
# В пароле допускаются только латинские большие и маленькие буквы, цифры и символ подчеркивания
# Пароль обязательно должен содержать Большие и маленькие буквы и цифры


def password_maker(long):
    pass_str = "abcdefghijklmnopqrstuvwxyz_ABCDEFGHIJKLMNOPQRSTUVWXYZ_01234567890123456789012345_"
    import random

    k1 = k2 = k3 = 0
    while k1 == 0 or k2 == 0 or k3 == 0:
        password = ""
        for i in range(0, long):
            random_position = int(random.randint(0,80))
            random_symbol = pass_str[random_position]
            password = password + random_symbol

        imperative_symbol1 = "abcdefghijklmnopqrstuvwxyz"
        imperative_symbol2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        imperative_symbol3 = "0123456789"

        check_sum1 = 0
        check_sum2 = 0
        check_sum3 = 0

        for i in range (0, long):
            x = password[i]
            is1 = imperative_symbol1.find(x)
            is2 = imperative_symbol2.find(x)
            is3 = imperative_symbol3.find(x)
            check_sum1 = check_sum1 + is1
            check_sum2 = check_sum2 + is2
            check_sum3 = check_sum3 + is3
        k1 = check_sum1 + long
        k2 = check_sum2 + long
        k3 = check_sum3 + long


    return password

x = password_maker(8)
print("password = ", x)

