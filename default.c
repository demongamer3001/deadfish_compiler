#include <stdio.h>
#include <stdbool.h>
#include<time.h>

void delay(unsigned int mseconds)
{
    clock_t goal = mseconds + clock();
    while (goal > clock());
}

int main(){
	int c = 0;
	char* script = "SCRIPTHERE"; // the python script puts the actual code here
	bool print_ascii = PRINTASCII; // if the "O" instruction should print out a character or just the number

	while(true){
	
		for(int i = 0; i < LENGTHHERE; i++){
			if(c == -1 || c == 256){
				c = 0;
			}

			if(script[i] == 'INCREMENT'){ // increment
				c++;
			}else if(script[i] == 'DECREMENT'){ // decrement
				c--;
			}else if(script[i] == 'SQUARE'){ // square
				c = c*c;
			}else if(script[i] == 'OUTPUT'){ // output
				if(print_ascii){
					printf("%c", c); // print character
				}else{
					printf("%i\n", c); // print just the number
				}
			}else if(script[i] == ';'){
                return 0;
            }
		}

		delay(1000);

		c = 0;
	}

    return 1;
}