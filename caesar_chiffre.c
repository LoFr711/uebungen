#include <stdio.h>
#include <stdlib.h>

// Verschiebt einen ASCII Buchstaben um key Stellen
int asciiOperation(char letter, int key) {
    if (letter >= 'A' && letter <= 'Z') {
        letter += key;
        if (letter > 'Z') {
            letter -= 26;
        } else if (letter < 'A') {
            letter += 26;
        }
    }
    return letter;
}

// Verschlüsselt einen in ASCII kompatiblen Großbuchstaben gegebenen Text im Caesar Schiffre um key Stellen
char *encipher(char string[], int key) {
    int i = 0;
    while(string[i] != '\0') {
        string[i] = (char) asciiOperation(string[i], key);
        i++;
    }
    char *result = string;
    return result;
}

// Entschlüsselt einen in ASCII kompatiblen Großbuchstaben gegebenen Text im Caesar Schiffre um key Stellen
char *decipher(char string[], int key) {
    int i = 0;
    while(string[i] != '\0') {
        string[i] = (char) asciiOperation(string[i], key * -1);
        i++;
    }
    char *result = string;
    return result;
}

int main() {
    char string[] = "YLHOH NDPHQ DOOPDHKOLFK CX GHU XHEHUCHXJXQJ HLQHQ JURVVHQ IHKOHU JHPDFKW CX KDEHQ DOV VLH YRQ GHQ EDHXPHQ KHUXQWHUJHNRPPHQ ZDUHQ XQG HLQLJH VDJWHQ VFKRQ GLH EDHXPH VHLHQ HLQ KROCZHJ JHZHVHQ GLH RCHDQH KDHWWH PDQ QLHPDOV YHUODVVHQ GXHUIHQ";
    char *ptr = decipher(string, 3);
    printf("Entschlüsselter Text:\n");
    printf("%s\n", ptr);
    return 1;
}