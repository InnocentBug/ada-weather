TARGET="/media/ludwig/CIRCUITPY/"

deploy: code.py util.py
	cp code.py $(TARGET)
	cp util.py $(TARGET)

code.py:
	trunk fmt code.py

util.py:
	trunk fmt util.py

clean:
	rm -f $(TARGET)"*.py"
