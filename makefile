all: build 

build:
	mkdir -p out
	gcc src/*.c src/*.h main.c -o out/main

lib:
	mkdir -p out
	gcc -fPIC -shared -o out/framebuffer-lib.so src/*.c src/*.h
	cp out/framebuffer-lib.so python/framebuffer/framebuffer/framebuffer-lib.so

python-lib: lib
	pip install --upgrade --no-deps --force-reinstall python/framebuffer

run:
	sudo ./out/main

clear:
	rm -r out/