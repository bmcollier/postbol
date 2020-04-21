#include <stdio.h>
#include <stdlib.h>

int main(int argc, char  *argv [ ] )
{
    printf(" \n PostBOL Lexer: %s \t", argv[0]);

    printf("Lexing file %s", argv[1]);
    FILE *fp;
    char buff[1024];

    fp = fopen(argv[1], "r");

    if (!fp) {      /* validate file is open */
        fprintf (stderr, "processText() error: file open failed '%s'.\n", "test");
        exit(EXIT_FAILURE);
    }

    printf("\n");

    while( fgets(buff ,1024,fp) ) {
        printf("%s", buff);
    }

    return 0;

}

