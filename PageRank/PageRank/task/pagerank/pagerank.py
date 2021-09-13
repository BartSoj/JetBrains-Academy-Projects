import copy
import numpy as np
import numpy.linalg as la

mat_dim = int(input())
websites = input().split()
link_matrix = [[eval(j) for j in input().split()] for _ in range(mat_dim)]
link_matrix = np.array(link_matrix)
search = input()


def pagerank(link_matrix, d):
    r = 100 * np.ones(mat_dim) / mat_dim

    M = d * link_matrix + (1 - d) / mat_dim * np.ones(mat_dim)

    r_ = M @ r

    r_prev = copy.deepcopy(r_)
    r_next = M @ r_prev
    r_temp = 0

    while la.norm(r_prev - r_next) >= 0.01:
        r_temp = M @ r_next
        r_prev = r_next
        r_next = r_temp

    return r_next


pr = pagerank(link_matrix, 0.5)
websites = dict(zip(websites, pr.tolist()))
list_to_print = sorted(websites.items(), key=lambda x: (x[1], x[0]), reverse=True)[:5]
if search in websites:
    print(search)
for name, _ in list_to_print:
    if name != search:
        print(name)
