#include "pblex.h"

int main(int argc, char  *argv [ ] )
{
    printf(" \n PostBOL Lexer: %s \t", argv[0]);

    printf("Lexing file %s", argv[1]);
    FILE *fp;
    char buff[1024];

    fp = fopen(argv[1], "r");

    if (!fp) {      /* validate file is open */
        fprintf (stderr, "processText() error: file open failed '%s'.\n", argv[1]);
        exit(EXIT_FAILURE);
    }

    printf("\n");
    char *tokens[20];
    while( fgets(buff ,1024,fp) ) {
        *tokens = tokeniseInput(buff);
        for (int i=0; i<20; i++ ) {
            if (tokens[i] != NULL) {
                printf("%s", tokens[i]);
            }
        }
        printf("%s", tokens[0]);
    }
    return 0;
}

char* tokeniseInput(char programLine[]) {
    int i = 0;
    char *p = strtok (programLine, " ");
    char *tokens[20];

    while (p != NULL) {
        tokens[i++] = p;
        p = strtok (NULL, " ");
    }

    return *tokens;
}