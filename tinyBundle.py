def bundle(inputPath, outputPath):
    """Bundles files in a certain path.

    Args:
        inputPath (str): Path of the unbundled python files
        outputPath (str): Path to output the bundle
    """

    from pathlib import Path
    from zipfile import ZipFile
    from shutil import copy

    bundlePath = outputPath + "bundle.py"
    files = []
    pythonFiles = []

    d = Path(inputPath)

    for entry in d.iterdir():
        if entry.is_file():
            files.append(entry)

    for value in files:
        if Path(value).suffix == ".py":
            pythonFiles.append(value)
            files.remove(value)

    with ZipFile(bundlePath, "w") as archive:
        for pythonFile in pythonFiles:
            archive.write(pythonFile)

    if 1 <= len(files):
        for remainingFile in files:
            copy(remainingFile, outputPath)


def compressedBundle(inputPath, outputPath, compressionLevel):
    """Bundles files in a certain path and compresses the output

    Args:
        inputPath (str): Path of the unbundled python files
        outputPath (str): Path to output the bundle
        compressionLevel (int): from 0 to 9, this is the level of
                                compression (9 being the most compressed)

    Raises:
        ValueError: _description_
    """

    from pathlib import Path
    from zipfile import ZipFile, ZIP_DEFLATED
    from shutil import copy

    if 0 or 9 < compressionLevel:  # valid inputs are between 0 and 9
        raise ValueError("The value for compression level is not valid!")

    bundlePath = outputPath + "bundle.py"
    files = []
    pythonFiles = []

    d = Path(inputPath)

    for entry in d.iterdir():
        if entry.is_file():
            files.append(entry)

    for value in files:
        if Path(value).suffix == ".py":
            pythonFiles.append(value)
            files.remove(value)

    with ZipFile(
        bundlePath, "w", ZIP_DEFLATED, compresslevel=compressionLevel
    ) as archive:
        for pythonFile in pythonFiles:
            archive.write(pythonFile)

    if 1 <= len(files):
        for remainingFile in files:
            copy(remainingFile, outputPath)
            
def specificFileBundle(pythonFiles,outputPath):
    """Creates bundle out of certain python files defined by user

    Args:
        pythonFiles (list): Contains the file path to all the python files.
        outputPath (str): Path to output the bundle
    """

    from zipfile import ZipFile

    bundlePath = outputPath + "bundle.py"
    
    with ZipFile(bundlePath, "w") as archive:
        for pythonFile in pythonFiles:
            archive.write(pythonFile)
        


def run(bundlePath):
    """Runs the bundle with the o2 arg

    Args:
        bundlePath (str): Path to the bundle
    """
    from os import system as cmd

    cmd("python " + bundlePath + " -o2")  # o2 argument added for extra optimization