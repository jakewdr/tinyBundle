# What is this?

tinyBundle is a bundler which compresses multiple python files into a single file!

This is similar to [pyz](https://github.com/BTOdell/pyz) and [zipfile](https://docs.python.org/3/library/zipapp.html) but doesn't require its own file type, hence it acts more like JavaScript's [rollup](https://rollupjs.org/).

# How do I build a bundle?

To build a bundle create a .py file and then import tinyBundle:

    import tinyBundle

Then you can build a bundle in the format:

    tinyBundle.bundle(listOfPythonFiles,outputPath,levelOfCompression)

# Upcoming features

 - The ability to bundle other file types (like [webpack](https://webpack.js.org/) can).
 - The ability to bundle dependencies in the bundle.
 - A cli version?
 - Automatic requriments.txt creation

