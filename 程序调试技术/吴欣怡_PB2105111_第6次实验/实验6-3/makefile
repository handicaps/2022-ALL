main:main.o bits.o
	g++ main.o bits.o -o main -lm
main.o:main.c
	g++ -c main.c
bits.o:bits.c bits.h
	g++ -c bits.c 
clean:
	rm -rf bits.o main.o main
