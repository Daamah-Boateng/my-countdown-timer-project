import time
import sys

def countdown_timer(total_seconds):
    """
    Displays a real-time countdown timer in the terminal 
    with a progress bar.
    """
    start_time = total_seconds
    
    print("\n--- Countdown Started ---")
    
    while total_seconds > 0:
        # Convert total_seconds to hours, minutes, and seconds
        mins, secs = divmod(total_seconds, 60)
        hours, mins = divmod(mins, 60)
        
        # Format the time output as HH:MM:SS or MM:SS
        if hours > 0:
            time_format = f"{hours:02d}:{mins:02d}:{secs:02d}"
        else:
            time_format = f"{mins:02d}:{secs:02d}"
            
        # Calculate progress bar percentage
        percent = ((start_time - total_seconds) / start_time)
        bar_length = 20
        filled_length = int(bar_length * percent)
        bar = "█" * filled_length + "-" * (bar_length - filled_length)
        
        # Print timer line using \r to overwrite the line each second
        sys.stdout.write(f"\rTime Remaining: {time_format} |[{bar}] {int(percent * 100)}%")
        sys.stdout.flush()
        
        time.sleep(1)
        total_seconds -= 1

    # Final completed output
    sys.stdout.write(f"\rTime Remaining: 00:00 |[{'█' * 20}] 100%\n")
    print("\n🔔 Time's up!\a")  # \a triggers a system alert beep on supported terminals

if __name__ == "__main__":
    try:
        user_input = int(input("Enter countdown time in seconds: "))
        if user_input <= 0:
            print("Please enter a positive integer.")
        else:
            countdown_timer(user_input)
    except ValueError:
        print("Invalid input. Please enter a whole number of seconds.")