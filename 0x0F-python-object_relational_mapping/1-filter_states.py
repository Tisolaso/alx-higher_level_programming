#!/usr/bin/python3
"""
states models
"""
if __name__ == "__main__":
    from MySQLdb import _mysql
    import sys

    args = sys.argv[1:]

    db_config = {
            'host': 'localhost',
            'port': 3306,
            'user': args[0],
            'password': args[1],
            'database': args[2],
            }
    db = _mysql.connect(**db_config)
    db.query(""" SELECT * FROM states WHERE name LIKE 'N%' """)

    r = db.store_result()

    r = r.fetch_row(maxrows=0)

    for row in r:
        print(f"({row[0].decode()}, '{row[1].decode()}')")
        db.close()
