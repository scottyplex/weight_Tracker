# weight_tracker.py

import datetime
import matplotlib.pyplot as plt

# The file where we'll store our data
DATA_FILE = 'weights.txt'

def main_menu():
    """Presents the main menu to the user."""
    print("\n--- Weight Tracker Menu ---")
    print("1. Add a new weight entry")
    print("2. View all weight entries")
    print("3. Calculate average weight")
    print("4. View progress chart")
    print("5. Exit")

def add_weight_entry():
    """Handles adding a new weight entry."""
    try:
        weight = float(input("Enter your current weight (in kg or lbs): "))
        
        # Get today's date in a simple format1
        date_str = datetime.date.today().isoformat()
        
        with open(DATA_FILE, 'a') as f:
            f.write(f"{date_str},{weight}\n")
        
        print(f"Weight of {weight} recorded for {date_str}.")
        
    except ValueError:
        print("Invalid input. Please enter a number for the weight.")
    except Exception as e:
        print(f"An error occurred: {e}")

def view_all_entries():
    """Displays all recorded weight entries."""
    try:
        with open(DATA_FILE, 'r') as f:
            lines = f.readlines()
            
            if not lines:
                print("No weight entries found.")
                return
            
            print("\n--- All Weight Entries ---")
            for line in lines:
                try:
                    date, weight = line.strip().split(',')
                    print(f"Date: {date}, Weight: {weight}")
                except (ValueError, IndexError):
                    print(f"Skipping malformed line: {line.strip()}")
                
    except FileNotFoundError:
        print("No weight data file found. Add an entry first.")
    except Exception as e:
        print(f"An error occurred: {e}")

def calculate_average_weight():
    """Calculates and displays the average weight."""
    try:
        with open(DATA_FILE, 'r') as f:
            lines = f.readlines()
            
            if not lines:
                print("No weight entries found to calculate an average.")
                return
            
            total_weight = 0
            count = 0
            
            for line in lines:
                try:
                    _, weight_str = line.strip().split(',')
                    total_weight += float(weight_str)
                    count += 1
                except (ValueError, IndexError):
                    print(f"Skipping malformed line: {line.strip()}")
            
            if count > 0:
                average = total_weight / count
                print(f"\n--- Average Weight ---")
                print(f"Based on {count} entries, your average weight is: {average:.2f}")
            else:
                print("No valid weight entries found.")
                
    except FileNotFoundError:
        print("No weight data file found. Add an entry first.")
    except Exception as e:
        print(f"An error occurred: {e}")

def view_progress_chart():
    """Creates a line graph of weight entries over time."""
    try:
        with open(DATA_FILE, 'r') as f:
            lines = f.readlines()
            
            if len(lines) < 2:
                print("Not enough data to create a chart (minimum 2 entries required).")
                return

            dates = []
            weights = []

            for line in lines:
                try:
                    date_str, weight_str = line.strip().split(',')
                    dates.append(datetime.datetime.strptime(date_str, '%Y-%m-%d'))
                    weights.append(float(weight_str))
                except (ValueError, IndexError):
                    print(f"Skipping malformed line: {line.strip()}")

            if len(dates) < 2:
                print("No valid data found to create a chart (minimum 2 entries required).")
                return

            # Create the plot
            plt.figure(figsize=(10, 6))
            plt.plot(dates, weights, marker='o', linestyle='-', color='b')
            plt.title('Weight Progress Over Time')
            plt.xlabel('Date')
            plt.ylabel('Weight')
            plt.grid(True)
            plt.xticks(rotation=45)
            plt.tight_layout()

            # Display the plot
            plt.show()

    except FileNotFoundError:
        print("No weight data file found. Add an entry first.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    """The main function to run the application."""
    while True:
        main_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_weight_entry()
        elif choice == '2':
            view_all_entries()
        elif choice == '3':
            calculate_average_weight()
        elif choice == '4':
            view_progress_chart()
        elif choice == '5':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()