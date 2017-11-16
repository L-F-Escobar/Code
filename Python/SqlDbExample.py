'''
    Create a database connection to the SQLite databese specified by 
    db_file.
    :param db_file: database file
    :return Connection object or None
'''
def create_connection(db_file):
    ''' Create a database connection to a SQLite database '''
    try:
        connectionObject = sqlite3.connect(db_file)
        return connectionObject
    except Error as e:
        print(e)
    return None


'''
    Create a table from the create_table_SQL statement.
    :param connection: connection object
    :param create_table_SQL: a CREATE TABLE statement
    :return:
'''
def create_table(connectionObject, create_table_SQL):
    try:
        cursorObject = connectionObject.cursor()
        cursorObject.execute(create_table_SQL)
    except Error as e:
        print(e)
        
        
'''
    Create a new project into the projects table.
    :param connectionObject:
    :param project:
    :return: project id
'''
def create_project(connectionObject, project):
    sql = ''' INSERT INTO projects(name, begin_date, end_date)
              VALUES(?,?,?)
              '''
    cursorObject = connectionObject.cursor()
    cursorObject.execute(sql, project)
    return cursorObject.lastrowid


'''
    Create a new task.
    :param connectionObject:
    :param project:
    :return: 
'''
def create_task(connectionObject, task):
    sql = ''' INSERT INTO tasks(name, priority, status_id, project_id, begin_date, end_date)
              VALUES(?,?,?,?,?,?)
              '''
    cursorObject = connectionObject.cursor()
    cursorObject.execute(sql, task)
    return cursorObject.lastrowid     
        
        
'''
    Update priority, begin_date, and end_date of a task.
    :param connectionObjectL
    :param task:
    :return: project id
'''
def update_task(connectionObject, task):
    sql = ''' UPDATE tasks
              SET name = ? ,
                  priority = ? ,
                  begin_date = ? ,
                  end_date= ?
              WHERE id = ?
         '''
    cursorObject = connectionObject.cursor()
    cursorObject.execute(sql, task)
    


'''
    Delete a task in the tasks table by id.
    :param connectionObject: connection to the SQLite database
    :param id: id of the task
    :return:
'''
def delete_task(connectionObject, id):
    sql = 'DELETE FROM tasks WHERE id=?'
    cursorObject = connectionObject.cursor()
    cursorObject.execute(sql, (id,))


'''
    Deletes all rows in the tasks table
    :param connectionObject: connection to the SQLite database
    :return:
'''
def delete_all_task(connectionObject):
    sql = 'DELETE FROM tasks'
    cursorObject = connectionObject.cursor()
    cursorObject.execute(sql)

  

# STEP ONE. <-- CREATE TABLES MUST BE EXECUTED FIRST -->
# Open/Create a SQLite3 database.
database = "C:\\sqlite\\Weather.db"
   
# CREATE TABLE statement example
sql_create_projects_table = ''' CREATE TABLE IF NOT EXISTS projects(
                                id integer PRIMARY KEY,
                                name text NOT NULL,
                                begin_date text,
                                end_date text
                                ); '''
  
# CREATE TABLE statement # CREATE TABLE statement example
sql_create_tasks_table = ''' CREATE TABLE IF NOT EXISTS tasks(
                                id integer PRIMARY KEY,
                                name text NOT NULL,
                                priority integer,
                                status_id integer NOT NULL,
                                project_id integer NOT NULL,
                                begin_date text NOT NULL,
                                end_date text NOT NULL,
                                FOREIGN KEY (project_id) REFERENCES projects (id)
                                ); '''
  
# Create a database connection.
connection = create_connection(database)
if connection is not None:
    # Create projects table.
    create_table(connection, sql_create_projects_table)
    # Create tasks table.
    create_table(connection, sql_create_tasks_table)
else:
    print('Error! Cannot create the database connection.')

 
# STEP TWO <-- GO IN THIS SEQUENCE -->
# Open/Create a SQLite3 database.
database = "C:\\sqlite\\Weather.db"
  
# Create a database connection.
connectionObect = create_connection(database)
  
# Insert data into database.
with connectionObect:
    # Create a new project.
    project = ('Cool App with SQLite & Python', '2017-07-19', '2020-01-22')
    project_id = create_project(connectionObect, project)
       
    # Create a new task.
    task_1 = ('Analyze the requirements of the app', 1, 1, project_id, '2017-07-19', '2020-01-22')
    task_2 = ('Confirm with user about top requirement', 1, 1, project_id, '2017-07-19', '2020-11-22')
   
    # Create tasks.
    create_task(connectionObect, task_1)
    create_task(connectionObect, task_2)

# Update database.
with connectionObect:
    update_task(connectionObect, ('UPDATED TASK', 5, '2025-05-25', '2125-01-35', 2))
     
# Delete a task and all tasks
with connectionObect:
    delete_task(connectionObect, 3)
    #delete_all_tasks(connectionObect) # <-- Will delete all tasks -->
