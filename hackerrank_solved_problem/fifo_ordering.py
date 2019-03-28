number = int(input("Enter the frame value:"))
page_value = 5
page_reference = []
# list1 = [[0]*number]
for i in range(0, page_value):
    page_number = int(input("Values of pages"))
    page_reference.append(page_number)
print(page_reference)

frame_list = []
count = 0

for element in page_reference:
    frame = []
    frame.append(element)
    frame_list.append(frame)
    index_to_change = 0
    if not frame_list:
        difference = number - len(frame)
        for num in range(0, difference):
            frame.append(None)
    else:
        previous_frame_to_change = frame_list[-1]
        for index, old_element in enumerate(previous_frame_to_change):
            if old_element is None:
                previous_frame_to_change[index] = element
                frame_list.append(previous_frame_to_change)
                continue



    # elif len(frame) == number:
    #     last_frame = frame_list[element]
    #     last_frame[index_to_change] = page_reference[element]
    #     frame_list.append(last_frame)
    # else:
    #     frame_list.append(frame)
# print(list1)
