import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="kousik@123",
    database="HR DBS")
cursor=conn.cursor()

cursor.execute("""create table if not exists Employee_Data(
    Employee_Id int,
    Employee_Name varchar(25),
    Employee_RegionID int,
    Region_Name varchar(10),
    Employee_Age int,
    Employee_Salary int,
    Total_Sales int
    )
    """)
sql="""insert into Employee_Data(
Employee_Id,
Employee_Name,
Employee_RegionID,
Region_Name,
Employee_Age,
Employee_Salary,
Total_Sales)
values (%s,%s,%s,%s,%s,%s,%s)"""

val=[
(320100,"Kumar",2,"North",28,39000,50),
(320101,"Divya",3,"East",23,26000,72),
(320102,"Harish",2,"East",32,53000,62),
(320103,"Yogesh",1,"South",22,39000,55),
(320104,"Krunal",3,"East",38,53000,40),
(320105,"Pandiyan",4,"West",22,20000,78),
(320106,"Yuvaraj",1,"North",22,20000,32),
(320107,"Harini",2,"East",24,26000,80),
(320108,"Rubesh",4,"West",22,53000,60),
(320106,"Yuvaraj",1,"North",22,20000,90),
(320107,"Praveen",1,"West",29,39000,85),
(320108,"Dharani",2,"East",30,35000,50),
(320109,"Yogini",3,"South",36,40000,65),
(321100,"Yashika",3,"South",32,40000,70),
(321101,"Kishore",2,"North",32,39000,60),
(321101,"Abi",2,"West",32,39000,40),
(321102,"Renu",1,"East",33,39000,30),
(321103,"Kousik",4,"North",29,53000,90),
(321104,"Dhayanithi",2,"East",29,39000,80),
(321105,"Hariharan",3,"West",23,20000,70),
(321106,"Kamesh",2,"South",23,20000,35),
(321107,"Pragathi",3,"East",29,39000,75),
(321108,"Dharshini",3,"South",29,53000,45),
(321109,"Srimathi",1,"North",27,26000,85),
(321110,"Yashavathi",4,"West",28,40000,65),
]

cursor.executemany(sql,val)
conn.commit()
cursor.execute("Select * from Employee_Data")
rows=cursor.fetchall()
print("\n Employee Data\n")

for row in rows:
    print(row)
conn.close()

print("\nTable is created successfully")
