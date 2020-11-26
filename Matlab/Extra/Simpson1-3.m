format long
x=input("Enter vector X: ");
y=input("Enter vector Y: ");
n=length(x);
sum1=0;
sum2=0;
h=((x(n)-x(1))/(n-1));
for i=2:n-1
  if mod(i, 2)==0
    sum2=sum2+y(i)
  else
    sum1=sum1+y(i)
  endif
endfor
sumt=y(1)+(4*sum1)+(2*sum2)+y(n);
sumt=(y(1)+(4*(sum2))+(2*(sum1))+y(n));
int=(h/3)*sumt;
disp("Integration by the Simpson 1/3 method is: ");
disp(int);  



