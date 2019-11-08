#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re

def extract_url(multiline_string):
    # Search for domain pattern
    p = re.compile('(([A-Za-z0-9-]{1,63}\.)+[a-zA-Z]{2,6})')
    return re.findall(p, multiline_string)

def main():
    print("Enter as many lines of text as you want.")
    print("When you're done, enter a semicolon on a line by itself.")

    # Multiple input line
    vbuffer = []
    while True:
        print("> ", end="")
        line = input()
        if line == ";":
            break
        vbuffer.append(line)
    multiline_string = "\n".join(vbuffer)

    extracted_data = extract_url(multiline_string)

    # Print result
    print("Result:")
    print()
    for xdata in extracted_data:
        print(xdata[0])

if __name__ == '__main__':
    main()
