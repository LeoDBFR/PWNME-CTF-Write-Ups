# Volatile Storage

Énoncé : "You just found a website with a new concept: do not store anything in a database, and do not let user to chose their password.

All stored data are volatile, and will be cleaned everyday.

To register an account, you just have to put a username, and the website will generate you a password according to your username. Once an account is create, the username is locked for you, so you will be the only one to access your data

Find how the website generate passwords, and take over admin account to view all his secrets

Bruteforce is useless!"

Format du flag : "PWNME{[A-Za-z0-9_]}"

Auteur : "Eteck#3426"

Nombre final de points : 50

URL : http://volatile-storage.pwnme.fr/

J'ai crée un compte (baba), et j'ai essayé de décoder le mot de passe, décodé en base64 ça donnait "e56e24cd60b10092", j'ai identifié le hash en tant que "Half MD5", et je l'ai cracké, ce qui m'as donnée "baba".

Le mot de passe d'Admin était donc simplement "admin" encodé en Half MD5 puis en base64.

Une fois connecté on obtient le flag

