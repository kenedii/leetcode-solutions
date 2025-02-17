// Beats 100% Runtime, Beats 92.99% Memory
#include <math.h>
#include <string.h>

char* intToRoman(int num) {
    static char new_s[16] = {0};
    memset(new_s, 0, sizeof(new_s)); // Clear the array at start of each call
    int lennum = ceil(log10(num + 1)); // Computes the number of digits in the number
    int index = 0;            // Keep track of current char index in string

    for (int i = 0; i < lennum; i++) { // Loops from 0 to lennum
        int current_digit =
            (num % (int)pow(10, lennum - i) -
             num % (int)pow(10, lennum - i - 1)) /
            (int)pow(10, lennum - i - 1); // Computes the digit at position i of the integer

        if (lennum - i ==4) { // Thousands (e.g. lennum=4, on iter 0 lennum-0 == 4)
            // Loop through the number of Ms (represented by current_digit)
            for (int j = 0; j < current_digit; j++) {
                new_s[index] = 'M';
                index++;
            }
        } else if (lennum - i == 3) { // Hundreds
            if (current_digit ==
                4) { // Handle current_digit=4 and current_digit=9 separately
                new_s[index] = 'C';
                index++;
                new_s[index] = 'D';
                index++;

            } else if (current_digit == 9) {

                new_s[index] = 'C';
                index++;
                new_s[index] = 'M';
                index++;

            } else {
                if (current_digit >= 5) { // If digit is >=5, 

                    new_s[index] = 'D'; // We append 'D' to the string
                    index++;

                    for (int j = 0; j < current_digit - 5; j++) { // plus current_digit-5 'C's

                        new_s[index] = 'C';
                        index++;
                    }
                } else {
                    for (int j = 0; j < current_digit; j++) {

                        new_s[index] = 'C';
                        index++;
                    }
                }
            }
        } else if (lennum - i == 2) { // Tens
            if (current_digit == 4) {

                new_s[index] = 'X';
                index++;
                new_s[index] = 'L';
                index++;

            } else if (current_digit == 9) {

                new_s[index] = 'X';
                index++;
                new_s[index] = 'C';
                index++;

            } else {
                if (current_digit >= 5) {

                    new_s[index] = 'L';
                    index++;

                    for (int j = 0; j < current_digit - 5; j++) {

                        new_s[index] = 'X';
                        index++;
                    }
                } else {
                    for (int j = 0; j < current_digit; j++) {

                        new_s[index] = 'X';
                        index++;
                    }
                }
            }
        } else if (lennum - i == 1) { // Ones
            if (current_digit == 4) {

                new_s[index] = 'I';
                index++;
                new_s[index] = 'V';
                index++;

            } else if (current_digit == 9) {

                new_s[index] = 'I';
                index++;
                new_s[index] = 'X';
                index++;

            } else {
                if (current_digit >= 5) {

                    new_s[index] = 'V';
                    index++;

                    for (int j = 0; j < current_digit - 5; j++) {

                        new_s[index] = 'I';
                        index++;
                    }
                } else {
                    for (int j = 0; j < current_digit; j++) {

                        new_s[index] = 'I';
                        index++;
                    }
                }
            }
        }
    }

    return new_s;
}
