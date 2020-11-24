#include <iostream>
#include<math.h>

using namespace std;

double Determinant(double a[3][3])
{
    double i = a[0][0],j = a[0][1],k=a[0][2],det=0;
    det += i*(a[1][1]*a[2][2]-a[1][2]*a[2][1]);
    det += -1*j*(a[1][0]*a[2][2]-a[1][2]*a[2][0]);
    det += k*(a[1][0]*a[2][1]-a[1][1]*a[2][0]);
    return (det);
}


int main(){

int i,n;

cout << "Digite a quantidade de entradas de 'x': ";

cin >> n;

double vetorx[n], vetory[n], vetorx2[n],vetorx3[n],vetorx4[n], vetorxy[n],vetorx2y[n], sumx=0, sumy=0, sumxy=0, sumx2=0,sumx3=0,sumx4=0,sumx2y=0, a, b,c,d, ym, SQReg, SQTot, Rquad;

for(i=0;i<n;i++){

    cout << "Digite X[" << i << "]: ";

    cin >> vetorx[i];

    cout << "Digite y[" << i << "]: ";

    cin >> vetory[i];

}

cout << "\n\n\n                      X  |  Y  |  XY  |  X2 | X3 | X4 | X**2*Y  \n";

for(i=0;i<n;i++){

    vetorxy[i]=vetorx[i]*vetory[i];

    vetorx2[i]=pow(vetorx[i],2);

    vetorx3[i]=pow(vetorx[i],3);

    vetorx4[i]=pow(vetorx[i],4);

    vetorx2y[i]=vetorx2[i]*vetory[i];

    sumx+=vetorx[i];

    sumy+=vetory[i];

    sumxy += vetorxy[i];

    sumx2+=vetorx2[i];

    sumx3+=vetorx3[i];

    sumx4+=vetorx4[i];

    sumx2y+=vetorx2y[i];

    cout << "                      " << vetorx[i] << "  |  " << vetory[i] << "  |  " << vetorxy[i]<< "   |  " << vetorx2[i]<< "   |  " << vetorx3[i]<< "   |  " << vetorx4[i]<< "   |  " << vetorx2y[i] <<  " \n";

    }

cout << "Somatorio:            " << sumx << "  |  " << sumy << "  |  " << sumxy << "   |  " << sumx2 << "   |  " << sumx3 << "   |  " << sumx4 << "   |  " << sumx2y << "  \n\n\n";

double temp = n; 
double D[3][3] = {{temp,sumx,sumx2},{sumx,sumx2,sumx3},{sumx2,sumx3,sumx4}};
double Dx[3][3] ={{sumy,sumxy,sumx2y},{sumx,sumx2,sumx3},{sumx2,sumx3,sumx4}};
double Dy[3][3] ={{temp,sumx,sumx2},{sumy,sumxy,sumx2y},{sumx2,sumx3,sumx4}};
double Dz[3][3] ={{temp,sumx,sumx2},{sumx,sumx2,sumx3},{sumy,sumxy,sumx2y}};

temp = Determinant(D);
if (temp == 0){
  cout << "Sistema não possui solução, ou quantidade de pontos foi insuficiente." << endl;
}
else {
  a = Determinant(Dx)/temp;
  b = Determinant(Dy)/temp;
  c = Determinant(Dz)/temp;
}

ym = sumy/n;

    

for(i=0;i<n;i++){

    SQReg += pow((a*vetorx2[i] + b*vetorx[i] + c - ym),2);

    SQTot += pow((vetory[i] - ym), 2);

}

 

Rquad = SQReg/SQTot;

 

cout << "Ajuste Linear: \n f(x)=" << c << "x^2 + " << b << "x + " << a << "\nR quadrado: " << Rquad;

return 0;

}
