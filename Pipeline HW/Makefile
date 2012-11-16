#Makefile for Heard it on the Pipeline HW

CC 	= g++
CFLAGS	= -Wall -g

all: generator consumer dispatcher

generator: generator.o 
	${CC} ${CFLAGS} -o $@ generator.o
consumer: consumer.o
	${CC} ${CFLAGS} -o $@ consumer.o
dispatcher: dispatcher.o
	${CC} ${CFLAGS} -o $@ dispatcher.o
dispatcher.o: dispatcher.cpp
	${CC} ${CFLAGS} -c $<
consumer.o: consumer.cpp
	${CC} ${CFLAGS} -c $<
generator.o: generator.cpp
	${CC} ${CFLAGS} -c $<
clean: 
	rm -f *.o consumer generator dispatcher
