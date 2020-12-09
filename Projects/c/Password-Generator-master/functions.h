//simply add or remove characters here
const char alphabet[]="1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
char buffer[128];
char passworddescription[128];
int letternumber;

void remove_newline(char *something){
    for(int c=0;c<strlen(something);c++){//for removing newline character
        if(something[c]=='\n'){
            something[c]='\0';
        }
    }
}
void getpassworddescription(char *description){
    printf("Enter password description:");
    fgets(description,128,stdin);
    remove_newline(description);
}
int getletternumber(){
    int returnvalue;
    printf("Enter the amount of letters(just pressing enter will bug):");
    fgets(buffer,128,stdin);
    int bufferlength=strlen(buffer)-1;//-1 for \0 character
    remove_newline(buffer);
    for(int c=0;c<bufferlength;c++){
        if((isdigit(buffer[c]))&&(buffer[c]!='\0')){
            continue;
        }else{
            printf("\aError, non-digit found.");
            getchar();
            return -1;
        }
    }
    sscanf(buffer, " %d", &returnvalue);
    return returnvalue;
}
void generatepassword(int letternumber,char *password,int alphabetlength){
    int r;
    srand(time(0));
    for(int c=0;c<letternumber;c++){
        r=rand()%(alphabetlength-2);//-1 for \0 character
        password[c]=alphabet[r];
    }
    remove_newline(password);
}
void printtime(FILE *fp){
    char te[64];
    time_t t = time(NULL);
    struct tm *tm = localtime(&t);
    strftime(te, sizeof(te), "%c", tm);
    fprintf(fp,"%s",te);
}
void printfile(FILE *fp, char *description, char *password){
    fseek(fp,0,SEEK_END);
    size_t length=ftell(fp);
    if(length!=0){//prints info to the next line if text is present
        fprintf(fp,"\n");
    }
    printtime(fp);
    fprintf(fp,"\n%s:%s",description,password);
    printf("Password successfully saved in Passwords.txt");
}
int quitmessage(){
    printf("\nType q to quit, enter to continue(any other letter will bug):");
    fgets(buffer,2,stdin);
    int input=buffer[0];
    return input;
}
