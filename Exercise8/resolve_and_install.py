def resolve_and_install(package):
    dependencies = package.dependencies

    if package.is_installed:
        return
    
    # If no dependencies
    if dependencies == ():
        if not package.is_installed:
            install(package)
        return 
        
    
    # Need to install dependencies.
    for dep in dependencies:
        if not dep.is_installed:
            resolve_and_install(dep)

