"""Task 1: create small utility functions and call them from main."""

from datetime import datetime


def current_time():
	"""Return the current date and time as formatted text."""
	return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def main():
	print(f"Current time: {current_time()}")


if __name__ == "__main__":
	main()