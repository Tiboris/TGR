login = xdudlak
ukol2a = power
ukol2b = reset
ukol2c = weakness
ukol2d = avltree

all:	$(ukol2a) $(ukol2b) $(ukol2c) $(ukol2d)

$(ukol2a):
	echo "python3 ./src/ukol2.py $(ukol2a)" > ./$(ukol2a)
	chmod +x ./$(ukol2a)

$(ukol2b):
	echo "python3 ./src/ukol2.py $(ukol2b)" > ./$(ukol2b)
	chmod +x ./$(ukol2b)

$(ukol2c):
	echo "python3 ./src/ukol2.py $(ukol2c)" > ./$(ukol2c)
	chmod +x ./$(ukol2c)

$(ukol2d):
	echo "python3 ./src/ukol2.py $(ukol2d)" > ./$(ukol2d)
	chmod +x ./$(ukol2d)

clean:
	rm -fv ./$(ukol2a)
	rm -fv ./$(ukol2b)
	rm -fv ./$(ukol2c)
	rm -fv ./$(ukol2d)
	rm -fv ./$(login).zip

run:
	./$(ukol2a) < tests/$(ukol2a)_01.in
	./$(ukol2b) < tests/$(ukol2b)_01.in
	./$(ukol2c) < tests/$(ukol2c)_01.in
	./$(ukol2d) < tests/$(ukol2d)_01.in

test:
	./test.sh $(ukol2a)
	./test.sh $(ukol2b)
	./test.sh $(ukol2c)
	./test.sh $(ukol2d)

# zabalenie ulohy do archivu zip
zip:
	zip $(login) -r ./lib/ ./src/ ./report.pdf ./Makefile ./tests/ ./test.sh
