from a_ops import add, sub, mul, div
from file_merger import merge
from passw import generate

# result_add = add(5, 3.5)
# result_subtract = sub(8, 2.5)
# result_multiply = mul(4, 1.5)
# result_divide = div(10, 2)

# print("Addition:", result_add)
# print("Subtraction:", result_subtract)
# print("Multiplication:", result_multiply)
# print("Division:", result_divide)

# file_paths = ['file1.txt', 'file2.txt', 'file3.txt']
# output_path = 'merged_file.txt'
# custom_order = [2, 0, 1]

# merge(file_paths, output_path, order=custom_order, separator='\n\n')

password = generate(12, True, True, True)
print(password)