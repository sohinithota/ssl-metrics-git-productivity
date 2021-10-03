import numpy as np
import argparse

def getArgs():
    argumentParser = argparse.ArgumentParser(prog="SSL Metrics Git Productivity", usage= "Calculates productivity measure of a git project.")
    argumentParser.add_argument('--jsonfile', '-j', required = True, type = open, help = "Commit since day 0")

# Import JSON file using Argparse
# TeamEffort = Last commit day_since_0
# ModuleSize = loc_sum
# Prod = moduleSize / Team Effort
# Store all productivity information in some array or dataframe
