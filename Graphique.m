n = 1:0.01:100;
A = 140 * n.^2;
B = 29 * n.^3 / 140;

plot(n,A, 'r', n,B, 'b')
legend('A','B')
xlabel('n')
ylabel('Nombre d opérations primitives')
