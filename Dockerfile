FROM python:3

RUN git clone https://github.com/AGauchat/Sudoku.git

WORKDIR /Sudoku

RUN pip install -r requerimientos.txt

CMD [ "python3" , "./interfaz.py" ]