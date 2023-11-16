from Backend.DAOs.DAO import DAO

class TransferTransactionDAO(DAO):
    def getAllTransferTransaction(self):
        return self._generic_retrieval_query(
            """
            SELECT transferid, tdate, part_amount, to_warehouse, user_requester, tid, pid, uid, wid
            FROM transfer
            NATURAL INNER JOIN transactions;
            """
        )
    

    def getTransferTransactionById(self, transferid):
        return self._generic_retrieval_query(
            query="""
            SELECT transferid, tdate, part_amount, to_warehouse, user_requester, tid, pid, uid, wid
            FROM transfer
            NATURAL INNER JOIN transactions
            WHERE transferid = %s;
            """,
            substitutions=(transferid)
        )


    def addTransferTransaction(self, unit_buy_price, sid, rid, tdate, part_amount, pid, uid, wid):
        tid = self._addEntry(table_name="transactions",
                             id_name="tid",
                             columns=("tdate", "part_amount", "pid", "uid", "wid"),
                             values=(tdate, part_amount, pid, uid, wid))
        transferid = self._addEntry(table_name="transfer",
                              id_name="transferid",
                              columns=("unit_buy_price", "sid", "rid", "tid"),
                              values=(unit_buy_price, sid, rid, tid))
        return transferid


    def modifyTransferTransactionById(self, unit_buy_price, sid, rid, tdate, part_amount, pid, uid, wid, transferid):
        tid = self._generic_retrieval_query(
            query="""
            SELECT tid
            FROM transactions
            NATURAL INNER JOIN transfer
            WHERE transferid = %s;
            """,
            substitutions=transferid
        )[0]
        if not tid:
            return None
        rowcountTransactions = self._modifyEntryByID(table_name="transactions",
                                                     id_name="tid",
                                                     id_value=tid,
                                                     columns=("tdate", "part_amount", "pid", "uid", "wid"),
                                                     values=(tdate, part_amount, pid, uid, wid))
        if not rowcountTransactions:
            return None
        rowcountTransferTransactions = self._modifyEntryByID(table_name="transfer",
                                     id_name="tid",
                                     id_value=tid,
                                     columns=("unit_buy_price", "sid", "rid"),
                                     values=(unit_buy_price, sid, rid))
        return rowcountTransferTransactions