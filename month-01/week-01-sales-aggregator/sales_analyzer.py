from pathlib import Path

def get_revenue_from_sales(data_path):
    revenue = 0.0
    try:
        with open(data_path, 'r') as file:
            header = next(file)
            for line in file:
                parts = line.strip().split(',')
                price = float(parts[2])
                sold = int(parts[3])
                revenue += price * sold
    except FileNotFoundError:
        print(f"Error: File '{data_path}' not found.")
        return None
    except ValueError:
        print(f"Error: Invalid number format in file on line: {line.strip()}")
        return None
    return revenue

if __name__ == "__main__":
    path = Path("sales_data.csv")
    revenue = get_revenue_from_sales(path)
    if revenue is not None:
        print(f"Total Revenue: ${revenue:.2f}")