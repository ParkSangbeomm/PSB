1,2,3,4,5)
var2 <- c(1:5)
var3 <- seq(1,5) #연속
var4 <- seq(1,10, by=2) #2간격으로 10까지
var1 + var2 # 가능
#문자로 된 변수 만들기- ""
str1 <- "a"
str2 <- c("Hello","Hi","Ho")
#문자열은 더하면 결과값 없음
#2
x <- c(1,2,3)
mean(x)
min(x)
#여러문자열 합쳐서 하나로 만들기
str2 <- c("Hello","Good","Morning")
paste(str2, collapse=",") #쉼표찍으면서 합치기
#3
#ggplot사용하면 다양한 함수 가능 install.packages("ggplot2") 이후에 library(ggplot2) 해야함
#qplot()은 빈도 막대 그래프 출력
x <- c("a","a","b","c","c","c")
qplot(x)
#ggplot2에는 미국환경보호국에서 공개한 mpg라는 자료가 있다
qplot(data=mpg,x=hwy) #데이터는 mpg, x축에 hwy변수 저장해 그래프 생성
#data, x, y으로 정하고 geom으로 그래프 형태바꿈 line:선 boxplot:상자그림 colour=drv면 drv별 색 표현
#?qplot 하면 함수 메뉴얼 출력

#둘째마당
#가로가 열 세로가 행
english <- c(90,80,60,70)
math <- c(50,60,100,20)
df_midterm <- data.frame(english,math) #english, math로 데이터 프레임 생성해서 할당
class <- c(1,1,2,2)
df_midterm <- data.frame(english,math,class)
mean(df_midterm$english) # df_midterm의 english로 평균산출
#데이터 프레임 한번에 만들기
df_midterm <- data.frame(english = c(90,80,60,70),
                         math = c(50,60,100,20),
                         class = c(1,1,2,2))
#외부데이터사용하기
#4
#엑셀파일 읽어올때 readxl패키지 다운
df_exam <- read_excel("excel_exam.xlsx")
df_exam <- read_excel("d:/easy_r/excel_exam.xlsx") #절대경로
#read_excel은 첫번째 줄을 변수명으로 받아들여 데이터 손실이 날수도 있음 이럴때 col_names=F사용
df_exam <- read_excel("excel_exam.xlsx", col_names=F)
df_exam <- read_excel("excel_exam.xlsx", sheet=3) #n번째 시트를 가져옴
#csv파일 읽어올때
df_csv_exam <- read.csv("csv_exam.csv")
#첫번째 행에 변수명이 없으면 header=F 해 주어야 함
#문자가 들어 있는 파일을 불러올 때는 stringAsFactors=F사용
#csv파일로 저장하기
write.csv(df_midterm, file="df_midterm.csv")
#RData파일로 저장하기
save(df_midterm, file="df_midterm.rda")
rm(df_midterm) #dataframe삭제
load("df_midterm.rda") #rda파일 불러오기

#5
exam <- read.csv("csv_exam.csv")
head(exam, 10) #앞에서부터 10줄 읽어오기 기본은 6줄
tail(exam, 10) #뒤에서부터 10줄 읽어오기 기본은 6줄
View(exam) #데이터 뷰어 창에서 데이터 확인
dim(exam) #행, 열 출력
str(exam) #속성 파악하기
summary(exam) #요약 통계량 산출하기
#ggplot2에 mpg데이터 불러와 데이터 프레임 만들기
mpg <- as.data.frame(ggplot2::mpg)
#dplyr패키지 중에 변수명 바꾸기
df_raw <- data.frame(var = c(1,2,1),
                     var2 = c(2,3,2))
df_new <- df_raw #복사본 만들기
df_new <- rename(df_new, v2=var2) #이름 바꾸기
#파생변수 만들기
df_raw <- data.frame(var = c(1,2,1),
                     var2 = c(2,3,2))
df_raw$var_sum <- df_raw$var1+df_raw$var2
hist(x$total) # x에 total을 히스토그램으로 표현
#합격 판정 변수 만들기
mpg$test <- ifelse(mpg$total>=20, "pass", "fail")
#중첩조건문사용
mpg$test <- ifelse(mpg$total>=30, "A",
                   ifelse(mpg$total>=20, "B", "C"))
table(mpg$test) #빈도확인
qplot(mpg$test) #막대 그래프 생성

#6
#자유자재로 데이터 가공하기
exam <- read.csv("exam_csv.csv")
exam %>% filter(class == 1) #class가 1일인거 모아서 출력
#그리고 > &  이거나 > |
exam %>% filter(class %in% c(1,3,5))
#추출한 행으로 데이터 만들기
class1 <- exam %>% filter(class == 1)
class2 <- exam %>% filter(class == 2)
exam %>% select(english) #변수 추출
exam %>% select(-math) #변수 제외
#함수조합하기
exam %>%
        filter(class == 1) %>%
        select(english)
exam %>% arrange(desc(math)) #오름차순이 기본, 이렇게하면 내림차순
exam %>% arrange(class, math) #두개 차례로 오름차순
exam %>% mutate(total = math + english + science) %>%
         head   #파생변수 추가하기
exam %>% mutate(test = ifelse(science >= 60, "pass", "fail")) %>%
         head # mutate에 ifelse적용가능
exam %>% summarise(mean_math = mean(math)) #math 평균산출
exam %>%
    group_by(class) %>%
    summarise(mean_math = mean(math))
#문제 : 회사별로 "suv" 자동차의 도시 및 고속도로 통합 연비 평균을 구해 내림차순으로 정렬하고, 1-5위까지 나열
#절차 : 1. 회사별로 분리 -> group_by()
        2. suv 추출 -> filter()
        3. 통합 연비 변수 생성 -> mutate()
        4. 통합 연비 평균 산출 -> summarise()
        5. 내림차순 정렬 -> arrange()
        6. 1-5위 출력 -> head()
mpg %>% group_by(manufacturer) %>%
        filter(class == "suv") %>%
        mutate(tot = (cty+hwy)/2) %>%
        summarise(mean_tot = mean(tot)) %>%
        arrange(desc(mean_tot)) %>%
        head(5)
#데이터 합치기
test1 <- data.frame(id = c(1:5),
         midterm = c(60,80,70,90,85))
test2 <- data.frame(id = c(1:5),
         final = c(70,83,65,95,80))
total <- left_join(test1, test2, by="id") #가로로 합치기

group1 <- data.frame(id = c(1:5),
         midterm = c(60,80,70,90,85))
group2 <- data.frame(id = c(1:5),
         final = c(70,83,65,95,80))
total <- bind_rows(group1, group2) #세로로 합치기
#빠진 데이터 이상한 데이터 제거하기
df <- data.frame(sex = c("M","F",NA,"M","F"),
                 score = c(5,4,3,4,NA))
is.na(df) #boolean 형태로 결측치 확인 table로 표현하면 빈도수 출력
df_nomiss <- df%>%filter(!is.na(score) & !is.na(sex))
df_nomiss <- na.omit(df)
mean(df$score, na.rm=T) #결측치 제외하고 평균산출
exam <- read.csv("csv_exam.csv")
exam[c(3,8,15),"math"] <- NA #math에서 3,8,15번째에 NA값 저장
exam %>% summarise(mean_math = mean(math, na.rm = T))

outlier <- data.frame(sex = c(1,2,1,3,1),
                      score = c(5,,3,4,2,6))
outlier$sex <- ifelse(sex >= 2,NA,outlier$sex)
outlier$score <- ifelse(score>=5,NA,outlier$score)
outlier%>%filter(!is.na(sex) & !is.na(score)) %>% group_by(sex) %>% summarise(mean_score = mean(score))
#8
#그래프만들기
ggplot(data=mpg, aes(x=displ,y=hwy)) #x.y축 정해서 배경 설정
#dplyr함수들은 %>%로 연결, ggplot2 함수들은 +로 연결
ggplot(data=mpg, aes(x=displ,y=hwy)) + geom_point() #산점도 추가
# +xlim(3,6) +ylib(10,30) 축 범위 지정
#막대 그래프 : geom_col()
ggplot(data=mpg, aes(x=reorder(drv,-mean_hwy),y=mean_hwy))+geom_col() #크기순정렬
ggplot(data=mpg, aes(x=drv)) + geom_bar() #빈도그래
#geom_line() 선그래 geom_boxplot() #상자그래프
