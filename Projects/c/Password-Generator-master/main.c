#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <math.h>
#include "functions.h"

int main()
{
    const int alphabetlength=strlen(alphabet);
    while(1){
    system("cls");
    letternumber=getletternumber();
    if(letternumber==-1){
    continue;
    }else{
    char *password;
    password=(char*)calloc(letternumber+1,sizeof(char));
    generatepassword(letternumber,password,alphabetlength);
    getpassworddescription(&passworddescription);

    FILE *fp;
    fp=fopen("Passwords.txt", "a");

    printfile(fp,passworddescription,password);

    free(password);
    fclose(fp);
    }
    int quit=quitmessage();
    if(quit=='q'||quit=='Q'){
        return 0;
    }else{continue;}
    }
}
