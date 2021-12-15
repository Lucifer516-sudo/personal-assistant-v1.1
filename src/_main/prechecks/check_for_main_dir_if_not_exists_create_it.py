def preckeck_one():    
    from src.core.configurer.directories_creator import make_the_home_dir_to_save_the_db
    
    home_dir_to_save_db = False
    
    create_home_dir = make_the_home_dir_to_save_the_db()
    if create_home_dir:
        home_dir_to_save_db = True
    
    return home_dir_to_save_db

print(preckeck_one())
