all: main.o rational.o euclid-algorithm.o
	c++ -std=c++11 main.o rational.o euclid-algorithm.o -o test_rational
euclid-algorithm.o: euclid-algorithm.c euclid-algorithm.h
	c++ -std=c++11 -c -g euclid-algorithm.c
rational.o: rational.cpp euclid-algorithm.h
	c++ -std=c++11 -c -g rational.cpp
main.o: main.cpp rational.cpp
	c++ -std=c++11 -c -g main.cpp
clean:
	-rm *.o test_rational
