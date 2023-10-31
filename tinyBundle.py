def bundle(inputPath,outputPath): 
    """Bundles files in a certain path.

    Args:
        inputPath (str): Path of the unbundled python files
        outputPath (str): Path to output the bundle
    """
    
    from pathlib import Path; from zipfile import ZipFile
    
    bundlePath = outputPath + "/bundle.py"
    
    with ZipFile(bundlePath, "w") as archive:
        for file_path in Path(inputPath).iterdir():
            archive.write(file_path, arcname=file_path.name)

def compressedBundle(inputPath, outputPath, compressionLevel):
    """Bundles files in a certain path and compresses the output

    Args:
        inputPath (str): Path of the unbundled python files
        outputPath (str): Path to output the bundle
        compressionLevel (int): from 0 to 9 this is the level of 
                                compression (9 being the most compressed)

    Raises:
        ValueError: _description_
    """
    
    from pathlib import Path; from zipfile import ZipFile, ZIP_DEFLATED
    
    if 0 or  9 < compressionLevel:
        raise ValueError("The value for compression level is not valid!")
    
    bundlePath = outputPath + "/bundle.py"
    
    with ZipFile(bundlePath, "w", ZIP_DEFLATED, compresslevel=compressionLevel) as archive:
        for file_path in Path(inputPath).iterdir():
            archive.write(file_path, arcname=file_path.name)
    
    
def run(bundlePath):
    """Runs the bundle with the o2 arg

    Args:
        bundlePath (str): Path to the bundle
    """
    from os import system as cmd 
    cmd("python " + bundlePath + " -o2") # o2 argument added for extra optimization