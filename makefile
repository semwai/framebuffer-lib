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

# make transparent cursor and close tty1 input & output, now use tty2 (ctrl+alt+f2)
# do it inside virtual machine, not ssh
kill-tty1:
	echo -n -e '\e[?1;14;0c'
	sudo systemctl stop getty@tty1.service

run:
	sudo ./out/main

clear:
	rm -r out/