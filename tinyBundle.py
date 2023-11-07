import zipfile

def bundle(pythonFiles, outputPath, compressionLevel):
    """Creates bundle out of certain python files defined by user

    Args:
        pythonFiles (list): List of paths to the specific python files (use forward slashes)
        outputPath (str): Path to output the bundle (use forward slashes)
        compressionLevel (int): The level of compression from 0 (minimum compression) to 9 (max compression)
    """
    
    if compressionLevel < 0 or 9 < compressionLevel: # Prevents invalid compression levels
        raise ValueError("The value for compression level is not valid!")

    bundlePath = outputPath + "bundle.py" # Creates the path to output the bundle
    
    with zipfile.ZipFile(bundlePath, 'w',compression= zipfile.ZIP_DEFLATED,
                compresslevel= int(compressionLevel)) as bundler:
        for files in pythonFiles: # For all the files in the user input list
            newName = files.rsplit('/', 1) # Splits the string into a list of substrings
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