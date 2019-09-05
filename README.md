# TFD-ICDAR 2019: A Dataset for Typeset Math Formula Detection

Developed at the [Document and Pattern Recognition Laboratory](https://www.cs.rit.edu/~dprl/index.html)  
(Rochester Institute of Technology, USA)

by [Parag Mali](https://paragmali.me), Puneeth Kukkadapu, Mahshad Madhavi

<img src="https://github.com/maliparag/TFD-ICDAR2019/blob/master/Cc-by-nc-nd_icon.png"/>

This dataset was created with permissions from the creators of the [GTDB datasets](https://github.com/uchidalab/GTDB-Dataset). Any questions regarding any other derivatives of the dataset need to be directed back to the creators of GTDB.

## Table of Contents
- <a href='#introduction'>Introduction</a>
- <a href='#dataset-statistics'>Dataset statistics</a>
- <a href='#download-instructions'>Download instructions</a>
- <a href='#evaluation-tool'>Evaluation Tool</a>
- <a href='#related-publications'>Related Publications</a>
- <a href='#acknowledgements'>Acknowledgements</a>
- <a href='#contact-information'>Contact information</a>

## Introduction

This dataset was used for Competition on Recognition of Handwritten Mathematical Expressions and Typeset Formula Detection (CROHME + TFD 2019) at the 15th International Conference on Document Analysis and Recognition (ICDAR 2019).

It was developed using the annotations from the [GTDB datasets](https://github.com/uchidalab/GTDB-Dataset). TFD-ICDAR 2019 dataset provides character locations, OCR codes, and, bounding boxes for math regions in PDF documents.

Directory structure is explained below:

1) Training and testing data are provided in directories `Train` and `Test`, respectively.

2) In `Train` there are math and character region annotations under directory `math_gt` and `char_gt`, respectively.

3) In `Test` there is a directory called `input`. The annotations in `input` can be used if character level information is required at inference time. The ground truths for test data are provided in directory `gt`. 


The ground truth annotations are provided at character level and math level:

1) Character level: bounding box of all characters are given with math/not-math labelling. Each character record has following values -`1:Page number, 2:Character id, 3-7:bounding box (left, top, right, bottom), 8:ORDINARY_TEXT or MATH_SYMBOL, 9: Relationship with other math characters 10: Parent math character id 11: OCR code`

For example `0,1,376.0,438.0,448.0,514.0,ORDINARY_TEXT,NONE,-1,0154`

Relationships can be one of the following:
`HORIZONTAL,RIGHT_SUB,RIGHT_SUP,LEFT_SUB,LEFT_SUP,UPPER,LOWER`

2) Math regions: bounding box of math regions are provided for each page. Each math record has following values - `1:Page number, 2-6: bounding box (left, top, right, bottom)`

The article pages were originally scanned at 600 dpi. Although we could not include the original document images of articles for copyright reasons, we provide the pdf URLs that we used to get the original documents.

## Dataset Statistics

|                                             | Train | Test  |
|---------------------------------------------|-------|-------|
| Number of documents                         | 36    | 10    |
| Number of pages                             | 569   | 236   |
| Number of single-character math expressions | 7506   | 2556  |
| Number of multi-character math expressions  | 18890 | 9329  |
| Total Number of math expressions            | 26396 | 11885 |

## Download Instructions

```EasyDownload``` directory provides tools to download PDF files used in the dataset.

1) Download all pdfs from the given URLs in GTDB_files.txt. Make sure the saved files have the name in the second column (for mapping with GT files).

2) Convert pdfs to images using ```convert_pdf_to_image.py```

3) Use the GTs provided for test and train in the corresponding folders. Note that for test PDFs, character bounding boxes are provided without math/non-math labels. 


`NOTE: If you find the bounding boxes are displaced from math regions, it is because the document image that you have rendered is of different size than the one used while annotating. datasetV2 provides file sizes for each image. Resize the image that you have rendered to the size provided in datasetV2 and you should be able to use the annotations.`

## Evaluation Tool

Usage:python3 IOUevaluater.py --detections `detections` --ground_truth `ground_truths`

We provide evalutation tool ```IOULib``` that calculates precision, recall and F-score for the detection results.

This tool can be used to evaluate IoU metric for predicted math regions against ground truth math regions for each pdf file. For each pdf in test set, you should generate a csv file which contains predicted bounding box regions. Each line in the csv file corresponds to a bounding box for one math region. It consists of 5 attributes:

page number, x, y, x2, y2 

`detections` contains `pdf_name.csv` files with predicted math regions and `ground_truths` contains <pdf_name.csv> files with ground-truth math regions.

For each math region in `ground_truths`, the IoU metric is computed for every math region in `detecions` (per page) and returns a sorted list of `ground_truth: IOU score,detection` in descending order. This information is saved for each page in a folder named `IOU_scores_pages`.

## Additional Tools

```visualize_annotations.py``` visualize math regions and character regions from annotation files on images. Find this under VisualizationTools. 

```convert_pdf_to_image.py``` converts PDF file into 600 DPI images.

## Dataset Versions

`TFD-ICDAR2019v1` was used in the ICDAR 2019 competition on the Tyepset Formula Detection (TFD). `Vesrion 2` of the TFD-ICDAR 2019 dataset fixed errors in `Version 1`. All the character annotations were updated to fit the characters and missing bounding boxes were added. `Version 2` is available under directory `TFD-ICDAR2019v2`. `IOULib` in `Version 2` was updated to provide file level results and it allows us to specify different IoU thresholds. Other tools were updated to work with csv, math, and, char files. `Version 2` provides file sizes of images used to create annotations.

## Related Publications

If you are using this dataset, please cite following paper:

M. Mahdavi, R. Zanibbi, H. Mouchere, and Utpal Garain (2019). [ICDAR 2019 CROHME + TFD: Competition on Recognition of Handwritten Mathematical Expressions and Typeset Formula Detection.](https://www.cs.rit.edu/~rlaz/files/CROHME+TFD%E2%80%932019.pdf) Proc. International Conference on Document Analysis and Recognition, Sydney, Australia (to appear).

## Acknowledgements

This dataset was developed using the annotations from the [GTDB datasets](https://github.com/uchidalab/GTDB-Dataset). If you have any questions regarding the license please contact GTDB dataset creators.

The copyright and license holder of GTDB datasets is  
Masakazu Suzuki  
[Science Accessibility Net](http://www.sciaccess.net/en/),  
Professor emeritus of Kyushu University

We would also like to thank Rafael Padilla for the [intersection over union calculator](
https://github.com/rafaelpadilla/Object-Detection-Metrics).

## Contact Information

Please direct questions or concerns regarding the dataset to Parag Mali (psm2208@rit.edu) or Richard Zanibbi (rxzvcs@rit.edu).
