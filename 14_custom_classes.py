"""
created by Nagaj at 19/06/2021
"""


class Attendee:
    """
    Common base class for all attendees
    """

    def __init__(self, name, tickets):
        self.name = name
        self.tickets = tickets

    def __repr__(self):
        return f"{self.name}-{self.tickets}"

    def is_equal(self, other):
        return self.__class__ == other.__class__

    def __eq__(self, other):
        if self.is_equal(other):
            return self.tickets == other.tickets
        raise ValueError

    def __gt__(self, other):
        if self.is_equal(other):
            return self.tickets > other.tickets
        raise ValueError

    def __ge__(self, other):
        if self.is_equal(other):
            return self.tickets >= other.tickets
        raise ValueError

    def __lt__(self, other):
        if self.is_equal(other):
            return self.tickets < other.tickets
        raise ValueError

    def __le__(self, other):
        if self.is_equal(other):
            return self.tickets <= other.tickets
        raise ValueError

    def display_attendee(self):
        print('Name : {}, Tickets: {}'.format(self.name, self.tickets))

    def add_ticket(self):
        self.tickets += 1
        print('{} tickets increased to {}'.format(self.name, self.tickets))


attendee = Attendee("John", 2)
attendee2 = Attendee("James", 4)

print(attendee > attendee2)
print(attendee >= attendee2)
print(attendee < attendee2)
print(attendee <= attendee2)
print(attendee2 > attendee)
print(attendee2 >= attendee)
print(attendee2 == attendee)

attendee.add_ticket()
attendee.add_ticket()
print(attendee2 == attendee)  # easy with magic methods

print(attendee.tickets == attendee2.tickets)  # without magic methods
