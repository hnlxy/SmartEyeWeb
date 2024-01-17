import pymysql


def execute_sql_file(file_path, connection):
    # 打开SQL文件并读取内容
    with open(file_path, 'r', encoding='utf-8') as file:
        sql_script = file.read()

    # 使用连接执行SQL语句
    with connection.cursor() as cursor:
        # 分割文件中的多个SQL语句
        sql_statements = sql_script.split(';')

        # 执行每个SQL语句
        for sql_statement in sql_statements:
            if sql_statement.strip():  # 跳过空语句
                cursor.execute(sql_statement)

    # 提交更改
    connection.commit()


# MySQL数据库连接配置
db_config = {
    'host': '39.107.225.242',
    'user': 'root',
    'password': 'smarteye',
    'database': 'smart_eye',
    'charset': 'utf8mb4'
}

# 创建MySQL连接
conn = pymysql.connect(**db_config)

# 在这里替换为你的SQL文件路径
sql_file_path = 'drawSQL-mysql-export-2023-11-15.sql'

# 执行SQL文件
execute_sql_file(sql_file_path, conn)

# 关闭连接
conn.close()
