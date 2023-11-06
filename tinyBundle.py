def bundle(pythonFiles,outputPath, compressionLevel):
    """Creates bundle out of certain python files defined by user

    Args:
        pythonFiles (list): List of paths to the specific python files (use forward slashes)
        outputPath (str): Path to output the bundle (use forward slashes)
        compressionLevel (int): The level of compression from 0 (minimum) to 9 (max)
    """

    from zipfile import ZipFile, ZIP_DEFLATED

    bundlePath = outputPath + "bundle.py"
    
    with ZipFile(bundlePath, 'w',compression= ZIP_DEFLATED,
                compresslevel= int(compressionLevel)) as bundler:
        for files in pythonFiles:
            newName = files.rsplit('/', 1)
            newName = str(newName[-1])
            bundler.write(files,arcname=newName)

def run(bundlePath):
    """Runs the bundle with the o2 arg

    Args:
        bundlePath (str): Path to the bundle
    """
    from os import system as cmd

    cmd("python " + bundlePath + " -o2")  # o2 argument added for extra optimization