from Backend.DAOs.DAO import DAO

class TransactionDAO(DAO):
    def getAllTransactions(self):
        return self._getAllEntries(
            table_name="transactions",
            columns=("tid", "tdate", "part_amount", "pid", "uid", "wid")
        )
 
    def getTransactionByID(self, tid):
        return self._getEntryByID(
            table_name="transactions",
            id_name="tid",
            id_value=tid,
            columns=("tid", "tdate", "part_amount", "pid", "uid", "wid")
        )