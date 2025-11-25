def square_root_bisection(number ,tolerance = 1e-6, max_iterations = 100):
    if number < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")

    elif number == 0 or number == 1:
        print(f"The square root of {number} is {number}")
        return number

    else:
        iterations = 0
        if number < 1:
            upper_bound = 1
        else:
            upper_bound = number

        lower_bound = 0

        while iterations < max_iterations:
            iterations += 1
            mid = (upper_bound + lower_bound)/2
            mid_square = mid ** 2

            if abs(mid - number**0.5) <= tolerance:
                print(f"The square root of {number} is approximately {mid}")
                return mid
            elif mid_square > number:
                upper_bound = mid
            else:
                lower_bound = mid

        print(f"Failed to converge within {max_iterations} iterations")
        return None
