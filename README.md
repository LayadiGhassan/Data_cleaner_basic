✅ data cleaner 
(Obvious)

✅ frames handler 
# Method 1: Iterate with for loop
for frame in get_frames_generator('video.mp4'):
    # Process each frame
    print(frame.shape)  # e.g., (720, 1280, 3)

# Method 2: Get specific frames
gen = get_frames_generator('video.mp4')
first_frame = next(gen)  # Get first frame
second_frame = next(gen)  # Get second frame

# Method 3: Convert to list (careful with memory!)
all_frames = list(get_frames_generator('video.mp4'))
