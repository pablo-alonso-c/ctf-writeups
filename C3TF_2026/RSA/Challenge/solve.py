from Crypto.Util.number import long_to_bytes

p = 266389670685446299301982514011839137549
q = 303154033304397379996687987857088285529
e = 65537
c = 53680572330452919695036081191681053288393544476733028575858708192356099574890

n = p * q
phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)          # clave privada
m = pow(c, d, n)             # descifra el mensaje
print(long_to_bytes(m))