# 학교 홈페이지에서 올해 3월~내년 2월까지의 학사일정 데이터를 Parsing하여
# 그것을 날짜(string):일정의 이름(string) 형태의 Key-Value를 가진 Dictionary로 변환한다.
# 그리고 그것을 json 형태로 data/ 디렉터리에 저장한다.(확장자는 .dat)
# 일정이 구간 형태로 되어있는 경우의 처리 방법:
## 예시) 19.09.10. ~ 19. 09. 12. 시험
### '19-09-10':'시험 1일차'
### '19-09-11':'시험 2일차'
### '19-09-12':'시험 2일차'
# 위와 같은 형태로 총 3개의 일정을 Dictionary에 저장하도록 한다.
# 이러한 기능을 하는 코드를 run()이라는 이름의 함수로 만들기 바란다.

# 새 Branch를 생성하고, 새 Branch에서 develop/DataManager를 Merge한 후 코딩을 시작하면 된다.
# 예시: git checkout -b feature/DataManager/ScheduleTableParser --> git merge develop/DataManager