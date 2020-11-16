/*###################################
#####################################
############# PLC EXAM 2 ############
###### Created by Anthony Asilo #####
########### November 2020 ###########
#### https://github.com/pillared ####
#####################################
###################################*/

#include <stdio.h> 
#include <stdlib.h> 
#include <ctype.h>
#include <time.h>

#define ARR_SIZE 10
#define loop_SIZE 100000

void declare_staticArr(){
    static int staticArr[ARR_SIZE];
}
void declare_stackArr(){
    int stackArr[ARR_SIZE];
}
void declare_heapArr(){
    int *heapArr = ( int* ) malloc ( ARR_SIZE * sizeof(int) );
    free(heapArr);
}

int main(int argc, char *argv[]){
    int i = 0;
    double time;
    clock_t begin;
    clock_t end;

    begin = clock();
    while(i < loop_SIZE){
        declare_staticArr();
        i++;
    }end = clock();
    time = (double)(end - begin) / CLOCKS_PER_SEC;
    printf("Time for static: %f seconds\n",time);

    i = 0;
    begin = clock();
    while(i < loop_SIZE){
        declare_stackArr();
        i++;
    }end = clock();
    time = (double)(end - begin) / CLOCKS_PER_SEC;
    printf("Time for stack: %f seconds\n",time);

    i = 0;
    begin = clock();
    while(i < loop_SIZE){
        declare_heapArr();
        i++;
    }end = clock();
    time = (double)(end - begin) / CLOCKS_PER_SEC;
    printf("Time for heap: %f seconds\n ",time);
    return 1;
}
