import os
import argparse
import time
pjoin = os.path.join
parser = argparse.ArgumentParser(description='Photorealistic Image Stylization')
parser.add_argument('--UHD', action='store_true', default=False)
parser.add_argument('--gpu', type=int)
parser.add_argument('--mode', type=str)
args = parser.parse_args()

TIME_ID = os.environ["SERVER"] + time.strftime("-%Y%m%d-%H%M")
img_dir = "./images/UHD" if args.UHD else "./images"
out_dir = "results"

for i in range(102): # 102 pairs
  content = pjoin(img_dir, "in%s.png" % (i+1))
  style   = pjoin(img_dir, "in%s_style.png" % (i+1))
  output  = pjoin(out_dir, "in%s_%s_%s.png" % (i+1, args.mode, TIME_ID))
  if_existed = sum(["in%s_%s" % (i+1, args.mode) in imgname for imgname in os.listdir(out_dir) if imgname.endswith(".png")])
  if if_existed:
    print("========> %d: pwct of '%s' has existed (mode=%s), process next" % (i+1, content, args.mode))
    continue
  script = "python demo.py --content_image_path {} --style_image_path {} --output_image_path {} --mode {} --cuda {}".format(content, style, output, args.mode, args.gpu)
  os.system(script)
  print("========> %d: pwct of '%s' done" % (i+1, content))
print(TIME_ID)