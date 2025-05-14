from Base.Base_db import DB
db = DB()
db.connect(
    db_type='postgresql',
    host='new.pg.server',
    user='admin',
    password='Temp@123',
    database='reports'
)
data = db.execute_query("SELECT * FROM daily_report")
db.close()