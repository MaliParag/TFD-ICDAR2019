# ICDAR 2019 Dataset for Typeset Math Formula Detection

## Introduction

This dataset was used for Competition on Recognition of Handwritten Mathematical Expressions and Typeset Formula Detection (CROHME + TFD 2019) at the 15th International Conference on Document Analysis and Recognition (ICDAR 2019).

It was developed using the annotations from the [GTDB datasets](https://github.com/uchidalab/GTDB-Dataset). ICDAR 2019 dataset provides character locations, OCR codes, and, bounding boxes for math regions in PDF documents.

## Dataset statistics

| 					    	                       | Train | Test  |
|---------------------------------------------|-------|-------|
| Number of documents                         | 36    | 10    |
| Number of pages                             | 569   | 236   |
| Number of single-character math expressions | 148   | 38    |
| Number of multi-character math expressions  | 26248 | 11847 |
| Total Number of math expressions            | 26396 | 11885 |

## Download instructions

The ground truth annotation provided in two formats

1) character level: bounding box of all characters are given with math/notmath labelling.

2) math regions: bounding box of math regions are provided for each page 

The article pages were originally scanned at 600 dpi. Although we could not include the original document images of articles for copyright reasons, we provide the pdf URLs that we used to get the original documents.

1) Download all pdfs from the given URLs in GTDB_files.txt. Make sure the saved files have the name in the second column (for mapping with GT files).

2) Convert pdfs to images using ```convert_pdf_to_image.py```

3) Use the GTs provided for test and train in the corresponding folders. Note that for test PDFs, character bounding boxes are provided without math/non-math labels. 

## Evaluation Tool

We provide evalutation tool ```IOU_lib``` that calculates precision, recall and F-score for the detection results.

This tool can be used to evaluate IoU metric for predicted math regions against ground truth math regions for each pdf file. For each pdf in test set, you should generate a csv file which contains predicted bounding box regions. Each line in the csv file corresponds to a bounding box for one math region. It consists of 5 attributes:

page number, x, y, x2, y2 

`detections` contains `pdf_name.csv` files with predicted math regions and `ground_truths` contains <pdf_name.csv> files with ground-truth math regions.

For each math region in `ground_truths`, the IoU metric is computed for every math region in `detecions` (per page) and returns a sorted list of `ground_truth: IOU score,detection` in descending order. This information is saved for each page in a folder named `IOU_scores_pages`.

Usage:python3 IOUevaluater.py --detections `detections` --ground_truth `ground_truths`

## Additional Tools

```visualize_annotations.py``` visualize math regions and character regions from annotation files on images. Find this under VisualizationTools. 

```GTDB_files.txt``` is a list of all 46 articles.

```convert_pdf_to_image.py``` converts PDF file into 600 DPI images.

## Contributors 

Parag Mali and Puneeth Kukkadapu worked on the preparation of the ICDAR 2019 dataset. Puneeth Kukkadapu and Mahshad Madhavi developed tools for evaluation, download, and visualization. 

Parag Mali created `Vesrion 2` of the ICDAR 2019 dataset after fixing many errors in ICDAR 2019. `Version 2` is available under directory `datasetV2`. `IOU_libV2` provides file level results and allows us to specify different IoU thresholds.    

## Acknowledgements

This dataset was developed using the annotations from the [GTDB datasets](https://github.com/uchidalab/GTDB-Dataset). 

The copyright and license holder of GTDB datasets is  
Masakazu Suzuki  
[Science Accessibility Net](http://www.sciaccess.net/en/),  
Professor emeritus of Kyushu University



