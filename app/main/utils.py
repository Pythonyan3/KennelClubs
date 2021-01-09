from app.models import DBManager


def clubs_addresses():
    with DBManager() as manager:
        query = """
            SELECT club_caption, address 
            FROM clubs
        """
        return manager.select(query)


def possible_rewards():
    with DBManager() as manager:
        query = """
            SELECT reward_caption, icon 
            FROM rewards
        """
        return manager.select(query)


def most_active_pets():
    with DBManager() as manager:
        query = """
            SELECT breed_name, count(id_dog), (SELECT count(*) FROM dogs) as all_count 
            FROM dogs INNER JOIN breeds USING (id_breed) 
            GROUP BY id_breed, breed 
            ORDER BY count(id_dog) DESC LIMIT 3
        """
        return manager.select(query)
