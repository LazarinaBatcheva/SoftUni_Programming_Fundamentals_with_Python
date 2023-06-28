def shells_for_filling(electrons):
    filled_shells = []
    for shell in range(1, electrons + 1):
        current_shell = 2 * (shell ** 2)
        if current_shell <= electrons:
            filled_shells.append(current_shell)
            electrons -= current_shell
        else:
            filled_shells.append(electrons)
            break
    return filled_shells


number_of_electrons = int(input())
print(shells_for_filling(number_of_electrons))