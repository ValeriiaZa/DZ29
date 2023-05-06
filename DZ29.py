def generate_cube_numbers(end):
    for i in range(2, end):
        i = i ** 3
        if i <= end:
            yield i
        else:
            break

gen = generate_cube_numbers(1000)
