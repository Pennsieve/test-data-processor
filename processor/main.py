import os
import logging

from config import Config

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
log = logging.getLogger()

def operator(o):
    #print(f"operator() o: {o}")
    if o == '+' or o == 'plus' or o == 'add':
        #print("operator() will perform addition")
        return '+'
    elif o == '-' or o == 'minus' or o == 'subtract':
        #print("operator() will perform subtraction")
        return '-'
    elif o == 'x' or o == '*' or o == 'times' or o == 'multiply':
        #print("operator() will perform multiplication")
        return '*'
    elif o == '÷' or o == '/' or o == 'divide':
        #print("operator() will perform division")
        return '/'
    else:
        #print("operator() will perform addition (fall-through case)")
        return '+'

def expression(a, op, b):
    #print(f"expression() a: {a} op: {op} b: {b}")
    exp =  f"{a} {op} {b}"
    #print(f"expression() exp: {exp}")
    return exp

def process_file(input_file_name, config):
    print(f"process_file() input_file_name: {input_file_name}")
    output_file_name = config.OUTPUT_DIR + '/' + os.path.basename(input_file_name) + '.out'
    with open(input_file_name, 'r') as i, open(output_file_name, 'w') as o:
        while line := i.readline():
            a = line.rstrip()
            b = config.OPERAND
            op = operator(config.OPERATOR)
            exp = expression(a, op, b)
            result = eval(exp)
            print(f"process_file() {exp} = {result}")
            o.write(f"{result}\n")

if __name__ == "__main__":
    print(f"main() os.environ: {os.environ}")
    config = Config()
    print(f"main() config: {config}")

    input_files = [
        f.path
        for f in os.scandir(config.INPUT_DIR)
        if f.is_file()
    ]
    print(f"main() input_files: {input_files}")

    for input_file in input_files:
        print(f"main() input_file: {input_file}")
        process_file(input_file, config)

