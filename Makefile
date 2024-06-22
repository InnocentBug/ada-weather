TARGET="/media/ludwig/CIRCUITPY/"

deploy: code.py util.py
	./trunk fmt
	cp code.py $(TARGET)
	cp util.py $(TARGET)


clean:
	rm -f $(TARGET)"*.py"
