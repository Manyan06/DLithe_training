class TicketLimitError(Exception):
  pass
available_tickets = 50
try:
  tickets = int(input("Enter number of tickets to book: "))
  if tickets <= 0:
    raise ValueError("Number of tickets must be greater than 0.")
  
  if tickets > available_tickets:
    raise TicketLimitError(f"Only {available_tickets} tickets are available")
  
  available_tickets -= tickets
  print("Booking Successfull")
  print("Remaining Tickets: ",available_tickets)

except ValueError as e:
  print("Input Error: ",e)
except TicketLimitError as e:
  print("Booking Error: ",e)

finally :
  print("Successfully Viwed oversw")