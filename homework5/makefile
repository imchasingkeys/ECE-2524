# Makefile HW

CC	= g++
CFLAGS	= -Wall -g
OBJS	= exprtest.o driver.o parser.tab.o scanner.o


all: exprtest

clean:
	rm -f *.o exprtest

exprtest:  ${OBJS}
	${CC} ${CFLAGS} -o $@ ${OBJS}

exprtest.o: exprtest.cpp 
	${CC} ${CFLAGS} -c $<
driver.o: driver.cpp
	${CC} ${CFLAGS} -c $<
parser.tab.o: parser.tab.cpp parser.tab.hpp
	${CC} ${CFLAGS} -c $<
scanner.o: scanner.cpp scanner.hpp
	${CC} ${CFLAGS} -c $<
	
driver.cpp: scanner.hpp driver.hpp

scanner.hpp: parser.tab.hpp

scanner.cpp: scanner.ll scanner.hpp
	flex -t scanner.ll > $@

parser.tab.hpp: parser.ypp
	bison parser.ypp

parser.tab.cpp: expression.hpp scanner.hpp driver.hpp parser.tab.hpp
	bison parser.ypp


