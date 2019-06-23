from passlib.hash import pbkdf2_sha256

password = input()
hash_ = str(pbkdf2_sha256.hash('qwerty'))

# print(pbkdf2_sha256.verify(password, hash))
# hash_db = "$pbkdf2-sha256$29000$AeAcw9gbY6x1bm2tNQagVA$fQXwCUMrCz28LQfa06TbneMYHZeRLzWz8AIzXXL7RYU"
print(pbkdf2_sha256.verify(password, hash_))
