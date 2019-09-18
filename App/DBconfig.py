def data():
    import os
    dtlist = []
    user = os.environ['USER']
    password = os.environ['PASS']
    host = os.environ['HOST']
    port = "5432"
    database = "da5rk6c5e5n5aj"
    table = "datatrain"
    dtlist.append(user)
    dtlist.append(password)
    dtlist.append(host)
    dtlist.append(port)
    dtlist.append(database)
    dtlist.append(table)
    return dtlist