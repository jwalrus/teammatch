from teammatch import *


def test_match1():
    people = [
        Person(0, [0, 1]),
        Person(1, [0, 1]),
        Person(2, [0, 1]),
    ]

    teams = [
        Team(0, 2, [0, 1, 2]),
        Team(1, 1, [0, 1, 2])
    ]

    assignments = {t.name: t.assignment.people for t in match(people, teams)}
    assert assignments[0] == [0, 1]
    assert assignments[1] == [2]

def test_match2():
    people = [
        Person(0, [0, 1]),
        Person(1, [1, 0]),
        Person(2, [1, 0])
    ]

    teams = [
        Team(0, 2, [0, 1, 2]),
        Team(1, 1, [0, 1, 2])
    ]

    assignments = {t.name: t.assignment.people for t in match(people, teams)}
    assert assignments[0] == [0, 2]
    assert assignments[1] == [1]

def test_match3():

    people = [
        Person(0, [0, 1, 2, 3]),
        Person(1, [0, 1, 2, 3]),
        Person(2, [2, 0, 3, 1]),
        Person(3, [1, 0, 3, 2]),
        Person(4, [3, 0, 1, 2]),
        Person(5, [3, 2, 1, 0]),
        Person(6, [2, 3, 0, 1]),
        Person(7, [2, 1, 3, 0]),
        Person(8, [1, 3, 2, 0]),
        Person(9, [1, 0, 2, 3])
    ]

    teams = [
        Team(0, 4, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
        Team(1, 3, [1, 3, 5, 7, 9, 0, 2, 4, 6, 8]),
        Team(2, 2, [0, 2, 4, 6, 8, 1, 3, 5, 7, 9]),
        Team(3, 1, [4, 6, 2, 1, 8, 7, 9, 0, 3, 5])
    ]

    assignments = {t.name: t.assignment.people for t in match(people, teams)}
    assert assignments[0] == [0, 1, 8, 9]
    assert assignments[1] == [3, 5, 7]
    assert assignments[2] == [2, 6]
    assert assignments[3] == [4]
