main:main.o find.o
	gcc main.o find.o -o main -lm
main.o:main.c
	gcc -c main.c
find.o:find.c find.h
	gcc -c find.c
clean:
	rm -rf find.o main.o main
