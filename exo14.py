word = input("Word: ")
frame_width = 30
total_padding = frame_width - len(word)
left_padding = total_padding // 2
right_padding = total_padding - left_padding

print("*" * frame_width)

print("*" + " " * left_padding + word + " " * right_padding + "*")
print("*" * frame_width)
