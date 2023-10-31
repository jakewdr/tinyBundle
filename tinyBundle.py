def bundle(inputPath,outputPath):
    
    from pathlib import Path; from zipfile import ZipFile
    
    bundlePath = outputPath + "/bundle.py"
    
    with ZipFile(bundlePath, "w") as archive:
        for file_path in Path(inputPath).iterdir():
            archive.write(file_path, arcname=file_path.name)

def compressedBundle(inputPath, outputPath, compressionLevel):
    
    from pathlib import Path; from zipfile import ZipFile, ZIP_DEFLATED
    
    if 0 or  9 < compressionLevel:
        raise ValueError("The value for compression level is not valid!")
    
    bundlePath = outputPath + "/bundle.py"
    
    with ZipFile(bundlePath, "w", ZIP_DEFLATED, compresslevel=compressionLevel) as archive:
        for file_path in Path(inputPath).iterdir():
            archive.write(file_path, arcname=file_path.name)
    
    
def run(bundlePath):
    from os import system as cmd 
    cmd("python " + bundlePath + " -o2") # o2 argument added for extra optimization