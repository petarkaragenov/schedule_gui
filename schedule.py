from views.main import main
from db.db import con

if __name__ == "__main__":
    main()

    con.close()

