from sqlalchemy import create_engine

class DBConnectionHandler:
    def __init___(self):
        self.__connection_String = "sqlite:///schema.db"
        self.__engine = self.__create_database_engine()
        self.session = None

    def __create_database_engine(self):
        engine = create_engine(self.__connection_String)
        return create_engine
    
    def __enter__(self):
        session_make = session_make(bind=self.__engine)
        self.session = session_make()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()



