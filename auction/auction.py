#!/usr/bin/env python

red = "\033[1;31m"
green = "\033[1;32m"
clr = "\033[0m"

import sys
import re
from pprint import pprint

auction_file = "auction_schedule.glm"

def get_chunk_name(name):
    curr_chunk_name = name.strip().split(" ")[1]
    if '{' in curr_chunk_name:
        curr_chunk_name = curr_chunk_name[:-1]
    return curr_chunk_name


with open(auction_file, "r") as auction_file:
    chunks = {}
    current_chunk = []
    curr_chunk_name = ""

    for line in auction_file.readlines():
        if line.startswith("schedule"):
            if len(current_chunk) != 0:
                chunks[curr_chunk_name] = current_chunk
                current_chunk = []
                curr_chunk_name = get_chunk_name(line)
            else:
                curr_chunk_name = get_chunk_name(line)
        else:
            try:
                data = line.strip().split("//")[0]
                data = [data.split("* ")[1].strip().split("-")[1], 
                        data.split("* ")[4].strip()[:-1]]
                current_chunk.append(data)
            except:
                continue
    chunks[curr_chunk_name] = current_chunk

    pprint(chunks)
