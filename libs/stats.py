stats = {}
stat_descriptions = {}

def initialize_stats(stat_ids, stat_descriptions, init_value=0):
    """
    Initializes N new stats with id in the list stat_ids, gives it a starting a value

    :param stat_id: ids of the new stats
    :param init_value: starting value for the new stats
    """
    for i in range(0, len(stat_ids)):
        initialize_stat(stat_ids[i], stat_descriptions[i], init_value)

def initialize_stat(stat_id, stat_description, init_value=0):
    """
    Initializes a new stat with id stat_id, gives it a starting a value

    :param stat_id: id of the new stat
    :param init_value: starting value for the new stat 
    """
    stats[stat_id] = {}
    stats[stat_id]["value"] = init_value
    stats[stat_id]["description"] = stat_description

def sum_stat(stat_id, value=0):
    """
    Sums to the value of the stat identified with stat_id a new value

    :param stat_id: key in the stats dictionary to update
    :param value: value to add to the current value of the stat
    :return: returns the new value of the stat
    """
    stats[stat_id]["value"] += value
    return stats[stat_id]["value"] 

def print_stats(to_file=""):
    """
    Prints saved stats
    """
    for id in stats:
        if to_file:
            print("{} : {}".format(stats[id]["description"], stats[id]["value"]), file=open(to_file, "a"))
        else:
            print("{} : {}".format(stats[id]["description"], stats[id]["value"]))