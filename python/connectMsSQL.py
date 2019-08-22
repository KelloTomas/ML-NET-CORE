import pyodbc 
#conn = pyodbc.connect('Driver={SQL Server};'
#                      'Server=dokelu.kst.fri.uniza.sk;'
#                      'Database=TrainsDb19-04-02;'
#                      'Trusted_Connection=yes;'
#                      'UID=xxx;'
#                      'PWD=xxx;')

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=dokelu.kst.fri.uniza.sk;DATABASE=TrainsDb19-04-02;UID=xxx;PWD=xxx')

 
cursor = conn.cursor()

#query = 'SELECT TOP (100) *  FROM [TrainsDb19-04-02].[dbo].[Trains]'

#query = 'SELECT TOP (100) count(*)  FROM [TrainsDb19-04-02].[dbo].[Trains]'

#query = 'SELECT TOP (1) bod1naz  FROM [TrainsDb19-04-02].[dbo].[Trains] where bod1cis = \'34601500\''

query = 'SELECT count(*), druh FROM [TrainsDb19-04-02].[dbo].[Trains] group by druh order by count(*) desc'

cursor.execute(query)

for row in cursor:
    try:
        print(row).decode('latin1')
    except:
        pass
