login = xdudlak
ukol3a = car
ukol3b = server
ukol3c = race

all:	$(ukol3a) $(ukol3b) $(ukol3c) $(ukol3d)

$(ukol3a):
	echo "python3 ./src/ukol3.py $(ukol3a)" > ./$(ukol3a)
	chmod +x ./$(ukol3a)

$(ukol3b):
	echo "python3 ./src/ukol3.py $(ukol3b)" > ./$(ukol3b)
	chmod +x ./$(ukol3b)

$(ukol3c):
	echo "python3 ./src/ukol3.py $(ukol3c)" > ./$(ukol3c)
	chmod +x ./$(ukol3c)

clean:
	rm -fv ./$(ukol3a)
	rm -fv ./$(ukol3b)
	rm -fv ./$(ukol3c)
	rm -fv ./$(login).zip

touch:
	touch tests/$(ukol3a).basic.in
	touch tests/$(ukol3b).basic.in
	touch tests/$(ukol3c).basic.in

run:
	./$(ukol3a) < tests/$(ukol3a)_basic.in
	./$(ukol3b) < tests/$(ukol3b)_basic.in
	./$(ukol3c) < tests/$(ukol3c)_basic.in


test:
	./test.sh $(ukol2a)
	./test.sh $(ukol2b)
	./test.sh $(ukol2c)
	./test.sh $(ukol2d)

# zabalenie ulohy do archivu zip
zip:
	zip $(login) -r ./lib/ ./src/ ./report.pdf ./Makefile ./tests/
