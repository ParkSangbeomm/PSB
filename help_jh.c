//정현이형 도와주면서 만든 c파일
//파일을 읽고 그 파일에 알파벳과 숫자의 빈도를 출력
#include <stdio.h>
#include <string.h>

int main(void) {
  /*
  문장전체를 읽어온 후에 만약 문자이면 아스키코드로 바꾼값에 비교하여
  array[i]번째에 저장하고 

  
  char d='A';
  char c='a';
  char b='Z';
  char a='z';
  printf("A:%d \nZ:%d \na:%d \nz:%d\n\n\n\n",d,b,c,a);

  char str[100];
  int len;
  int cnt[26]={0};
  int num[10]={0};

  printf("Input : ");
  scanf("%[^\n]s",str);
  len=strlen(str);
  for(int i=0;i<len;i++){
    if((str[i] >= 'A' && str[i] <='Z') || (str[i] >= 'a' && str[i] <='z')){
      if(str[i] <='Z')
        cnt[str[i]-'A']++;
      else
        cnt[str[i]-'a']++;
    }
    else
      num[str[i]-'0']++;
  }
  for(int i=0;i<26;i++){
    //if(cnt[i])
      printf("%c : %d\n",'A'+i,cnt[i]);
  }
  for(int i=0;i<10;i++)
    printf("%d : %d\n",0+i,num[i]);
  */
  FILE* fp;
  fp=fopen("input.txt","rt");
  int ch;
  int cnt[26]={0};
  int num[10]={0};
  //fopen_s(fp,"input.txt","rt");

  while(!feof(fp)){
    ch=getc(fp);
    if((ch >= 'A' && ch <='Z') || (ch >= 'a' && ch <='z')){
      if(ch <='Z')
        cnt[ch-'A']++;
      else
        cnt[ch-'a']++;
    }
    else
      num[ch-'0']++;
  }

  for(int i=0;i<26;i++){
    //if(cnt[i])
      printf("%c : %d\n",'A'+i,cnt[i]);
  }
  for(int i=0;i<10;i++)
    printf("%d : %d\n",0+i,num[i]);
  return 0;
}
