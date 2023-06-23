# Démo de l'exercice 2d de la semaine 7

# Fonction de hachage avec résolution de collisions par double hachage
# Le hash primaire est h(x) = x mod N où N est la taille de la table
# Le hash secondaire est h'(x) = 7 - x mod 7
# Le hash total est H(x) = (h(x) + i * h'(x)) mod N où i est le nombre de collisions
class double_hashing_demo:
    def __init__(self, table_size):
        self.table_size = table_size

    def primary_hash(self, n):
        resultat = n % self.table_size
        return resultat

    def secondary_hash(self, n):
        resultat = 7 - n % 7
        return resultat

    def hash(self, n, i):
        primary = self.primary_hash(n)
        secondary = self.secondary_hash(n)
        if i == 0:
            print(f"Hash primaire pour la clé {n} = {primary}")
            print(f"Hash secondaire pour la clé {n} = {secondary}")
        resultat = (primary + i * secondary) % self.table_size
        print(f"Hash total obtenu avec la clé {n}: ({primary} + {i} * {secondary}) % {self.table_size} = {resultat}")
        return resultat

class hash_entry:
    def __init__(self, key, status):
        self.key = key
        self.status = status

    def __repr__(self):
        if self.status == "F":
            return "Libre"
        elif self.status == "O":
            return f"Occupée, clé = {self.key}"
        else:
            raise "État non reconnu pour hash_entry"


# Table de hachage dont on peut spécifier la taille et le type de hachage
class hash_table:
    def __init__(self, table_size, hash_engine):
        self.table_size = table_size
        self.hash_engine = hash_engine(self.table_size)
        self.table = [hash_entry(0, "F") for i in range(self.table_size)]

    def insert_key(self, key):
        print(f"Insertion de la clé {key}:")
        tentative = 0
        hash = self.hash_engine.hash(key, tentative)
        while self.table[hash].status == "O" and tentative < self.table_size :
            tentative += 1
            hash = self.hash_engine.hash(key, tentative)
        if tentative == self.table_size:
            print(f"Insertion de la clé: {key} impossible!  Table trop occupée!")
            return

        self.table[hash].key = key
        self.table[hash].status = "O"

    def display_table(self, message=""):
        print(f"État de la table de dispersion {message}")
        for i in range(self.table_size):
            print(f"Cellule {i} --> {self.table[i]}")
        print("\n\n")

if __name__ == '__main__':

    ht = hash_table(10, double_hashing_demo)
    ht.display_table()
    keys = [4371, 1323, 6173, 4199, 4344, 9679, 1989]
    for key in keys:

        input(f"Veuillez appuyer sur une touche pour insérer la clé suivante: {key}")
        print("")
        ht.insert_key(key)
        ht.display_table(f"après insertion de la clé {key}")




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
