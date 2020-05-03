#!/usr/bin/env python

import os
import argparse

def convertWorld(path: str):
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='Bukkit World Converter', description='Convert Bukkit Server worlds to Singleplayer worlds.', epilog='If no arguments are given, nothing will happen.')
    parser.add_argument('--world-dir', type=str, required=True, metavar='<world dir>')
    args = parser.parse_args()