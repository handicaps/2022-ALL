main:main.o case1.o case2.o case3.o case4.o
	g++ main.o case1.o case2.o case3.o case4.o -o main -lm
main.o:main.c
	g++ -c main.c
case1.o:case1.c case1.h
	g++ -c case1.c
case2.o:case2.c case2.h
	g++ -c case2.c
case3.o:case3.c case3.h
	g++ -c case3.c
case4.o:case4.c case4.h
	g++ -c case4.c
clean:
	rm -rf case1.o case2.o case3.o case4.o main.o main
