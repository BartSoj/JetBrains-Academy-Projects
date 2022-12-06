import json
import re

types = {"bus_id": int,
         "stop_id": int,
         "stop_name": str,
         "next_stop": int,
         "stop_type": str,
         "a_time": str}

errors = {"bus_id": 0,
          "stop_id": 0,
          "stop_name": 0,
          "next_stop": 0,
          "stop_type": 0,
          "a_time": 0}


def get_data():
    try:
        return json.loads(input())
    except json.JSONDecodeError:
        return None


def check_entry(entry):
    for prop_name, prop_type in types.items():
        if type(entry[prop_name]) != prop_type:
            errors[prop_name] += 1
        elif prop_name == "stop_name":
            if not re.match("^([A-Z]+\w* )+(Road|Avenue|Boulevard|Street)$", entry[prop_name]):
                errors[prop_name] += 1
        elif prop_name == "stop_type":
            if entry[prop_name] not in ("", "S", "O", "F"):
                errors[prop_name] += 1
        elif prop_name == "a_time":
            if not re.match("^([0-1][0-9]|2[0-3]):[0-5][0-9]$", entry[prop_name]):
                errors[prop_name] += 1


def check_data(data):
    for entry in data:
        check_entry(entry)


def type_validation():
    global errors
    errors_sum = sum(errors.values())

    print(f"Type and required field validation: {errors_sum} errors")
    for err_name, err_val in errors.items():
        print(f"{err_name}: {err_val}")


def format_validation():
    global errors
    format_validation_fields = "stop_name", "stop_type", "a_time"
    errors = {key: val for key, val in errors.items() if key in format_validation_fields}
    errors_sum = sum(errors.values())

    print(f"Format validation: {errors_sum} errors")

    for err_name, err_val in errors.items():
        print(f"{err_name}: {err_val}")


def bus_lines(data):
    buses = {}

    for entry in data:
        bus_id = entry["bus_id"]
        if bus_id not in buses:
            buses[bus_id] = {entry["stop_id"]}
        else:
            buses[bus_id].add(entry["stop_id"])

    print("Line names and number of stops:")
    for bus_id, stops in buses.items():
        print(f"bus_id: {bus_id}, stops: {len(stops)}")


def get_transfer_stops(data):
    stop_usage = {}

    for entry in data:
        if entry["stop_name"] not in stop_usage:
            stop_usage[entry["stop_name"]] = 1
        else:
            stop_usage[entry["stop_name"]] += 1

    return [stop for stop, usage in stop_usage.items() if usage > 1]


def stops(data):
    buses = set()
    bus_starts = set()
    bus_ends = set()
    start_stops = set()
    finish_stops = set()

    for entry in data:
        buses.add(entry["bus_id"])

        if entry["stop_type"] == "S":
            if entry["bus_id"] in bus_starts:
                print(f"There is no start or end stop for the line: {entry['bus_id']}.")
                return
            else:
                bus_starts.add(entry["bus_id"])
                start_stops.add(entry["stop_name"])
        elif entry["stop_type"] == "F":
            if entry["bus_id"] in bus_ends:
                print(f"There is no start or end stop for the line: {entry['bus_id']}.")
                return
            else:
                bus_ends.add(entry["bus_id"])
                finish_stops.add(entry["stop_name"])

    for bus in buses:
        if bus not in bus_starts or bus not in bus_ends:
            print(f"There is no start or end stop for the line: {bus}.")
            return

    start_stops = sorted(list(start_stops))
    finish_stops = sorted(list(finish_stops))
    transfer_stops = sorted(get_transfer_stops(data))

    print(f"Start stops: {len(start_stops)} {start_stops}")
    print(f"Transfer stops: {len(transfer_stops)} {transfer_stops}")
    print(f"Finish stops: {len(finish_stops)} {finish_stops}")


def arrival_time_test(data):
    bus_arrival = {}
    anomalies = {}
    for entry in data:
        bus_id = entry["bus_id"]
        if bus_id not in bus_arrival:
            bus_arrival[bus_id] = entry["a_time"]
        elif bus_id not in anomalies:
            if bus_arrival[bus_id] >= entry["a_time"]:
                anomalies[bus_id] = entry["stop_name"]
            else:
                bus_arrival[bus_id] = entry["a_time"]

    print("Arrival time test:")
    if anomalies:
        for bus, stop in anomalies.items():
            print(f"bus_id line {bus}: wrong time on station {stop}")
    else:
        print("OK")


def on_demand_stops_test(data):
    transfer_stops = get_transfer_stops(data)
    wrong_stops = set()

    for entry in data:
        if entry["stop_name"] in transfer_stops and entry["stop_type"] == "O":
            wrong_stops.add(entry["stop_name"])

    wrong_stops = sorted(list(wrong_stops))

    print("On demand stops test:")
    if wrong_stops:
        print(f"Wrong stop type: {wrong_stops}")
    else:
        print("OK")


def run():
    data = get_data()
    on_demand_stops_test(data)


run()
