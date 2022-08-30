SECRET_KEY = 'alura'

SQLALCHEMY_DATABASE_URI = \
    '{SGDB}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGDB = 'mysql+mysqlconnector',
        usuario = 'layramendes',
        senha = 'Robertinho123?',
        servidor = 'localhost',
        database = 'jogoteca'
    )