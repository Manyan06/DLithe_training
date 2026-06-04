class SlotOccupiedError(Exception):
  pass
class InvalidSlotError(Exception):
  pass
parking_slots = [None] * 5

try :
  while parking_slots is not None:
    vehicle_number = input("Enter vehicle no.: ")
    slot_number = int(input("Enter Slot no.(1-5): "))

    if slot_number < 1 or slot_number > 5 :
      raise InvalidSlotError(
        "Slot number must be between 1-5."
      )
    
    if parking_slots[slot_number - 1] is not None:
      raise SlotOccupiedError(
        "Selected slot is already occupied."
      )
    
    parking_slots[slot_number - 1] = vehicle_number
    print("\nVehicle Parked Successfully")
    print("Parking Status: ")
    
    for i in range(len(parking_slots)):
      if parking_slots[i]:
        print(f"Slot {i+1}: {parking_slots[i]}")
      else :
        print(f"Slot {i+1}: Empty")

except ValueError:
   print("Please Enter a valid slot number")
except InvalidSlotError as e:
   print("Invalid slot Error: ", e)
except SlotOccupiedError as e:
   print("Parking Error: ", e)
finally:
   print("Parking Transaction Completed")