def getIndex(getList, value_to_search_for):
  try: 
    for counter in range(len(getList) - 1, -1, -1):
      if getList[counter] == value_to_search_for:
        break
  except:
    print("Error in the getIndex function.")
  return counter + 1

try:
  # Get the input value
  getInput = input()

  # Filter the list to store only integer value.
  getInput = [int(element) for element in getInput if element != " "]

  # Create a view of getInput
  getInputTemp = getInput.copy()
  getInputTemp.sort()

  # Get the value of second highest number in the list.
  second_highest_value = getInputTemp[-2]

  getIndexValue = getIndex(getInput, second_highest_value)

  # Output
  print("value : ", second_highest_value)
  print("position : ", getIndexValue)
except:
  print("Error in the code. Make sure that the input value must be numeric only.")
