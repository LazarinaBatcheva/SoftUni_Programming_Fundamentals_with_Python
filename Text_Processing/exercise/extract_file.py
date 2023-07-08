path_to_a_file = input().split("\\")
filename, extension = path_to_a_file[-1].split(".")
print(f"File name: {filename}\nFile extension: {extension}")
