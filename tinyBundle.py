import zipfile, pathlib, os
            
def bundle(pythonFiles, outputPath, compressionLevel):
    """Creates bundle out of certain python files defined by user

    Args:
        pythonFiles (list): List of paths to the specific python files (use forward slashes)
        outputPath (str): Path to output the bundle (use forward slashes)
        compressionLevel (int): The level of compression from 0 (minimum compression) to 9 (max compression)
    """
    
    compressionCheck(compressionLevel)
    bundling(pythonFiles,outputPath,compressionLevel)
            
def bundleDirectory(fileDirectory, outputPath, compressionLevel):
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
    
    bundling(pythonFiles,outputPath,compressionLevel)
    
def compressionCheck(compressionLevel):
    if compressionLevel < 0 or 9 < compressionLevel: # Prevents invalid compression levels
        raise ValueError("The value for compression level is not valid!")

def bundling(pythonFiles, outputPath, compressionLevel):
    with zipfile.ZipFile(str(outputPath + "bundle.py"), 'w',compression= zipfile.ZIP_DEFLATED,
            compresslevel= int(compressionLevel)) as bundler:
        bundling = [bundler.write(files,arcname=str(files.rsplit('/', 1)[-1])) for files in pythonFiles] # List comprehension for faster bundling
    
def run(bundlePath):
    """Runs the bundle with the o2 arg

    Args:
        bundlePath (str): Path to the bundle
    """
    os.system("python " + bundlePath + " -o2") # o2 argument added for extra optimization (or something)