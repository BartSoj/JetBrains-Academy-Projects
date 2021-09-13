with open("salary.txt", "r") as f1, open("salary_year.txt", "w") as f2:
    f2.write('\n'.join([str(int(x) * 12) for x in f1]))
