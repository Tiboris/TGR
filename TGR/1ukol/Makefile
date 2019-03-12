login = xdudlak
ukol1a = information
ukol1b = fusion
ukol1c = chemistry

all:	$(ukol1a) $(ukol1b) $(ukol1c)
# information
$(ukol1a):
	echo "python3 ./src/ukol1.py $(ukol1a)" > ./$(ukol1a)
	chmod +x ./$(ukol1a)
# fusion
$(ukol1b):
	echo "python3 ./src/ukol1.py $(ukol1b)" > ./$(ukol1b)
	chmod +x ./$(ukol1b)
# chemistry
$(ukol1c):
	echo "python3 ./src/ukol1.py $(ukol1c)" > ./$(ukol1c)
	chmod +x ./$(ukol1c)

clean:
	rm -fv ./$(ukol1a)
	rm -fv ./$(ukol1b)
	rm -fv ./$(ukol1c)
	rm -fv ./$(login).zip

test:
	./information < tests/test-information-basic.in | diff -u tests/test-information-basic.out -
	./fusion < tests/test-fusion-basic.in | diff -u tests/test-fusion-basic.out
	./chemistry < tests/test-chemistry-basic.in | diff -u tests/test-chemistry-basic.out

# zabalenie ulohy do archivu zip
zip:
	zip $(login) -r ./lib/ ./src/ ./report.pdf ./Makefile
