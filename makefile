all: build run

build:
	gcc src/*.c src/*.h -o out/main

run:
	./out/main

clear:
	rm *.out *.gch out/*