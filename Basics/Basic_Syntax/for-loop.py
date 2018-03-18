# using range

initial_value = 0
final_value = 100
step_count = 2

for i in range(initial_value, final_value, step_count):
    print(i)


# using list

for i in [1, 2, 4, 8, 16, 32]:
    print(i)

# generator
generated_list = [i for i in range(10)]
print(generated_list)