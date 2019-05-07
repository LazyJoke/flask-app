from app import create_app


(manager, db) = create_app()

if __name__ == '__main__':
    manager.run()
