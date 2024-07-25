import random
import time
import operator

OPERATORS = {"+": operator.add, "-": operator.sub, "*": operator.mul}
MIN_OPERAND = 2
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10


def generate_problem(existing_problems: set):
    while True:
        left = random.randint(MIN_OPERAND, MAX_OPERAND)
        right = random.randint(MIN_OPERAND, MAX_OPERAND)
        operator = random.choice(list(OPERATORS.keys()))
        expression = f"{left} {operator} {right}"
        if not expression in existing_problems:
            answer = OPERATORS[operator](left, right)
            existing_problems.add(expression)
            return expression, answer


def main():
    input("Press enter to start the challenge 🤙")
    print("-------------------------------------")

    wrong_attempts = 0
    start_time = time.time()
    existing_problems = set()

    for i in range(TOTAL_PROBLEMS):
        expression, answer = generate_problem(existing_problems)
        while True:
            try:
                user_answer = input(f"Problem #{i + 1}:\n{expression} = ")
                if int(user_answer) == answer:
                    break
                wrong_attempts += 1
            except ValueError:
                print("Please enter a valid number.")
                wrong_attempts += 1

    end_time = time.time()
    total_time = round(end_time - start_time, 2)

    print("-------------------------------------")
    print(
        f"Challenge Completed 🤙\nYou finished in {total_time} seconds with {wrong_attempts} wrong attempts"
    )


if __name__ == "__main__":
    main()
