import os
import logging

from config import Config

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
log = logging.getLogger()

def operator(o):
    if o == '+' or o == 'plus' or o == 'add':
        return '+'
    elif o == '-' or o == 'minus' or o == 'subtract':
        return '-'
    elif o == 'x' or o == '*' or o == 'times' or o == 'multiply':
        return '*'
    elif o == '÷' or o == '/' or o == 'divide':
        return '/'
    else:
        return '+'

def expression(a, op, b):
    return f"{a} {op} {b}"

def process_file(input_file_name, config):
    output_file_name = config.OUTPUT_DIR + '/' + os.path.basename(input_file_name) + '.out'
    with open(input_file_name, 'r') as i, open(output_file_name, 'w') as o:
        while line := i.readline():
            a = line.rstrip()
            b = config.OPERAND
            op = operator(config.OPERATOR)
            result = eval(expression(a, op, b))
            o.write(f"{result}\n")

if __name__ == "__main__":
    config = Config()

    input_files = [
        f.path
        for f in os.scandir(config.INPUT_DIR)
        if f.is_file()
    ]

    for input_file in input_files:
        log.info(f"input_file: {input_file}")
        process_file(input_file, config)

