# Bukkit-World-Converter
Converts Multiplayer Bukkit worlds to Singleplayer worlds.

Bukkit (and all forks of Bukkit that I know of) split up the Nether and The End into their own separate worlds. This means you can't copy + paste the world folder into saves folder and begin playing it in Singleplayer properly. The overworld will work, but the Nether and The End dimensions will be generated from scratch. While the process of converting a Bukkit world to Singleplayer is very simple (changing its file tree), but I decided to make a script to make this process a bit faster.

## Usage
```
usage: Bukkit World Converter [-h] [--world-dir <world dir>] [--world-name <world>] [--check-world <world dir>]

Convert Bukkit Server worlds to Singleplayer worlds.

optional arguments:
  -h, --help            show this help message and exit
  --world-dir <world dir>
                        The directory that the Bukkit world is stored.
  --world-name <world>  The name of the world.
  --check-world <world dir>
                        Check whether all worlds exist to convert.

If no arguments are given, nothing will happen.
```

