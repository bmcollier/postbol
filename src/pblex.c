#include <stdio.h>

int main(int argc, char  *argv [ ] )
{
    printf(" \n PostBOL Lexer: %s \t", argv[0]);

    if( argc == 2 )
    {
        printf("\n Value given by user is: %s \t", argv[1]);
    }
    else if( argc > 2 )
    {
        printf("\n Many values given by users.\n");
    }
    else
    {
        printf(" \n Single value expected.\n");
    }
}