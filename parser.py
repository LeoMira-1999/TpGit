#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

def create_parser():
    """
    parsing function to add argument
	"""
    parser = argparse.ArgumentParser()
    parser.add_argument('-i','--inputfile', type=argparse.FileType('r'),
    metavar='FASTA', required=True)
    parser.add_argument('-s','--seq', type=str, required=True, nargs="+")
    return parser

def file_parser(inputfile, sequence):
    """
    file parser to retreive sequence from sequence ID
	"""
    results = {}
    for attribute in sequence:

        for line in inputfile:
            if line.startswith(">"+attribute):
                continue

            if line.startswith(">"):
                break

            if attribute not in results:
                results[attribute] = line.replace("\n","")
            else:
                results[attribute] += line.replace("\n","")
    for attribute, seq in results.items():
        print(attribute+"\n"+seq+"\n")

def main():
    """
    function that initiate launching sequence
	"""
    parser = create_parser()
    args = parser.parse_args()
    args = args.__dict__
    file_parser(args["inputfile"], args["seq"])



if __name__ == "__main__":
    main()
