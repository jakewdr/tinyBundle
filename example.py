def exampleBundleScript ():
    """
    This bundles the files in 'src/' and outputs it in 'out/'
    
    You can use compressedBundle to do this as well 
    although the size decrease doesn't become as apparent 
    until the project is much larger.
    """
    from tinyBundle import bundle 
    bundle("src/","out/") # You should a / to the end of the bundle command!

def exampleBundleAndRunScript():
    """
    This bundles the files in 'src/' and outputs it in 'out/' 
    and then runs the file with the -o2 optimization argument
    
    (again you can use compressed bundle)
    """
    from tinyBundle import bundle, run
    bundle("src/", "out/") # You should a / to the end of the bundle command!
    run("out/bundle.py")
