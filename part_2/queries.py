from mysql_connector_config import Mysql


class Queries:

    def query_1_mooving_alert():
        cnx = Mysql.get_mysql_connection()
        cursor = cnx.cursor()
        # priority 1 or 2 and mooved at least 5 km
        # entity_id, target_name, priority_leve from targets
        query = '''SELECT * FROM targets
                    WHERE (priority = 1 OR priority = 2)
                            AND movement_distance_km >= 5'''
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        cnx.close()
        return result
    

    def query_2():
        pass