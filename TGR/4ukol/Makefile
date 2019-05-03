login = xdudlak
ukol4a = evacuation
ukol4b = groups
ukol4c = parking

all:	$(ukol4a) $(ukol4b) $(ukol4c) $(ukol4d)

$(ukol4a):
	echo "python3 ./src/ukol4.py $(ukol4a)" > ./$(ukol4a)
	chmod +x ./$(ukol4a)

$(ukol4b):
	echo "python3 ./src/ukol4.py $(ukol4b)" > ./$(ukol4b)
	chmod +x ./$(ukol4b)

$(ukol4c):
	echo "python3 ./src/ukol4.py $(ukol4c)" > ./$(ukol4c)
	chmod +x ./$(ukol4c)

clean:
	rm -fv ./$(ukol4a)
	rm -fv ./$(ukol4b)
	rm -fv ./$(ukol4c)
	rm -fv ./$(login).zip

touch:
	touch tests/$(ukol4a)_basic.in
	touch tests/$(ukol4b)_basic.in
	touch tests/$(ukol4c)_basic.in

run:
	./$(ukol4a) < tests/$(ukol4a)_basic.in
	./$(ukol4b) < tests/$(ukol4b)_basic.in
	./$(ukol4c) < tests/$(ukol4c)_basic.in


test:
	./test.sh $(ukol4a)
	./test.sh $(ukol4b)
	./test.sh $(ukol4c)

# zabalenie ulohy do archivu zip
zip:
	zip $(login) -r ./lib/ ./src/ ./report.pdf ./Makefile ./test.sh ./tests/
