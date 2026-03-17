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
    

    def query_2_count_signal_type():
        cnx = Mysql.get_mysql_connection()
        cursor = cnx.cursor()
        # count how many signal are from every type
        query = '''SELECT signal_type COUNT(*) FROM intel_signals
                    GROUP BY signal_type
                    ORDER BY COUNT(*) DESC'''
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        cnx.close()
        return rows
    


    def query_3_top_3_unknown():
        cnx = Mysql.get_mysql_connection()
        cursor = cnx.cursor()
        # the top 3 targets that are unknown
        # subquery to find all the unknown targets priority level = 99
        query = '''SELECT entity_id, COUNT(*) FROM (SELECT * FROM targets WHERE priority_level = 99)
                    GROUP BY entity_id
                    ORDER BY COUNT(*) DESC
                    LIMIT 3'''
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        cnx.close()
        return rows
    

    def query_4_waking_up():
        cnx = Mysql.get_mysql_connection()
        cursor = cnx.cursor()
        # join targets and intel_signals
        query = '''SELECT entity_id FROM targets
                    INNER JOIN intel_signals
                        ON entity_id.targets = entity_id.intel_signals
                    WHERE (HOUR(timestamp.intel_signals) BETWEEN 8 AND 20 AND movement_distance_km = 0)
                            AND 
                            (HOUR(timestamp.intel_signals) BETWEEN 20 AND 8 AND movement_distance_km > 10)'''
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        cnx.close()
        return rows