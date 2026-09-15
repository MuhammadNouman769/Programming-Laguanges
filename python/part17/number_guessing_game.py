import random

"""
Mini Project: Number Guessing Game (Random Number Game)
Part 17 - Python Programming
Description:
    Computer 1 se lekar select kiye gaye range tak ek random number choose karta hai.
    User ko hints (Too High / Too Low) ke sath sahi number guess karna hota hai.
"""

def play_game():
    print("\n" + "=" * 50)
    print("🎯 Welcome to the Number Guessing Game! 🎯")
    print("=" * 50)

    print("\nSelect Difficulty Level / Mushkil ka darja chunein:")
    print("1. Easy   (Range: 1 - 50,  Attempts: 10)")
    print("2. Medium (Range: 1 - 100, Attempts: 7)")
    print("3. Hard   (Range: 1 - 200, Attempts: 5)")

    while True:
        choice = input("\nApna choice enter karein (1-3): ").strip()
        if choice == "1":
            max_num = 50
            max_attempts = 10
            break
        elif choice == "2":
            max_num = 100
            max_attempts = 7
            break
        elif choice == "3":
            max_num = 200
            max_attempts = 5
            break
        else:
            print("❌ Invalid choice! Bara-e-meherbani 1, 2 ya 3 enter karein.")

    secret_number = random.randint(1, max_num)
    attempts = 0

    print(f"\nMaine 1 se {max_num} ke darmiyan ek number select kiya hai.")
    print(f"Aapke paas total {max_attempts} attempts hain. Koshish karein!\n")

    while attempts < max_attempts:
        attempts += 1
        remaining = max_attempts - attempts

        try:
            user_input = input(f"[Attempt {attempts}/{max_attempts}] Apna guess enter karein: ").strip()
            guess = int(user_input)
        except ValueError:
            print("⚠️  Invalid input! Sirf aik valid number enter karein.")
            attempts -= 1  # Invalid input par attempt zaya nahi hogi
            continue

        if guess < 1 or guess > max_num:
            print(f"⚠️  Number 1 se {max_num} ke darmiyan hona chahiye!")
            attempts -= 1
            continue

        if guess == secret_number:
            print("\n" + "*" * 50)
            print("🎉 Mubarak ho! Aapne bilkul sahi number guess kar liya! 🎉")
            print(f"🏆 Secret Number tha: {secret_number}")
            print(f"⭐ Aapne yeh number {attempts} koshish(on) mein pehchan liya!")
            print("*" * 50 + "\n")
            return
        elif guess < secret_number:
            print("📉 Too Low! (Socha hua number is se BADA hai)")
        else:
            print("📈 Too High! (Socha hua number is se CHOTA hai)")

        if remaining > 0:
            print(f"⏳ Baqi attempts: {remaining}\n")
        else:
            print("\n" + "-" * 50)
            print("😢 Game Over! Aapke tamaam attempts khatam ho gaye.")
            print(f"Sahi number tha: {secret_number}")
            print("-" * 50 + "\n")

def main():
    try:
        while True:
            play_game()
            play_again = input("Kya aap dobara khelna chahte hain? (y/n): ").strip().lower()
            if play_again not in ('y', 'yes'):
                print("\nShukriya khelne ka! Allah Hafiz! 👋\n")
                break
    except (KeyboardInterrupt, EOFError):
        print("\n\nKhuda Hafiz! Game exit ho gaya. 👋\n")

if __name__ == "__main__":
    main()
