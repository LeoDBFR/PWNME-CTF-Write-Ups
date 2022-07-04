# PimpMyBicycle

Énoncé : "Your friend just had an idea: allow everyone to create the bike of their dream ! He asks you to verify if his website is secure, since you're the best pentester he knows.

Find a way to access the admin page

note: admin doesn't have access to the internet ! He is behind a very restrictive firewall, and he can only be on his own website

Bruteforce is useless!"

Format du flag : "PWNME{[A-Za-z0-9_]}"

Auteur : "Eteck#3426"

Nombre final de points : 458

Je n'ai pas trop noté ce que j'ai fais pour ce challenge mais dans mes souvenirs j'ai remarqué que l'on pouvait injecter du XSS stocké dans le SVG du bike qu'on renvoyait, j'ai donc fait une payload qui écrivait le document cookie dans un nouveau bike, et ensuite je l'ai envoyé à l'admin, guess le numéro du bike, puis récupéré son cookie d'Admin, et j'ai récuperé le flag.
