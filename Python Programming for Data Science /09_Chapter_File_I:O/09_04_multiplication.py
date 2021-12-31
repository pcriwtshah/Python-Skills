#Write multiplication table from 2 to 20 in a folder Multiplication_Table

for i in range(2, 21):
    with open(f'Multiplication_Tables/Multiplication Table of {i}.txt', 'w') as f:
        for j in range(1,11):
            f.write(f"{i} X {j} = {i*j}")
            if j!=10:
                f.write('\n')