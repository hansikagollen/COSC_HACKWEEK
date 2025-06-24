import argparse

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    parser = argparse.ArgumentParser(
        description="🔁 Convert temperature between Celsius and Fahrenheit"
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--c2f", type=float, help="Convert Celsius to Fahrenheit")
    group.add_argument("--f2c", type=float, help="Convert Fahrenheit to Celsius")
    
    args = parser.parse_args()

    if args.c2f is not None:
        result = celsius_to_fahrenheit(args.c2f)
        print(f"{args.c2f:.2f}°C = {result:.2f}°F")
    elif args.f2c is not None:
        result = fahrenheit_to_celsius(args.f2c)
        print(f"{args.f2c:.2f}°F = {result:.2f}°C")

if __name__ == "__main__":
    main()
