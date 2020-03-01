class Bid:
    def __init__(self, name, choice):
        self.name = name
        self.choice = choice

    def __repr__(self):
        return f"<Bid(name={self.name}, choice={self.choice})>"

class Assignment:
    def __init__(self, capacity, preferences, bids):
        self.people = Assignment._take(capacity, preferences, bids)

    def __repr__(self):
        return f"<Assignment(people={self.people})>"

    @staticmethod
    def _take(n, prefs, bids, default = -1):
        def gen():
            for x in [y for y in prefs if y in bids]:
                yield x
            while True:
                yield default

        return [ x for _,x in zip(range(n), gen()) ]

class Person:
    def __init__(self, name, preferences):
        self.name = name
        self.preferences = preferences

    def top_choice(self):
        return self.preferences[0]

    def update_preferences(self, teams):
        top = teams[self.top_choice()]
        if self.name not in top.assignment.people:
            new_prefs = [x for x in self.preferences if x != top.name]
            return Person(self.name, new_prefs)
        return Person(self.name, self.preferences)

    def make_bid(self):
        return Bid(self.name, self.preferences[0])

    def __repr__(self):
        return f"<Person(name={self.name}, preferences={self.preferences})>"


class Team:
    def __init__(self, name, capacity, preferences, assignment = []):
        self.name = name
        self.capacity = capacity
        self.preferences = preferences
        self.assignment = assignment

    def update_assignment(self, bids):
        team_bids = [bid.name for bid in bids if bid.choice == self.name]
        return Team(self.name,
                    self.capacity,
                    self.preferences,
                    Assignment(self.capacity, self.preferences, team_bids)), len(team_bids) > self.capacity

    def __repr__(self):
        return f"<Team(name={self.name}, assignment={self.assignment})>"


def match(people, teams):
    bids = [p.make_bid() for p in people]
    teams, rejections = zip(*[team.update_assignment(bids) for team in teams])
    if any(rejections):
        people = [p.update_preferences(teams) for p in people]
        return match(people, teams)
    return teams



def main():
    people = [
        Person(0, [0, 1]),
        Person(1, [0, 1]),
        Person(2, [0, 1]),
    ]

    teams = [
        Team(0, 2, [0, 1, 2]),
        Team(1, 1, [0, 1, 2])
    ]

    print(f"test 1 = {match(people, teams)}")

    people = [
        Person(0, [0, 1]),
        Person(1, [1, 0]),
        Person(2, [1, 0])
    ]

    teams = [
        Team(0, 2, [0, 1, 2]),
        Team(1, 1, [0, 1, 2])
    ]

    print(f"test 2 = {match(people, teams)}")

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

    print(f"test 3 = {match(people, teams)}")


if __name__ == '__main__':
    main()