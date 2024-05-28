from database.DB_connect import DBConnect
from model.go_retailers import go_retailers


class DAO():
    @staticmethod
    def getAllYears() -> list[tuple[int]] | None:
        cnx = DBConnect.get_connection()
        if cnx is not None:
            cursor = cnx.cursor()
            query = """SELECT DISTINCT YEAR(gds.Date)
                           FROM go_daily_sales gds"""
            cursor.execute(query)
            rows = cursor.fetchall()
            cursor.close()
            cnx.close()
            return rows
        else:
            print("Errore nella connessione")
            return None

    @staticmethod
    def getAllCountries() -> list[tuple[str]]:
        cnx = DBConnect.get_connection()
        if cnx is not None:
            cursor = cnx.cursor()
            query = """select distinct gr.Country 
                        from go_retailers gr """
            cursor.execute(query)
            rows = cursor.fetchall()
            cursor.close()
            cnx.close()
            return rows
        else:
            print("Errore di connessione")
            return None

    @staticmethod
    def getAllRetailers(country):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
                    from go_retailers gr 
                    where gr.Country = %s"""

        cursor.execute(query, (country,))

        for row in cursor:
            result.append(go_retailers(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllEdges(country, year):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select gr1.Retailer_code, gr2.Retailer_code
            from go_retailers gr1, go_retailers gr2, go_daily_sales gds1, go_daily_sales gds2  
            where gr1.Country = 'France' 
            and gr2.Country  = 'France'
            and year(gds1.`Date`) = 2015
            and year(gds2.`Date`) = 2015
            and gr1.Retailer_code < gr2.Retailer_code 
            and gds1.Retailer_code = gr1.Retailer_code 
            and gds2.Retailer_code = gr2.Retailer_code 
            and gds1.Product_number = gds2.Product_number 
            """

        cursor.execute(query, (country,country, year))

        for row in cursor:
            result.append(go_retailers(**row))

        cursor.close()
        conn.close()
        return result