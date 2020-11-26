format long
x=input("Enter vector X: ");
y=input("Enter vector Y: ");
n=length(x);
sum=0;
h=x(2)-x(1);
for i=2:n-1
  sum=sum+y(i);
endfor
int=(h/2)*(y(1)+2*sum+y(n));
disp("Integration by the trapeze method is: ");
disp(int);