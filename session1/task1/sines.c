/* Program that invokes sin() many times, summing the returned values */

#include <math.h>
#include <stdio.h>

int main(void)
{
    double sum = 0.0;

    for(int i = 0; i < 50000000; ++i)
        sum += sin(i);

    printf("Sum = %g\n", sum);
 
    return 0;
}
