import zipfile
import pathlib

def bundle(pythonFiles, outputPath, compressionLevel):
    """Creates bundle out of certain python files defined by user

    Args:
        pythonFiles (list): List of paths to the specific python files (use forward slashes)
        outputPath (str): Path to output the bundle (use forward slashes)
        compressionLevel (int): The level of compression from 0 (minimum compression) to 9 (max compression)
    """
    
    if compressionLevel < 0 or 9 < compressionLevel: # Prevents invalid compression levels
        raise ValueError("The value for compression level is not valid!")

    with zipfile.ZipFile(str(outputPath + "bundle.py"), 'w',compression= zipfile.ZIP_DEFLATED,
                compresslevel= int(compressionLevel)) as bundler:
        for files in pythonFiles: # For all the files in the user input list
            newName = files.rsplit('/', 1) # Splits the string into a list of substrings
            try: 
                bundler.write(files,arcname=str(newName[-1])) # Makes the new file name the final part of the string (removing the previous forward slashes)
            except FileNotFoundError:
                raise FileNotFoundError("The file " + files + " has not been found!")
            
def bundleDirectory(fileDirectory, outputPath, compressionLevel):
    """Creates a bundle from all python files in a directory.

    Args:
        fileDirectory (str): Path to the directory in which the python files are located (use forward slashes)
        outputPath (str): Path to output the bundle (use forward slashes)
        compressionLevel (int): The level of compression from 0 (minimum compression) to 9 (max compression)
    """
    
    if compressionLevel < 0 or 9 < compressionLevel: # Prevents invalid compression levels
        raise ValueError("The value for compression level is not valid!")

    files = pythonFiles = []

    for entry in pathlib.Path(fileDirectory).iterdir():
        if entry.is_file():
            files.append(entry)

    for value in files:
        if pathlib.Path(value).suffix == ".py":
            pythonFiles.append(value)
            files.remove(value)
    
    with zipfile.ZipFile(str(outputPath + "bundle.py"), 'w',compression= zipfile.ZIP_DEFLATED,
                compresslevel= int(compressionLevel)) as bundler:
        for files in pythonFiles: # For all the files in the user input list
            newName = str(files).rsplit('/', 1) # Splits the string into a list of substrings
            try: 
                bundler.write(files,arcname=str(newName[-1])) # Makes the new file name the final part of the string (removing the previous forward slashes)
            except FileNotFoundError:
                raise FileNotFoundError("The file " + files + " has not been found!")

def run(bundlePath):
    """Runs the bundle with the o2 arg

    Args:
        bundlePath (str): Path to the bundle
    """
    from os import system as cmd

    cmd("python " + bundlePath + " -o2") # o2 argument added for extra optimization