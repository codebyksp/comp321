N=int(input())
for i in range(N):
    task = input()
    if task == 'P=NP':
        print('skipped')
    else:
        print(eval(task))