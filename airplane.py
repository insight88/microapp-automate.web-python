import math
import random

num_people = 300

num_sim = 10
num_wrong = [0 for i in range(num_people)]
total_wrong = []
last_wrong = 0

for it in range(num_sim):
    seats_remaining = [i+1 for i in range(num_people)]
    seats_assigned = random.sample(seats_remaining, num_people)

    seat_first = random.sample(seats_remaining, 1)[0]
    seats_remaining.remove(seat_first)

    count_wrong = 0

    if seat_first != seats_assigned[0]:
        num_wrong[0] = num_wrong[0] + 1
        count_wrong = count_wrong + 1

    for i in range(2, num_people + 1):
        assigned = seats_assigned[i - 1]
        if assigned in seats_remaining:
            seats_remaining.remove(assigned)
        else:
            seat_alternative = random.sample(seats_remaining, 1)[0]
            num_wrong[0] = num_wrong[0] + 1
            count_wrong = count_wrong + 1
            seats_remaining.remove(seat_alternative)
    total_wrong.append(count_wrong)

print(total_wrong)
