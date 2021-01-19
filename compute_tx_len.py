#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 19 09:14:12 2021

@author: Marine Girardey
"""

#Imports
import re

#Dictionnary initialisation
transcript_start = dict()
transcript_end = dict()

def get_tx_genomic_length(input_file=None):
    """
    Parameters
    ----------
    input_file : GTF file

    Returns
    -------
    transcript length.
    """

    file_handler = open(input_file)
    for line in file_handler:
        token = line.split("\t")
        start = int(token[3]) # start position of the exon
        end = int(token[4]) # end position of the exon

        # Get transcript ID
        tx_id = re.search('transcript_id "([^"]+)"', token[8]).group(1)

        # Insert each transcript ID in the two dictionaries
        if tx_id not in transcript_start:
            transcript_start[tx_id] = start
            transcript_end[tx_id] = end

        # If start or end position not in dictionaries, add it
        else:
            if start < transcript_start[tx_id]:
                transcript_start[tx_id] = start
                if end > transcript_end[tx_id]:
                    transcript_end[tx_id] = end

    # Print each transcript with their length
    for tx_id in transcript_start:
        print(tx_id + "\t" + str(
            transcript_end[tx_id] - transcript_start[tx_id] + 1))

# Only run the 'get_tx_genomic_length' function
if __name__ == '__main__':
    get_tx_genomic_length(input_file='../pymetacline/data/gtf/simple.gtf')
