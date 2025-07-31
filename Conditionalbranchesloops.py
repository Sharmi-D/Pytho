# Movie list with ticket price
movies = {
    "Inception": 150,
    "Interstellar": 180,
    "Oppenheimer": 200,
    "Kung Fu Panda 4": 120
}

# Function to display movies
def display_movies():
    print("\n🎥 Available Movies:")
    for name, price in movies.items():
        print(f"🎬 {name} - ₹{price} per ticket")

# Booking loop
while True:
    display_movies()
    
    choice = input("\nEnter movie name to book (or 'exit' to quit): ").strip()

    if choice.lower() == "exit":
        print("Thank you for visiting. 🎟️")
        break

    elif choice in movies:
        price = movies[choice]
        try:
            tickets = int(input(f"How many tickets for '{choice}'? 🎟️: "))
            if tickets <= 0:
                print("❌ Please enter a valid number of tickets.")
                continue
        except ValueError:
            print("❌ Please enter a number.")
            continue

        total = price * tickets

        # Apply discount if more than 4 tickets
        if tickets >= 5:
            discount = total * 0.1  # 10% discount
            total -= discount
            print(f"🎁 Group discount applied: ₹{discount:.2f}")

        print(f"✅ Booking Confirmed! Total amount: ₹{total:.2f}")

    else:
        print("❌ Movie not found. Please choose from the list.")
