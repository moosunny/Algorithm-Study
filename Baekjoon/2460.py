import sys

train_list = []
for _ in range(10):
    train_list.append(list(map(int, sys.stdin.readline().split())))

max_answer = 0
tmp_people = 0
for i in range(10):
    tmp_people -= train_list[i][0]
    tmp_people += train_list[i][1]

    if tmp_people > max_answer:
        max_answer = tmp_people

print(max_answer)