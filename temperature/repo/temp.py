from deta import Deta

deta = Deta("a09rrrza_mW3BFLo4fDmUfMxEndWyjBKeZAQn8ZEf")
db = deta.Base("temperature")


def all_temp():
    return [x for x in db.fetch().items]


def add_temp(new_temp):
    return db.put(new_temp, key=new_temp)


def latest_temp():
    return [x for x in db.fetch().items][-1]
