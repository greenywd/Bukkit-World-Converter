#!/usr/bin/env python

import os
from distutils.dir_util import copy_tree
import shutil
import sys
import argparse

class WorldConverterError(Exception):
    pass

class NetherNotFound(WorldConverterError):
    def __init__(self, message):
        self.message = message

class EndNotFound(WorldConverterError):
    def __init__(self, message):
        self.message = message

class WorldConverter:
    def checkWorld(self, path: str, world_name: str = "world"):
        # Add a trailing / if one isn't given
        if (path[-1:] != '/'):
            path += '/'

        if (os.path.exists(path)):
            # Check whether _nether and _the_end exists.
            if (not os.path.exists(path + world_name + '_nether')):
                raise NetherNotFound("Nether not found in %s. Make sure that %s_nether exists or try specifying the world name with --world-name." % (path, world_name))

            if (not os.path.exists(path + world_name + '_the_end')):
                raise EndNotFound("The End not found in %s. Make sure that %s_the_end exists or try specifying the world name with --world-name." % (path, world_name))

            print("Nether and The End worlds found. Ready to convert!")

        else:
            raise FileNotFoundError("Directory '%s' does not exist." % (path)) 

    def convertWorld(self, path: str, world_name: str = "world"):
        try:
            self.checkWorld(path, world_name)
        except Exception as error:
            print(error)
            sys.exit(1)

        output_path = 'Converted/%s' % (world_name)
        
        if not os.path.exists(output_path):
            # Overworld
            os.makedirs(output_path, exist_ok=True)
            # Nether
            os.makedirs(output_path + '/DIM-1', exist_ok=True)
            # The End
            os.makedirs(output_path + '/DIM1', exist_ok=True)

        # Copy Worlds to Temp/
        print("Copying Worlds...")
        copy_tree(path + world_name, 'Temp/Overworld/')
        copy_tree(path + world_name + '_nether', 'Temp/Nether/')
        copy_tree(path + world_name + '_the_end', 'Temp/TheEnd/')

        print("-- Copying Overworld...")
        copy_tree('Temp/Overworld/', output_path)

        print("-- Copying Nether...")
        copy_tree('Temp/Nether/DIM-1', output_path + '/DIM-1')
        
        print("-- Copying The End...")
        copy_tree('Temp/TheEnd/DIM1', output_path + '/DIM1')

        print("Removing Temp files...")
        shutil.rmtree('Temp')

        print("Done!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='Bukkit World Converter', description='Convert Bukkit Server worlds to Singleplayer worlds.', epilog='If no arguments are given, nothing will happen.')
    parser.add_argument('--world-dir', type=str, required=False, metavar='<world dir>', help='The directory that the Bukkit world is stored.')
    parser.add_argument('--world-name', type=str, required=False, metavar='<world>', help='The name of the world.')
    parser.add_argument('--check-world', type=str, required=False, metavar='<world dir>', help='Check whether all worlds exist to convert.')
    args = parser.parse_args()

    converter = WorldConverter()

    if args.world_dir:
        try:
            converter.convertWorld(args.world_dir)
        except NetherNotFound as error:
            print(error)
        except EndNotFound as error:
            print(error)

        sys.exit(0)

    if args.check_world:
        try:
            converter.checkWorld(args.check_world)
        except Exception as e:
            print(e)
            sys.exit(1)
        
        sys.exit(0)