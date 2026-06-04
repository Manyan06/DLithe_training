from collections import deque
ticket_queue = deque()
while True:
  print("\n1. Book Ticket")
  print("2. Serve Customer")
  print("3. Display Queue")
  print("4. Exit")

  choice = input("Enter Choice: ")
  if choice == "1" :
    customer = input("Enter customer name: ")
    ticket_queue.append(customer)
    print(customer, "added to booking queue.")
  elif choice == "2" :
    if ticket_queue:
      print("Ticket issued to: ",ticket_queue.popleft())
    else: 
      print("No customers in queue.")
  elif choice == "3" :
      print("Current Queue: ",list(ticket_queue))
  elif choice == "4" :
    break