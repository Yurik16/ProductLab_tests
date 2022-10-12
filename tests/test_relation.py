from main import check_relation
import pytest

net = (
    ("Ваня", "Лёша"), ("Лёша", "Катя"),
    ("Ваня", "Катя"), ("Вова", "Катя"),
    ("Лёша", "Лена"), ("Оля", "Петя"),
    ("Стёпа", "Оля"), ("Оля", "Настя"),
    ("Настя", "Дима"), ("Дима", "Маша")
)

@pytest.mark.one
def test_relation():
    assert check_relation(net, "Петя", "Стёпа") is True
    assert check_relation(net, "Маша", "Петя") is True
    assert check_relation(net, "Ваня", "Дима") is False
    assert check_relation(net, "Лёша", "Настя") is False
    assert check_relation(net, "Стёпа", "Маша") is True
    assert check_relation(net, "Лена", "Маша") is False
    assert check_relation(net, "Вова", "Лена") is True
