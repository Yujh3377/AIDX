import statistics
scores=[]
hap=0
for i in range(10):
    scores.append(int(input("{}번 학생 점수입력:".format(i+1))))
    hap += scores[i]
avg = statistics.mean(scores)
max = max(scores)
min = min(scores)

for i in range (10):
    print("{}번 학생의 성적입니다.={}".format(i+1,scores[i]))
    
print("성적 합=",hap)
print("성적 평균=",avg)
print("성적 최대값=", maxScore)
print("성적 최소값=", minScore)

print("특정 점수이상의 학생 수 출력하기")
score =int(input("점수입력:"))
cnt = 0
for i in range(10):
    if scores[i]>=score:
        cnt += 1
print(scores)
print("{}점이상의 학생은 {}명입니다.".format(score,cnt))
