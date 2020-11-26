format long
x=input("Enter vector X: ");
y=input("Enter vector Y: ");
n=length(x);
niter=n-1;
sum1=0;
sum2=0;
yy=y(2:n);
h=((x(n)-x(1))/(n-1));
if mod(niter, 3)==0  
  for i=4:3:n-3
    sum1=sum1+y(i);
  endfor
  for i=1:n-1
    if mod(i, 3)!=0
      sum2=sum2+yy(i);
    endif
  endfor
endif
int=((3*h)/8)*((y(1)+y(n)+(2*sum1)+(3*sum2)));
disp("Integration by the Simpson 3/8 method is: ");
disp(int);  
 
  
