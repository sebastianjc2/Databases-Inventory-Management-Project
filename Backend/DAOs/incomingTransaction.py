from Backend.DAOs.DAO import DAO

class IncomingTransactionDAO(DAO):
    def getAllIncomingTransaction(self):
        return self._generic_query(
            """
            SELECT itid, tdate, unit_buy_price, part_amount, sid, rid, tid, pid, uid, wid
            FROM incoming_transaction
            NATURAL INNER JOIN transactions 
            """
        )
    

    def getIncomingTransactionById(self, itid):
        return self._generic_query(
            query="""
            SELECT itid, tdate, unit_buy_price, part_amount, sid, rid, tid, pid, uid, wid
            FROM incoming_transaction
            NATURAL INNER JOIN transactions
            WHERE itid = %s
            """,
            substitutions=(itid)
        )


    def addIncomingTransaction(self, unit_buy_price, sid, rid, tdate, part_amount, pid, uid, wid):
        tid = self._addEntry(table_name="transactions",
                             id_name="tid",
                             columns=("tdate", "part_amount", "pid", "uid", "wid"),
                             values=(tdate, part_amount, pid, uid, wid))
        itid = self._addEntry(table_name="incoming_transaction",
                              id_name="itid",
                              columns=("unit_buy_price", "sid", "rid", "tid"),
                              values=(unit_buy_price, sid, rid, tid))
        return itid


    def modifyIncomingTransactionById(self, unit_buy_price, sid, rid, tdate, part_amount, pid, uid, wid, itid):
        tid = self._generic_query(
            """
            SELECT tid
            FROM transactions
            NATURAL INNER JOIN incomind_transaction 
            """
        )
        rowcountTransactions = self._modifyEntryByID(table_name="transactions",
                                                     id_name="tid",
                                                     id_value=str(tid),
                                                     columns=("tdate", "part_amount", "pid", "uid", "wid"),
                                                     values=(tdate, part_amount, pid, uid, wid))
        rowcountIncomingTransactions = self._modifyEntryByID(table_name="incoming_transaction",
                                     id_name="itid",
                                     id_value=str(itid),
                                     columns=("unit_buy_price", "sid", "rid"),
                                     values=(unit_buy_price, sid, rid))
        return rowcountIncomingTransactions