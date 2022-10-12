def check_relation(net: set, first: str, second: str) -> bool:
    def find_friends(net: set, name: str):
        return [tup[abs(tup.index(name) - 1)] for tup in net if name in tup]

    first_friends = find_friends(net, first)
    second_friends = find_friends(net, second)
    return len([x for x in first_friends if x in second_friends]) > 0


if __name__ == '__main__':
    net = (
        ("Ваня", "Лёша"), ("Лёша", "Катя"),
        ("Ваня", "Катя"), ("Вова", "Катя"),
        ("Лёша", "Лена"), ("Оля", "Петя"),
        ("Стёпа", "Оля"), ("Оля", "Настя"),
        ("Настя", "Дима"), ("Дима", "Маша")
    )

    # assert check_relation(net, "Петя", "Стёпа") is True
    # assert check_relation(net, "Маша", "Петя") is True
    # assert check_relation(net, "Ваня", "Дима") is False
    # assert check_relation(net, "Лёша", "Настя") is False
    # assert check_relation(net, "Стёпа", "Маша") is True
    # assert check_relation(net, "Лена", "Маша") is False
    # assert check_relation(net, "Вова", "Лена") is True

    print(check_relation(net, "Петя", "Стёпа"))
    print(check_relation(net, "Маша", "Петя"))
    print(check_relation(net, "Ваня", "Дима"))
    print(check_relation(net, "Лёша", "Настя"))
    print(check_relation(net, "Стёпа", "Маша"))
    print(check_relation(net, "Лена", "Маша"))
    print(check_relation(net, "Вова", "Лена"))