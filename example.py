def exampleBundleScript ():
    """
    You can use compressedBundle to do this as well 
    although the size decrease doesn't become as apparent 
    until the project is much larger.
    """
    from tinyBundle import bundle 
    bundle("src/","main/")

def exampleBundleAndRunScript():
    from tinyBundle import bundle, run
    bundle("src/", "main/")
    run("out/bundle.py")