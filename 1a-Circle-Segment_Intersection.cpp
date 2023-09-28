//task_2.2.12_Soyfer

#include <iostream>
#include <cmath>
#include <fstream>

#define EPS 1e-15

using namespace std;

int signum (double x)
{
	int sign;
	if (x > EPS) {sign = 1;}
	else if (x < -EPS) {sign = -1;}
	else {sign = 0;}
	return sign;
}

double length (double *x)	//Euclidian norm
{
	double l;
	l = sqrt(x[0]*x[0] + x[1]*x[1]);
	return l;
}

double scalar (double *x, double *y)
{
	double c;
	c = x[0]*y[0] + x[1]*y[1];
	return c;
}

double ht (double *v1, double *v2, double *v3)
{
	double height;
	height = fabs(v1[0]*v2[1] - v1[1]*v2[0]) / length(v3);
	return height;
}

double dist(double *A, double *B, double *M) //a[0]=AB, a[1]=BA, c[0]=AM, c[1]=BM;
{

	double a[2][2] = {{B[0] - A[0], B[1] - A[1]}, {A[0] - B[0], A[1] - B[1]}};
	double c[2][2] = {{M[0] - A[0], M[1] - A[1]}, {M[0] - B[0], M[1] - B[1]}};

	int sum = 0;
	double d, scal;

	for (int i = 0; i < 2; i++)
	{
		scal = scalar(a[i], c[i]);
		sum += signum(scal);
		if (scal <= EPS) {d = length(c[i]);}
	}

	if (sum == 2) {d = ht(c[0], c[1], a[0]);}

	return d;
}

int pts_intersect(double *M, double r, double *A, double *B) //M - center, r - radius, A,B - ends of segment;
{
	double MA[2] = {A[0] - M[0], A[1] - M[1]};
	double MB[2] = {B[0] - M[0], B[1] - M[1]};
	double AB[2] = {B[0] - A[0], B[1] - A[1]};

	int ans; double h, a[2] = {length(MA), length(MB)};

	if (length(AB) <= EPS) {h = length(MA);} //segment with very close ends is considered as one point

	else {h = dist(A, B, M);}

	if ((h > r)||((a[0] < r)&&(a[1] < r))) {ans = 0;}

	if (fabs(h - r) <= EPS) {ans = 1;} //h == r

	if (h < r)
	{
		ans = 0;
		for (int i = 0; i < 2; i++)
		{
			if (a[i] >= r) {ans++;}
		}
	}

	return ans;
}


int main()
{
	ifstream f_in; string s;

	cout<<"File: "; cin>>s;

	f_in.open(s);

	if (f_in.is_open())
	{
		int count = 0; //counter for checking amount of data
		int n = 7; //correct amount of data

		double tmp, radius, data[n], center[2], left[2], right[2];

		while ((f_in >> tmp)&&(count < 7))
		{
			data[count] = tmp;
			count++;
		}

		if (count < 7) {cout << "\nError: empty file or incorrect data" << endl;}

		else
		{
			center[0] = data[0]; center[1] = data[1];
			radius = data[2];
			left[0] = data[3]; left[1] = data[4];
			right[0] = data[5]; right[1] = data[6];
			/*cout<<"\ncenter: "<<center[0]<<" "<<center[1]<<endl;
			cout<<"\nradius: "<<radius<<endl;
			cout<<"\nleft: "<<left[0]<<" "<<left[1]<<endl;
			cout<<"\nright: "<<right[0]<<" "<<right[1]<<endl;*/
			cout<<"\nPoints of intersection:\t"<<pts_intersect(center, radius, left, right)<<endl;
		}
	}

	else
	{
		cout<<"\nError: cannot open file\n"<<endl;
	}

	f_in.close();

	return 0;
}




