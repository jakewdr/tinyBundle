import tinyBundle
from timeit import default_timer as timer

"""
This is the boilerplate for a bundle script, this uses the tinyBundle module to bundle all files
specified in the "files" list

Use forward slashes for paths!

Alternative options:

tinyBundle.bundleDirectory("src/","out/",0)
tinyBundle.run("out/bundle.py")
"""

files = ["src/__main__.py"] # Add other files here (can also be a list but a tuple if preferred)

start = timer()
tinyBundle.bundle(files,"out/",0) # out/ is the default output location and 0 is the default compression level
end = timer()
print("Bundle time = " + str(end - start) + " seconds") # time in seconds