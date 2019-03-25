login = xdudlak
ukol3a = car
ukol3b = server
ukol3c = race

all:	$(ukol3a) $(ukol3b) $(ukol3c) $(ukol3d)

$(ukol3a):
	echo "python3 ./src/ukol2.py $(ukol3a)" > ./$(ukol3a)
	chmod +x ./$(ukol3a)

$(ukol3b):
	echo "python3 ./src/ukol2.py $(ukol3b)" > ./$(ukol3b)
	chmod +x ./$(ukol3b)

$(ukol3c):
	echo "python3 ./src/ukol2.py $(ukol3c)" > ./$(ukol3c)
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
	./$(ukol3a) < tests/$(ukol3a).basic.in
	./$(ukol3b) < tests/$(ukol3b).basic.in
	./$(ukol3c) < tests/$(ukol3c).basic.in

# zabalenie ulohy do archivu zip
zip:
	zip $(login) -r ./lib/ ./src/ ./report.pdf ./Makefile
