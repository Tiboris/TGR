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
	./$(ukol2a) < tests/$(ukol2a).basic.in
	./$(ukol2b) < tests/$(ukol2b).basic.in
	./$(ukol2c) < tests/$(ukol2c).basic.in
	./$(ukol2d) < tests/$(ukol2d).basic.in

# zabalenie ulohy do archivu zip
zip:
	zip $(login) -r ./lib/ ./src/ ./report.pdf ./Makefile
