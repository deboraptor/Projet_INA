## MODULES ##
import pathlib

## MAIN ##
# def main(chemin) : 

#     files = recup_file(chemin)

#     read_file()



#recuperer tous les fichiers du dossier 
def recup_file(chemin): 

    path = pathlib.Path(chemin)
    paths = list(path.glob("**/*.eaf"))
    return paths

