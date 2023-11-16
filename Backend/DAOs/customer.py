from Backend.DAOs.DAO import DAO


class CustomerDAO(DAO):
    def getAllCustomers(self):
        return self._getAllEntries(table_name="customer",
                                   columns=("cid", "cfname", "clname", "czipcode", "cphone"))

    def getCustomerById(self, cid):
        return self._getEntryByID(table_name="customer",
                                  id_name="cid",
                                  id_value=str(cid),
                                  columns=("cid", "cfname", "clname", "czipcode", "cphone"))

    def addCustomer(self, cfname, clname, czipcode, cphone):
        return self._addEntry(table_name="customer",
                              id_name="cid",
                              columns=("cfname", "clname", "czipcode", "cphone"),
                              values=(cfname, clname, czipcode, cphone))

    def modifyCustomerById(self, cfname, clname, czipcode, cphone, cid):
        return self._modifyEntryByID(table_name="customer",
                                     id_name="cid",
                                     id_value=str(cid),
                                     columns=("cfname", "clname", "czipcode", "cphone"),
                                     values=(cfname, clname, czipcode, cphone))

    def deleteCustomerById(self, cid):
        return self._deleteEntryByID(table_name="customer",
                                     id_name="cid",
                                     id_value=cid)