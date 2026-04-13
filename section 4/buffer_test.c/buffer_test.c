#include <stdio.h>
#include <string.h>

int main() {
    char buffer[16];   // small buffer
    char input[100];   // large input

    printf("Enter text: ");
    scanf("%s", input);   // taking user input

    strcpy(buffer, input);  // unsafe copy (can overflow)

    printf("Buffer content: %s\n", buffer);

    return 0;
}

/*
==================== ANSWERS ====================

1. What happens with long input?
When the user enters input longer than 16 characters, a buffer overflow occurs.
This overwrites nearby memory and may cause unexpected behavior or program crash.

2. Why is this dangerous?
It is dangerous because:
- It can crash the program
- It can corrupt memory
- Attackers can exploit this vulnerability to execute malicious code

3. How would you fix it?
To fix this issue, use safe functions such as:
- fgets(buffer, sizeof(buffer), stdin);
- strncpy(buffer, input, sizeof(buffer)-1);

These functions limit input size and prevent overflow.

================================================
*/
