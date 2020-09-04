from datetime import time
from math import ceil


class TicketStatus:
    LIVE = 1
    PAID = 2


class FeeStructure:
    FIRST_HOUR = 2
    SUBSEQUENT_HOUR = 1


class Ticket:
    def __init__(self, spot, registration, entry_time=time(), ticket_status=TicketStatus.LIVE):
        self.spot = spot
        self.registration = registration.lower()
        self.entry_time = entry_time
        self.ticket_status = ticket_status

    def get_spot(self):
        return self.spot

    def get_registration(self):
        return self.registration

    def get_entry_time(self):
        return self.entry_time

    def get_ticket_status(self):
        return self.ticket_status

    def change_ticket_status(self, new_status):
        self.ticket_status = new_status
        return

    def calculate_fee(self, exit_time=time()):
        diff = (exit_time.hour - self.entry_time.hour) + (exit_time.minute - self.entry_time.minute)/60
        hours = ceil(diff)

        return FeeStructure.FIRST_HOUR + (hours - 1) * FeeStructure.SUBSEQUENT_HOUR


t1 = Ticket(95, 'WB26S5113', time(8, 0, 0))

print(t1.get_spot())
print(t1.get_registration())
print(t1.get_entry_time())
print(t1.get_ticket_status())

print(t1.calculate_fee(time(9, 30, 0)))
t1.change_ticket_status(TicketStatus.PAID)