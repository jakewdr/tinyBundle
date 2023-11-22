import zipfile
import pathlib
import os
import ntpath
            
def bundle(pythonFiles: list, outputPath: str, compressionLevel: int):
    """Creates bundle out of certain python files defined by user

    Args:
        pythonFiles (tuple): Tuple of paths to the specific python files (use forward slashes for paths)
        outputPath (str): Path to output the bundle (use forward slashes)
        compressionLevel (int): The level of compression from 0 (minimum compression) to 9 (max compression)
    """
    
    compressionCheck(compressionLevel)
    
    bundling(list(pythonFiles),str(outputPath),int(compressionLevel))
            
def bundleDirectory(fileDirectory: str, outputPath: str, compressionLevel: int):
    """Creates a bundle from all python files in a directory.

    Args:
        fileDirectory (str): Path to the directory in which the python files are located (use forward slashes)
        outputPath (str): Path to output the bundle (use forward slashes)
        compressionLevel (int): The level of compression from 0 (minimum compression) to 9 (max compression)
    """
    
    compressionCheck(compressionLevel)

    pythonFiles = []

    for entry in pathlib.Path(fileDirectory).iterdir():
        if entry.is_file() and pathlib.Path(entry).suffix == ".py":
                pythonFiles.append(str(entry))
    
    bundling(list(pythonFiles),str(outputPath),int(compressionLevel))
    
    """
    Below functions don't need Doc-strings as they are only interacted with when imported 
    by other more functions, the code for them is pretty self explanatory too!
    """

def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)
    
def compressionCheck(compressionLevel: int):
    if compressionLevel < 0 or 9 < compressionLevel: # Prevents invalid compression levels
        raise ValueError("The value for compression level is not valid!")

def bundling(pythonFiles: list, outputPath: str, compressionLevel: int): # This code is hellish but optimal
    with zipfile.ZipFile(str(outputPath + "bundle.py"), 'w',compression= zipfile.ZIP_DEFLATED,
            compresslevel= int(compressionLevel)) as bundler:
        [bundler.write(file, arcname=str(path_leaf(file))) for file in pythonFiles] # List comprehension

def run(bundlePath):
    """Runs the bundle with the o2 arg

    Args:
        bundlePath (str): Path to the bundle
    """
    os.system("python " + " -O " + bundlePath) # o2 argument added for extra optimization (or something)