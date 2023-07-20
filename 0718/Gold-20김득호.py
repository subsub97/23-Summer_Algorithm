# 숫자 입력 및 가공
num = int(input())
num += 1
num = list(map(int, list(str(num))))
flag = 0
# 중간값이 10이되는 경우가 발생할수도 있으니까
for i in range(2):
    # 반만 보면된다.
    for i in range(0, len(num) // 2 + 1):
        # 뒷자리가 크면 한자리수 높은 수를 1증가
        if num[i] < num[len(num) - i - 1]:
            num[len(num) - i - 2] += 1
        # 팬린드롬 대응하는수는 같게
        num[len(num) - i - 1] = num[i]
        # 두자리수는 초기화
        for i in range(len(num) - 1, -1, -1):
            if num[i] >= 10:
                flag = 1
                num[i], num[i - 1] = num[i] % 10, num[i - 1] + num[i] // 10
    if flag == 0:
        break

for n in num:
    print(n,end='')