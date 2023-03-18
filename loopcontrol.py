import random


def main():
    rnum = random.randint(15, 35)
    loop_total = random.randrange(0,45)

    print(f'Random target : {rnum}')
    print(f'Total loops : {loop_total}')

    for number in range(loop_total):
        print(number,end='|')
        if number == rnum:
            print(f'\nRandom target found : {rnum}')
            break
        if number == loop_total-1:
            print(f'\nRandom target {rnum} not found within {loop_total} loops.')


if __name__ == "__main__":
    while True:
        main()
        user_input = input("'Enter/Return' to roll Again, 'exit' to quit:\n").lower()
        if user_input == 'exit':
            break
        else:
            continue