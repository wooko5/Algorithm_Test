N = int(input())
data_list = list(map(int, input().split()))
data_list.sort()
answer = data_list[0] * data_list[len(data_list)-1]
print(answer)