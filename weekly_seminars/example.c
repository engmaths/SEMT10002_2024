#include <stdio.h>
#include <math.h>

int main(){
    double M = 1.54;
    double e = 0.3;
    double E;
    double newE;

    E=M;
    int ii;
    for (ii=0; ii<100; ii++) {
        printf("Iteration %d value of E is %lf\n",ii,E);
        newE = M + e*sin(E);
        if (fabs(newE-E)<1e-9) {
            printf("Converged\n");
            break;
        }
        else {
            E = newE;
        }
    }
    return(0);
}