#include <stdio.h>

int times_row(double *data, int rows, int columns){
	int i, j;
	for(i=0; i<rows; i++){
		for(j=0; j<columns; j++){
			data[i*columns + j] *= i;
		}
	}
	
	return 0;
}
