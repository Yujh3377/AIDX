import examCalculator as ex

score1 = int(input('1과목 점수 입력'))
score2 = int(input('2과목 점수 입력'))
score3 = int(input('3과목 점수 입력'))

print('총점:',ex.getTotalScore(score1,score2,score3))
print('평균:',ex.getAverageScore(score1,score2,score3))
print('합격여부:',ex.getPassFail(score1,score2,score3))

