from Evaluator import *
from utils import *
import os
import argparse


def read_file(filename):
    """
    Parses the input .csv file and returns a list of bounding box objects corresponding to each math region in the file.
    :param filename:
    :return: List<BoundingBox>
    """
    fh1 = open(filename, "r")
    bboxes = []
    for line in fh1:
        line = line.replace("\n", "")
        if line.replace(' ', '') == '':
            continue
        splitLine = line.split(",")
        idClass = splitLine[0]
        x = float(splitLine[1])
        y = float(splitLine[2])
        w = float(splitLine[3])
        h = float(splitLine[4])
        bb = BoundingBox(
            "test",
            1,
            x,
            y,
            w,
            h,
            CoordinatesType.Absolute, (200, 200),
            BBType.GroundTruth,
            format=BBFormat.XYWH)
        bboxes.append(bb)
    fh1.close()
    return bboxes

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--detections", type=str, required=True, help="detections.csv file")
    parser.add_argument("--ground_truth", type=str, required=True, help="ground_truth.csv file")
    args = parser.parse_args()

    evaluator = Evaluator()

    if (os.path.isfile(args.detections)):
        detections = read_file(args.detections)
    else:
        raise  ValueError("Invalid detections file")

    if len(detections)==0:
        raise ValueError("Empty detections file or not in valid format")

    if (os.path.isfile(args.ground_truth)):
        gts = read_file(args.ground_truth)
    else:
        raise ValueError("Invalid ground truth file")

    if len(gts)==0:
        raise ValueError("Empty ground truths file or not in valid format")

    # For each ground truth bounding box, returns list of detection boxes in descending order of IoU along with IoU value.
    for gt in gts:
        ious = evaluator._getAllIOUs(gt, detections)
        print(ious)