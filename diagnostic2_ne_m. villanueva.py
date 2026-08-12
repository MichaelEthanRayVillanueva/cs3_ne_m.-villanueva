def calculate_fuel(cargo_weight):
    cargo_weight+=50000
    fuel=cargo_weight*3
    return fuel
cargo=0
weight=0
while cargo != "launch":
    cargo=input("What would you like to add to the ship? type either 'satellite', 'rover', or 'supplies'. If you're ready to take off, type 'launch'. ")
    if cargo=="satelllite":
        weight+=1000
        limiter=1000
    elif cargo=="rover":
        weight+=2500
        limiter=2500
    elif cargo=="supplies":
        weight+=500
        limiter=500
    else:
        print("Item is not approved for mission.")
    if weight > 10000:
        print("ERROR. MAX WEIGHT REACHED")
        weight=weight-limiter
print("Launching rocket.")
print(f"{calculate_fuel(weight)} gallons of fuel used.")
print("Goodbye")