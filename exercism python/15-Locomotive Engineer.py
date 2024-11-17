"""Functions which helps the locomotive engineer to keep track of the train."""
def get_list_of_wagons(*args):
    return list(args)
def fix_list_of_wagons(each_wagons_id, missing_wagons):
    x, y, z, *rest = each_wagons_id;
    new_order = [z, *missing_wagons, *rest, x, y];
    return new_order;
    
def add_missing_stops(routing, **kwargs):
    stops = list(kwargs.values())
    routing["stops"] = stops
    return routing
def extend_route_information(route, more_route_information):
    return {**route, **more_route_information}
def fix_wagon_depot(wagon_data):
    transposed = list(zip(*wagon_data))
    return [list(row) for row in transposed]