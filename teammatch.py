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

