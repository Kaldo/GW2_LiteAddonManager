# Check version of module
import main as ModManagerMain

# Check update address
if update_version > ModManagerMain.version:
    download(update_module)
    import module
    reload(ModManagerMain)

ModManagerMain.main()