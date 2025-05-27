
from matplotlib import pyplot
from matplotlib.patches import Rectangle
from PIL import Image, ImageDraw, ImageFont

def encoder_dic(valid_data):
    data_dic = {}
    (valid_boxes, valid_labels, valid_scores) = valid_data
    for box, label, score in zip(valid_boxes, valid_labels, valid_scores):
        if label not in data_dic:
            data_dic[label] = [[score, box, 'kept']]
        else:
            data_dic[label].append([score, box, 'kept'])

    return data_dic

def draw_boxes(filename, valid_data):
    # Open image
    image = Image.open(filename)
    draw = ImageDraw.Draw(image)

    # Load font (use default if TTF unavailable)
    try:
        font = ImageFont.truetype("arial.ttf", 16)
    except:
        font = ImageFont.load_default()

    boxes, labels, scores = valid_data

    for i in range(len(boxes)):
        box = boxes[i]
        label = labels[i]
        score = scores[i]

        x1, y1, x2, y2 = box.xmin, box.ymin, box.xmax, box.ymax

        # Draw rectangle
        draw.rectangle([x1, y1, x2, y2], outline="red", width=3)

        # Draw label text
        text = f"{label} ({score:.2f})"
        draw.text((x1, y1 - 15), text, fill="red", font=font)

    # 💾 Save modified image back to original filename
    image.save(filename)