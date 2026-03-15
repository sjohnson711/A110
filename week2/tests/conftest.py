import sys
import os

#FIX: refactored sys.path to include parent directory so pytest can locate logic_utils module from the tests/ subfolder using Claude agent mode
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
