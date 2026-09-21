while True:
    try:
        output_power = float(input("Please enter the output power in [kW]: "))
        if output_power < 0:
            print("Output power cannot be a negative value. Try again.")
            continue

        input_power = float(input("Please enter the input power in [kW]: "))
        if input_power < 0:
            print("Input power cannot be a negative value. Try again.")
            continue
        if input_power < output_power:
            print("Output power cannot exceed input power. Try again.")
            continue

        print(f"Efficiency: {output_power/input_power * 100:.2f}%")
        break
    
    except ValueError:
        print("Please enter a valid value. Try again.")

    except ZeroDivisionError:
        print("Input power cannot be ZERO. Try again.")