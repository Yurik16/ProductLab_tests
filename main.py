def check_relation(net: set, first: str, second: str) -> bool:
    def find_friends(net: set, name: str):
        return [tup[abs(tup.index(name) - 1)] for tup in net if name in tup]

    # Finding first handshake friends
    first_friends = find_friends(net, first)
    second_friends = find_friends(net, second)
    handshake_one = [x for x in first_friends if x in second_friends]
    if len(handshake_one) > 0:
        return True

    # Finding second handshake friends
    first_friends_plus = [find_friends(net, x) for x in first_friends]
    second_friends_plus = [find_friends(net, x) for x in second_friends]
    first_set = set().union(*first_friends_plus)
    second_set = set().union(*second_friends_plus)
    handshake_two = [x for x in first_set if x in second_set]
    return len(handshake_two) > 0


if __name__ == '__main__':
    net = (
        ("Ваня", "Лёша"), ("Лёша", "Катя"),
        ("Ваня", "Катя"), ("Вова", "Катя"),
        ("Лёша", "Лена"), ("Оля", "Петя"),
        ("Стёпа", "Оля"), ("Оля", "Настя"),
        ("Настя", "Дима"), ("Дима", "Маша")
    )

    assert check_relation(net, "Петя", "Стёпа") is True
    assert check_relation(net, "Маша", "Петя") is True
    assert check_relation(net, "Ваня", "Дима") is False
    assert check_relation(net, "Лёша", "Настя") is False
    assert check_relation(net, "Стёпа", "Маша") is True
    assert check_relation(net, "Лена", "Маша") is False
    assert check_relation(net, "Вова", "Лена") is True
