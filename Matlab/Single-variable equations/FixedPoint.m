%This program finds the root of a function by converting f(x) to x=g(x)
%using the fixed point method. 

syms x
format longE
iter=input("Enter the number of iterations: ");
x0=input("Enter an initial approximation: ");
f=input("Enter the function:  ");
g=input("Enter the function g: ");
error=input("Enter the maximum absolute error accepted: ");
gx=eval(subs(g,x0));
xi=gx;
fx=eval(subs(f,x0));
e=10;
c=2;

Iter=[0];
Xi=[x0];
Gxi=[gx];
Fxi=[fx];
E(2,1)=[xi-x0];
Xi(2,1)=gx;
Iter(2,1)=1;
Gxi(2,1)=eval(subs(g,xi));
Fxi(2,1)=eval(subs(f,xi));

while e>=error && c<=iter
    gxant=gx;
    gx=eval(subs(g,xi));
    fx=eval(subs(f,xi));
    xi=gx;
    e=abs(gx-gxant);
    c=c+1;
    gxx=eval(subs(g,gx));
    fxx=eval(subs(f,gx));
    Iter(c,1)=c-1;
    Xi(c,1)=xi;
    Gxi(c,1)=[gxx];
    Fxi(c,1)=[fxx];
    E(c,1)=[e];
end

T=table(Iter,Xi,Gxi,Fxi,E);
writetable(T,"Fixed_Point")