# 666 부터 차례대로 1씩 증가시키면서 '666' 문자열이 포함되는지 체크하면서 N을 센다
N=int(input())

count=0
end_number=666

while True:
    if "666" in str(end_number):
        count+=1
    if count==N:
        print(end_number)
        break
    end_number+=1

