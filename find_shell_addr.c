#include <stdio.h>
#include <stdlib.h>

int main() {
    char* shell = getenv("MYSHELL");
    if (shell) {
        printf("Address of MYSHELL: 0x%08x\n", (unsigned int)shell);
        printf("Content: %s\n", shell);
    } else {
        printf("MYSHELL not found\n");
    }
    return 0;
}