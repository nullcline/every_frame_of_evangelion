# A simple script for posting images to Facebook

import sys
import facebook
import time
import glob

titles = {1: "Angel Attack",
          2: "The Beast",
          3: "A Transfer",
          4: "Hedgehog's Dilemma",
          5: "Rei I",
          6: "Rei II",
          7: "A Human Work",
          8: "Asuka Strikes!",
          9: "Both of You, Dance Like You Want to Win!",
          10: "Magma Diver",
          11: "The Day Tokyo-3 Stood Still",
          12: "She said, \"Don't make others suffer for your personal hatred\"",
          13: "Liliputian Hitcher",
          14: "Weaving a Story",
          15: "Those women longed for the touch of others' lips, and thus invited their kisses",
          16: "Splitting of the Breast",
          17: "Fourth Child",
          18: "Ambivalence",
          19: "Introjection",
          20: "Weaving a Story 2: Oral Stage",
          21: "He was aware that he was still a child",
          22: "Don't Be",
          23: "Rei III",
          24: "The Beginning and the End, or \"Knockin' on Heaven's Door\"",
          25: "Do you love me?",
          26: "Take care of yourself",
          27: "The End of Evangelion",
          28: "Evangelion 2.22: You Can (Not) Advance",
          29: "Evangelion: 3.33 You Can (Not) Redo",
          30: "Evangelion: 3.0 + 1.0 Thrice Upon A Time"
          }

token = 'dog'
fb = facebook.GraphAPI(access_token=token)

# Posts frame to facebook, using param text as the post text
def post_to_fb(text, path):
  post_id = fb.put_photo(image=open(path, 'rb'), connection_name='feed', message=text)
  return int(post_id["id"])

# For testing
def post_to_terminal(text, path):
  return 0

def main():

  # finding what episode and frame was last posted
  with open('next_frame.txt', 'r') as f:
    frame = int(f.readline())
    episode = int(f.readline())

  if episode == 31:
    sys.exit()

  total_frames = len(glob.glob(f"{episode}/*"))

  text = f"Episode {episode} - {titles[episode]} - Frame {frame} of {total_frames}"
  # the () below are for convienience, as I use the default windows renaming method to reorganize the frames when I need to make edits
  path = f"{episode}/({frame}).PNG"

  if (len(sys.argv)-1 > 0):
    post_id = post_to_terminal(text, path)

  else:
    post_id = post_to_fb(text, path)


  print(f"Posted {episode}-{frame} of {total_frames} with post ID: {post_id}")
  frame += 1

  if frame > total_frames:
    episode += 1
    frame = 1

  with open('next_frame.txt', 'w') as f:
    f.write(str(frame)+"\n")
    f.write(str(episode))

if __name__ == '__main__':
  sys.exit(main() or 0)
