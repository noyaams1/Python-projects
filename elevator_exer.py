
print("Elevator rules: 'U'- Moves up 1 floor 'D'- Moves down 1 floor")

def final_elevator_floor(instructions):
    current_floor=0
    for i in instructions:
        if i=='U':
            current_floor+=1
        elif i=='D' and current_floor > 0:
            current_floor-=1
    return current_floor


print(final_elevator_floor("UUUUUDD"))