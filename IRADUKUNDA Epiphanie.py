from collections import deque
available_drivers = []  
waiting_passengers = deque()  
ride_requests_stack = []  

def add_driver(driver_name):
    """Add a new driver to the list of available drivers."""
    available_drivers.append(driver_name)
    print(f"Driver {driver_name} added.")

def request_ride(passenger_name):
    """Request a ride for a passenger."""
    if not available_drivers:
        print(f"No available drivers for {passenger_name}. Adding to queue.")
        waiting_passengers.append(passenger_name)
    else:
        driver = available_drivers.pop(0) 
        ride_requests_stack.append((passenger_name, driver))
        print(f"{passenger_name} has been assigned to driver {driver}.")

def complete_ride():
    """Complete the last ride and make the driver available again."""
    if ride_requests_stack:
        passenger_name, driver_name = ride_requests_stack.pop()
        print(f"Ride completed for {passenger_name} with driver {driver_name}.")
        available_drivers.append(driver_name)  
        check_waiting_passengers()
    else:
        print("No rides to complete.")

def check_waiting_passengers():
    """Check if there are waiting passengers and assign them to available drivers."""
    while waiting_passengers and available_drivers:
        passenger_name = waiting_passengers.popleft() 
        driver = available_drivers.pop(0)  
        ride_requests_stack.append((passenger_name, driver))
        print(f"{passenger_name} has been assigned to driver {driver} from the waiting queue.")

def undo_last_request():
    """Undo the last ride request."""
    if ride_requests_stack:
        passenger_name, driver_name = ride_requests_stack.pop()
        waiting_passengers.append(passenger_name) 
        available_drivers.append(driver_name)  
        print(f"Undid last request: {passenger_name} and driver {driver_name} returned to waiting queue and available drivers.")
    else:
        print("No ride requests to undo.")

def show_status():
    """Display the current status of drivers and passengers."""
    print("\nCurrent Status:")
    print(f"Available drivers: {available_drivers}")
    print(f"Waiting passengers: {list(waiting_passengers)}")
    print(f"Active ride requests: {ride_requests_stack}\n")
add_driver("Driver A")
add_driver("Driver B")

request_ride("Passenger 1")
request_ride("Passenger 2")
request_ride("Passenger 3")  

show_status()

complete_ride() 
show_status()

undo_last_request() 
show_status()