class DataBaseEmulation:
    """
    This class is a placeholder to possible database implementation.
    """

    @staticmethod
    def db_write(key, data_to_write):
        """
        Writes the data to the database.
        :param key: the key to write the data by, an employee's name.
        :param data_to_write: List, optional. If unspecified all values available for a key are overwritten.
        If the params are set, only them are updated. E.g., you may specify ["location", "calendar"]
        :return: None
        """
        pass

    @staticmethod
    def db_fetch(key, params):
        """
        Returns the data by a given key.
        :param key: The key to return the data by, an employee's name.
        :param params: List, optional. If unspecified all values available for a key are returned.
        If the params are set, only them are returned. E.g., you may specify ["location", "calendar"]
        :return: The data by the given key.
        """
        pass
